# EternalView

EternalView is a defensive, authorized security-posture checker for modern web-facing infrastructure. It focuses on passive, low-impact validation of HTTP, TLS, DNS, and security metadata so teams can evaluate exposure and configuration quality without moving into exploit capabilities.

This project was originally a single interactive Bash menu script. It has been modernized into a safer CLI-first workflow with structured findings, explicit target validation, and report generation suitable for automation and review.

## Why this version exists

The original script was useful as a learning project and quick reconnaissance tool, but it had several maintenance and safety risks:

- monolithic shell logic
- repeated self-invocation and menu recursion
- unquoted user input and unsafe shell execution patterns
- missing dependency validation
- no test coverage or CI validation
- no structured reporting
- no explicit safety boundary for target scope
- no separation between passive checks and exploit-oriented behavior

The updated version addresses those issues by:

- moving the logic to a structured Python implementation
- keeping a Bash launcher for compatibility
- validating target input before requests are made
- blocking private, loopback, and link-local targets by default
- disabling exploit-style workflow paths
- generating structured output in terminal, JSON, Markdown, and CSV
- making the tool easier to extend with future checks

## Safety policy

EternalView is intended only for systems that the user owns or is explicitly authorized to assess.

The project does not perform exploitation workflows, credential attacks, destructive actions, or automated privilege escalation.

By default, the CLI blocks:

- private IP ranges
- loopback addresses
- link-local ranges
- malformed or empty targets

Use `--allow-private` only if you are explicitly authorized to assess internal targets and understand the scope.

## Installation

### From source

```bash
git clone https://github.com/rpranshu/EternalView.git
cd EternalView
python3 -m pip install -e .
```

### Run without installation

```bash
python3 -m eternalview example.com
```

### Bash launcher

The repository still includes the original launcher script, which now forwards execution to the Python CLI:

```bash
./EternalView.sh example.com
./EternalView.sh example.com --format json --output report.json
```

## Quick start

### Basic scan

```bash
eternalview example.com
```

### JSON report

```bash
eternalview example.com --format json --output report.json
```

### Markdown report

```bash
eternalview example.com --format markdown --output report.md
```

### CSV report

```bash
eternalview example.com --format csv --output report.csv
```

### Target with explicit private-target override

```bash
eternalview 127.0.0.1 --allow-private
```

## Command-line options

```bash
eternalview --help
```

Supported options include:

- `target` positional argument: domain or URL
- `--format {terminal,json,markdown,csv}`: output mode
- `--output PATH`: write results to a file
- `--timeout SECONDS`: request timeout per check
- `--allow-private`: permit private, loopback, and link-local target assessment when explicitly authorized

## Output formats

### Terminal view

Default output is human-readable, concise, and suitable for quick checks in a terminal.

### JSON

Machine-readable output designed for automation, integration, or storing report data.

Example shape:

```json
{
  "schema_version": "1.0",
  "tool": {
    "name": "EternalView",
    "version": "3.0.0"
  },
  "scan": {
    "target": "example.com",
    "started_at": "2026-09-23T00:00:00+00:00",
    "completed_at": "2026-09-23T00:00:02+00:00",
    "duration_seconds": 2.0
  },
  "findings": [
    {
      "id": "http.missing_hsts",
      "title": "Missing Strict-Transport-Security",
      "category": "http",
      "severity": "medium",
      "confidence": "high",
      "target": "example.com",
      "description": "The response did not include the HSTS policy header.",
      "remediation": "Configure HSTS after validating HTTPS coverage.",
      "evidence": {
        "header": "strict-transport-security"
      }
    }
  ]
}
```

### Markdown

Useful for documentation, review comments, and reporting in GitHub or docs systems.

### CSV

Useful for spreadsheet-based review, filtering, or importing into other tools.

## Included checks

The current release includes the following low-impact checks:

- HTTP response validation
- HTTP header review
- missing security header detection
- cookie security flag evaluation
- TLS connection and certificate validity checks
- DNS resolution validation
- `/.well-known/security.txt` presence and basic field checks
- link extraction from HTML responses

The tool reports findings as indicators, not absolute proof of vulnerabilities. Each result includes:

- a finding ID
- severity
- confidence
- target
- description
- remediation guidance
- evidence data

## Current architecture

The codebase now follows a modern structure designed for maintainability:

```text
EternalView/
├── EternalView.sh            # Bash launcher
├── pyproject.toml            # Python packaging metadata
├── README.md                 # Project documentation
├── SECURITY.md               # Safety and reporting guidance
├── src/
│   └── eternalview/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       └── ...
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── ...
└── docs/
```

## Recent improvements over the original script

### Security and reliability

- removed recursive self-relaunch behavior
- fixed invalid shell syntax and undefined variable issues
- added dependency checks
- validated target format before scanning
- prevented execution against private networks by default
- disabled exploit-oriented Autopwn behavior in the interface
- added safe request timeout handling

### Maintainability

- migrated the implementation to Python
- introduced structured code organization
- separated CLI, model, and reporting logic
- prepared a path for incremental check expansion
- added CI validation for syntax and packaging basics

### Reporting

- added machine-readable JSON output
- added Markdown reporting for documentation and review
- added CSV output for spreadsheets and import workflows
- standardized finding metadata and remediation guidance

### Safety-first posture

- no brute-force actions by default
- no destructive or exploit actions
- no credential collection
- no automatic scope expansion beyond the provided target
- opt-in private target support

## Known limitations

This version intentionally focuses on defensive, passive checks. It does not yet include:

- full asset discovery
- subdomain enumeration
- certificate transparency-based reconnaissance
- advanced DNS posture analysis beyond address resolution
- rich HTML report generation
- customizable policy-driven custom checks
- plugin-based extensibility beyond the internal structure

These are planned next steps in the modernization roadmap.

## Roadmap

Planned future work includes:

- command-based check modularity (`dns`, `tls`, `headers`, `security-txt`, etc.)
- advanced DNS posture checks
- redirect analysis and canonical host detection
- certificate transparency discovery
- HTML report generation
- policy-based scanning configuration
- plugin architecture
- comprehensive unit and integration testing
- live security posture comparison over time

## Contributing

Contributions are welcome if they align with the project’s defensive and ethics-first goals.

Before proposing new functionality, ensure it:

- does not introduce exploit capabilities
- remains passive and low-impact
- respects user authorization and scope
- includes appropriate tests
- remains compatible with the project’s safety-first policy

## License

This project is distributed under the repository's chosen license. See the repository root for the current license file.

## Security reporting

If you discover a project security issue, please report it through the repository's supported security disclosure path rather than creating a public issue that discloses sensitive details.

For more details, see `SECURITY.md`.
