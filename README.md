# EternalView

EternalView 3 is a defensive, authorized security-posture checker. It performs low-impact HTTP, TLS, DNS, and `security.txt` checks and produces terminal, JSON, Markdown, or CSV reports.

## Quick start

```bash
python3 -m eternalview example.com
python3 -m eternalview example.com --format json --output report.json
./EternalView.sh example.com --format markdown --output report.md
```

Install locally with:

```bash
python3 -m pip install -e .
```

Private, loopback, and link-local targets are blocked by default. Use `--allow-private` only for systems you own or are explicitly authorized to assess. The project does not execute exploitation workflows.

## Checks

- HTTP security headers and cookie flags
- HTTP response and link-count metadata
- TLS certificate expiry, protocol, and cipher
- DNS address resolution
- `/.well-known/security.txt`

Results are indicators, not proof of vulnerabilities. Review findings in context.
