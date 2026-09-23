from __future__ import annotations

import argparse
import csv
import io
import json
import socket
import ssl
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from . import __version__


@dataclass
class Finding:
    id: str
    title: str
    category: str
    severity: str
    confidence: str
    target: str
    description: str
    remediation: str
    evidence: dict = field(default_factory=dict)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(value)


def normalize_target(value: str) -> tuple[str, str]:
    raw = value.strip()
    parsed = urlparse(raw if "://" in raw else f"https://{raw}")
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("target must be a domain or http(s) URL")
    host = parsed.hostname.rstrip(".").lower()
    try:
        socket.inet_aton(host)
    except OSError:
        if not all(part and (part.replace("-", "").isalnum()) for part in host.split(".")) or "." not in host:
            raise ValueError("target must contain a valid hostname or IPv4 address")
    return host, f"{parsed.scheme}://{host}{(':'+str(parsed.port)) if parsed.port else ''}/"


def is_private(host: str) -> bool:
    try:
        import ipaddress
        addresses = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)
        return any(ipaddress.ip_address(item[4][0]).is_private or ipaddress.ip_address(item[4][0]).is_loopback or ipaddress.ip_address(item[4][0]).is_link_local for item in addresses)
    except (OSError, ValueError):
        return False


def request(url: str, timeout: float, max_bytes: int = 2_000_000):
    req = Request(url, headers={"User-Agent": f"EternalView/{__version__}"})
    try:
        with urlopen(req, timeout=timeout) as response:
            body = response.read(max_bytes + 1)
            return response.status, dict(response.headers.items()), body, response.geturl(), None
    except HTTPError as exc:
        return exc.code, dict(exc.headers.items()), b"", url, str(exc)
    except (URLError, TimeoutError, OSError) as exc:
        return None, {}, b"", url, str(exc)


def add_header_findings(target, headers, findings):
    lower = {key.lower(): value for key, value in headers.items()}
    checks = {
        "strict-transport-security": ("http.missing_hsts", "Missing Strict-Transport-Security", "medium", "Configure HSTS after validating HTTPS coverage."),
        "content-security-policy": ("http.missing_csp", "Missing Content-Security-Policy", "low", "Define a restrictive Content-Security-Policy."),
        "x-content-type-options": ("http.missing_x_content_type_options", "Missing X-Content-Type-Options", "low", "Set X-Content-Type-Options: nosniff."),
        "referrer-policy": ("http.missing_referrer_policy", "Missing Referrer-Policy", "low", "Configure an appropriate Referrer-Policy."),
        "permissions-policy": ("http.missing_permissions_policy", "Missing Permissions-Policy", "informational", "Restrict browser features not required by the application."),
    }
    for header, (fid, title, severity, remediation) in checks.items():
        if header not in lower:
            findings.append(Finding(fid, title, "http", severity, "high", target, f"The response did not include {header}.", remediation, {"header": header}))
    cookies = lower.get("set-cookie", "").lower()
    if cookies and "secure" not in cookies:
        findings.append(Finding("http.cookie_missing_secure", "Cookie may be missing Secure", "http", "medium", "medium", target, "A Set-Cookie response did not visibly include Secure.", "Set Secure on cookies delivered over HTTPS.", {}))


def check_http(host, base, timeout, findings):
    status, headers, body, final_url, error = request(base, timeout)
    if error:
        findings.append(Finding("http.request_failed", "HTTP request failed", "availability", "informational", "high", host, error, "Verify that the target is reachable.", {"url": base}))
        return
    add_header_findings(host, headers, findings)
    parser = LinkParser()
    try:
        parser.feed(body.decode("utf-8", errors="replace"))
    except Exception:
        pass
    findings.append(Finding("http.response_observed", f"HTTP response received ({status})", "availability", "informational", "high", host, "The target returned an HTTP response.", "No action required.", {"status": status, "final_url": final_url, "link_count": len(parser.links)}))


def check_tls(host, timeout, findings):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, 443), timeout=timeout) as raw:
            with context.wrap_socket(raw, server_hostname=host) as sock:
                cert = sock.getpeercert()
                not_after = cert.get("notAfter")
                expires = ssl.cert_time_to_seconds(not_after) if not_after else None
                days = int((expires - time.time()) / 86400) if expires else None
                if days is not None and days < 30:
                    severity = "high" if days < 0 else "medium"
                    findings.append(Finding("tls.certificate_expiry", "TLS certificate expires soon or is expired", "tls", severity, "high", host, f"Certificate validity remaining: {days} days.", "Renew the certificate and deploy the renewed chain.", {"days_remaining": days}))
                findings.append(Finding("tls.observed", "TLS certificate and protocol observed", "tls", "informational", "high", host, "A certificate-verified TLS connection succeeded.", "No action required.", {"version": sock.version(), "cipher": sock.cipher()[0] if sock.cipher() else None, "days_remaining": days}))
    except (OSError, ssl.SSLError) as exc:
        findings.append(Finding("tls.connection_failed", "TLS connection failed", "tls", "medium", "medium", host, str(exc), "Use a valid certificate and support modern TLS versions.", {}))


def check_dns(host, timeout, findings):
    try:
        addresses = sorted({item[4][0] for item in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)})
        findings.append(Finding("dns.addresses", "DNS addresses resolved", "dns", "informational", "high", host, "The hostname resolved successfully.", "No action required.", {"addresses": addresses}))
    except OSError as exc:
        findings.append(Finding("dns.resolution_failed", "DNS resolution failed", "dns", "medium", "high", host, str(exc), "Check DNS records and nameserver availability.", {}))


def check_security_txt(host, base, timeout, findings):
    status, headers, body, final_url, error = request(base.rstrip("/") + "/.well-known/security.txt", timeout)
    if error or status != 200:
        findings.append(Finding("security_txt.missing", "security.txt was not found", "security.txt", "informational", "high", host, "The standard security contact file was unavailable.", "Publish /.well-known/security.txt with a valid security contact if appropriate.", {"status": status}))
        return
    text = body.decode("utf-8", errors="replace")
    fields = {line.split(":", 1)[0].strip().lower() for line in text.splitlines() if ":" in line and not line.lstrip().startswith("#")}
    if "contact" not in fields:
        findings.append(Finding("security_txt.missing_contact", "security.txt has no Contact field", "security.txt", "low", "high", host, "No Contact field was found.", "Add at least one security contact address or URL.", {"url": final_url}))
    else:
        findings.append(Finding("security_txt.present", "security.txt is present", "security.txt", "informational", "high", host, "A security contact file was found.", "Keep the file current and ensure its Expires value remains valid.", {"fields": sorted(fields), "url": final_url}))


def render(findings, metadata, fmt):
    data = {"schema_version": "1.0", "tool": {"name": "EternalView", "version": __version__}, "scan": metadata, "findings": [asdict(f) for f in findings]}
    if fmt == "json":
        return json.dumps(data, indent=2)
    if fmt == "csv":
        output = io.StringIO(); writer = csv.writer(output); writer.writerow(["id", "severity", "confidence", "category", "target", "title", "description", "remediation"])
        for f in findings: writer.writerow([f.id, f.severity, f.confidence, f.category, f.target, f.title, f.description, f.remediation])
        return output.getvalue()
    lines = [f"# EternalView report: {metadata['target']}", "", f"Generated: {metadata['completed_at']}", "", "## Findings", ""]
    for f in findings:
        lines += [f"### [{f.severity.upper()}] {f.title}", f"- ID: `{f.id}`", f"- Confidence: {f.confidence}", f"- Description: {f.description}", f"- Remediation: {f.remediation}", f"- Evidence: `{json.dumps(f.evidence, sort_keys=True)}`", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Authorized, defensive web security posture checks")
    parser.add_argument("target", help="domain or HTTP(S) URL")
    parser.add_argument("--format", choices=["terminal", "json", "markdown", "csv"], default="terminal")
    parser.add_argument("--output", help="write report to a file")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--allow-private", action="store_true", help="allow private/loopback targets when explicitly authorized")
    args = parser.parse_args(argv)
    try:
        host, base = normalize_target(args.target)
        if is_private(host) and not args.allow_private:
            raise ValueError("private, loopback, and link-local targets are blocked by default; use --allow-private only for authorized testing")
    except ValueError as exc:
        parser.error(str(exc))
    started = datetime.now(timezone.utc)
    findings = []
    check_http(host, base, args.timeout, findings)
    check_tls(host, args.timeout, findings)
    check_dns(host, args.timeout, findings)
    check_security_txt(host, base, args.timeout, findings)
    completed = datetime.now(timezone.utc)
    metadata = {"target": host, "started_at": started.isoformat(), "completed_at": completed.isoformat(), "duration_seconds": round((completed-started).total_seconds(), 3), "timeout_seconds": args.timeout}
    output = render(findings, metadata, "markdown" if args.format == "terminal" else args.format)
    if args.output:
        with open(args.output, "w", encoding="utf-8", newline="") as handle: handle.write(output)
    else:
        print(output)
    return 0

if __name__ == "__main__":
    sys.exit(main())
