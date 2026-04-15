# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| main    | Yes       |
| develop | No        |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, please send an email to: [palvchx@gmail.com]

You can expect a response within 48 hours. If the issue is confirmed, a patch will be 
released as soon as possible.

## Security Measures

This project implements the following security controls:
- SAST (Static Application Security Testing) via Bandit and Semgrep
- Secret scanning via Gitleaks
- Dependency scanning (SCA) via pip-audit
- Container scanning via Trivy
- Image signing via Cosign (Sigstore)
- SBOM generation via Syft (CycloneDX)
- DAST (Dynamic Application Security Testing) via OWASP ZAP