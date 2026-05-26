# Secure CI/CD Pipeline

![Security Gate I](https://github.com/palvch0/secure-cicd-pipeline/actions/workflows/security-gate-1.yml/badge.svg)
![Build and Container Security](https://github.com/palvch0/secure-cicd-pipeline/actions/workflows/build-and-scan.yml/badge.svg)
![DAST](https://github.com/palvch0/secure-cicd-pipeline/actions/workflows/dast.yml/badge.svg)

Security-focused CI/CD pipeline — master's thesis project

## Opis projektu

Projekt implementuje kompleksowy pipeline bezpieczeństwa dla aplikacji webowej
opartej na FastAPI. Pipeline automatycznie wykrywa podatności bezpieczeństwa
na każdym etapie wytwarzania oprogramowania zgodnie z filozofią DevSecOps.

## Architektura pipeline'u

Code Push → GitHub Actions
├── Security Gate I (równolegle)
│   ├── SAST: Bandit + Semgrep (własne reguły CWE-327, CWE-89)
│   ├── Secret Scan: Gitleaks (własne reguły detekcji)
│   └── SCA: pip-audit (baza OSV)
├── Docker Build → GHCR
├── Security Gate II (równolegle)
│   ├── IaC Scan: Checkov
│   ├── Container Scan: Trivy
│   ├── Image Signing: Cosign (Sigstore/SLSA Level 2)
│   └── SBOM: Syft (CycloneDX)
├── DAST: OWASP ZAP (API scan z OpenAPI)
└── Deploy: SSH → VPS (workflow gotowy)

## Narzędzia bezpieczeństwa

| Kategoria | Narzędzie | Cel | Standard |
|-----------|-----------|-----|----------|
| SAST | Bandit | Podatności w kodzie Python | CWE |
| SAST | Semgrep | Własne reguły detekcji | CWE-327, CWE-89 |
| Secret Scan | Gitleaks | Sekrety w historii git | OWASP A02 |
| SCA | pip-audit | Podatne zależności | OSV/CVE |
| IaC Scan | Checkov | Misconfiguracje Dockerfile | CKV |
| Container Scan | Trivy | Podatności w obrazie Docker | CVE |
| Image Signing | Cosign | Podpisywanie obrazów | SLSA Level 2 |
| SBOM | Syft | Software Bill of Materials | CycloneDX |
| DAST | OWASP ZAP | Dynamiczne testy bezpieczeństwa | OWASP Top 10 |

## Celowe podatności demonstracyjne

Gałąź `develop` zawiera celowo wbudowane podatności:

| # | Podatność | Plik | Wykrywa |
|---|-----------|------|---------|
| 1 | Hardcoded SECRET_KEY | `app/config.py:4` | Gitleaks, Bandit |
| 2 | Słabe hashowanie MD5 | `app/routers/users.py:28` | Bandit, Semgrep |
| 3 | SQL Injection | `app/routers/users.py:55` | Bandit, Semgrep |
| 4 | Kontener jako root | `Dockerfile` | Checkov |

## Wyniki skanowania

- **Bandit**: 3 podatności (High: 1, Medium: 1, Low: 1)
- **Semgrep**: 2 podatności (własne reguły: CWE-327, CWE-89)
- **Gitleaks**: 2 sekrety wykryte w historii commitów
- **pip-audit**: 0 podatności w zależnościach
- **Checkov**: 2 misconfiguracje w Dockerfile
- **Trivy**: 110 podatności w obrazie bazowym
- **OWASP ZAP**: 2 ostrzeżenia (brakujące nagłówki HTTP)

## Wnioski badawcze

Projekt potwierdza że SAST i DAST są narzędziami komplementarnymi.
SQL Injection został wykryty przez SAST (analiza statyczna kodu),
natomiast DAST (OWASP ZAP) nie wykrył go dynamicznie ze względu
na domyślną obsługę wyjątków FastAPI która nie ujawnia błędów SQL.

## Standardy i frameworki

- OWASP Top 10 (2021)
- SLSA Level 2 (Supply-chain Levels for Software Artifacts)
- CWE (Common Weakness Enumeration)
- CycloneDX SBOM Standard
- US Executive Order 14028 (SBOM requirement)

## Technologie

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green)
![Docker](https://img.shields.io/badge/Docker-containerized-blue)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)