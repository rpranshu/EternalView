#!/usr/bin/env bash
set -uo pipefail

# EternalView: authorized reconnaissance and information gathering only.
# This is a hardened Bash rewrite of the original script.

require_cmds() {
  local missing=0
  for cmd in "$@"; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
      echo "[ERROR] Missing required dependency: $cmd" >&2
      missing=1
    fi
  done
  return "$missing"
}

trim_target() {
  local value="${1:-}"
  value="${value#http://}"
  value="${value#https://}"
  value="${value%%/*}"
  printf '%s' "$value"
}

is_valid_target() {
  local value
  value="$(trim_target "${1:-}")"
  [[ -n "$value" ]] || return 1
  [[ "$value" =~ ^([A-Za-z0-9.-]+\.[A-Za-z]{2,}|localhost|[0-9]{1,3}(\.[0-9]{1,3}){3})$ ]]
}

prompt_target() {
  local label="$1" value
  echo -en "$label"
  IFS= read -r value || return 1
  value="$(trim_target "$value")"
  if ! is_valid_target "$value"; then
    echo "[ERROR] Invalid target. Use a domain (example.com) or IPv4 address." >&2
    return 1
  fi
  printf '%s' "$value"
}

pause() {
  echo -en "\nPress Enter to continue..."
  IFS= read -r _ || true
}

banner() {
  clear 2>/dev/null || true
  echo "========================================="
  echo "EternalView - authorized information gathering"
  echo "========================================="
  echo
  echo "1) Whois information"
  echo "2) DNS lookup"
  echo "3) Web technology detection"
  echo "4) IP locator"
  echo "5) Nmap scan"
  echo "6) Cloudflare detection"
  echo "7) robots.txt"
  echo "8) WAF detection"
  echo "9) Extract embedded links"
  echo "10) HTTP headers"
  echo "11) Traceroute"
  echo "12) AutoPwn (disabled)"
  echo "13) Reload"
  echo "14) Exit"
  echo
  echo -n "Choose an option: "
}

run_whois() {
  require_cmds whois || return 1
  local target
  target="$(prompt_target 'Enter website or IP: ')" || return 1
  whois -- "$target"
}

run_dns() {
  require_cmds dig || return 1
  local target
  target="$(prompt_target 'Enter website or IP: ')" || return 1
  dig -- "$target"
}

run_tech() {
  require_cmds wget || return 1
  local target
  target="$(prompt_target 'Enter website or IP: ')" || return 1
  wget -q -- "https://builtwith.com/$target" -O log.html
  echo "Saved output to $(pwd)/log.html"
}

run_ip() {
  require_cmds curl || return 1
  local ip
  echo -en 'Enter IPv4 address: '
  IFS= read -r ip || return 1
  if ! [[ "$ip" =~ ^[0-9]{1,3}(\.[0-9]{1,3}){3}$ ]]; then
    echo "[ERROR] Invalid IPv4 address." >&2
    return 1
  fi
  curl -fsSL -- "https://ipinfo.io/$ip" | grep -v readme || true
}

run_nmap() {
  require_cmds nmap || return 1
  local mode target
  echo -en '1) Basic scan  2) Extensive scan: '
  IFS= read -r mode || return 1
  target="$(prompt_target 'Enter website or IP: ')" || return 1

  case "$mode" in
    1)
      nmap -- "$target"
      ;;
    2)
      echo "This may take time; only use on authorized targets."
      if command -v sudo >/dev/null 2>&1; then
        sudo nmap -sS -sV -vv --top-ports 1000 -T4 -O -- "$target"
      else
        nmap -sS -sV -vv --top-ports 1000 -T4 -O -- "$target"
      fi
      ;;
    *)
      echo "[ERROR] Invalid scan option." >&2
      ;;
  esac
}

run_cloudflare() {
  require_cmds dig ping || return 1
  local target ip result
  target="$(prompt_target 'Enter website or IP: ')" || return 1
  ip="$(ping -c 1 -- "$target" 2>/dev/null | grep -Eo '[0-9]{1,3}(\.[0-9]{1,3}){3}' | head -1 || true)"
  result="$(dig -- "$target" 2>/dev/null | grep -Ei 'cloudflare|103\.21|103\.22|104\.16|104\.|103\.3|104\.1|108\.162\.|131\.0|141\.101|162\.15|172\.6|173\.245|188\.114|190\.93\.|197\.234\.|198\.41' || true)"

  if [[ -n "$result" ]]; then
    echo "Runs on Cloudflare"
    echo "IP: ${ip:-unknown}"
  else
    echo "Does not appear to run on Cloudflare."
  fi
}

run_robots() {
  require_cmds curl || return 1
  local target
  target="$(prompt_target 'Enter website: ')" || return 1
  curl -fsSL -- "https://$target/robots.txt" || echo "Unable to fetch robots.txt for $target."
}

run_waf() {
  require_cmds wafw00f || return 1
  local target
  target="$(prompt_target 'Enter website or IP: ')" || return 1
  wafw00f -- "$target"
}

run_links() {
  require_cmds curl || return 1
  local target
  target="$(prompt_target 'Enter website or IP: ')" || return 1
  curl -fsSL -- "https://$target" | grep -Eo 'href="[^"]+"' | sed 's/^href="//; s/"$//' || echo "No embedded links found."
}

run_headers() {
  require_cmds curl || return 1
  local target
  target="$(prompt_target 'Enter website: ')" || return 1
  curl -fsSI -- "https://$target"
}

run_trace() {
  require_cmds traceroute || return 1
  local target
  target="$(prompt_target 'Enter website or IP: ')" || return 1
  traceroute -- "$target"
}

run_autopwn() {
  echo "AutoPwn is intentionally disabled in this version to avoid exploitation workflows."
}

main() {
  while :; do
    banner
    IFS= read -r opt || exit 0

    case "$opt" in
      1) run_whois ;;
      2) run_dns ;;
      3) run_tech ;;
      4) run_ip ;;
      5) run_nmap ;;
      6) run_cloudflare ;;
      7) run_robots ;;
      8) run_waf ;;
      9) run_links ;;
      10) run_headers ;;
      11) run_trace ;;
      12) run_autopwn ;;
      13) continue ;;
      14) exit 0 ;;
      *) echo "[ERROR] Choose a valid option." >&2 ;;
    esac

    pause
  done
}

if [[ ! -t 0 ]]; then
  echo "This script requires an interactive terminal." >&2
  exit 1
fi

main "$@"
