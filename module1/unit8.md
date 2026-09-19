# Unit 8 · Principles of Cyber Security

> A phishing incident, its mitigations, and the ethics behind defending against it.

## Task / Assignment
Analyse a hypothetical cyber-attack and build a mitigation + ethical response.

### Scenario
A trading firm's staff receive a phishing email — sender shows "HR Department" but from a disguised external
mailbox — titled *"Your 2026 Salary Increase — confirm payroll before Friday"*, demanding bank/identity details
via a link (or else forfeit the raise). A virus in the link could open the internal network.

### Threat analysis
Classic phishing: lures users into handing over sensitive data; firewalls + email filters alone are **not enough**.

### Mitigation
- **Training** so staff check the true sender and never click suspicious links.
- **Data segregation** — separate sensitive DBs from public ones; least-privilege access.
- **MFA** on every account (a stolen password alone is insufficient).
- **Network segmentation** — keep the customer DB off general office traffic.
- **Compliance** — GDPR 72-hour breach notification; adopt **ISO/IEC 27001** controls.

### Ethical considerations
- **User privacy** — transparency + user control over collected data.
- **Duty of care** — protect employee payroll data with the same rigour as client data.
- **Consent in drills** — fake-phishing simulations should include informed consent / a clear debrief.
- **Just culture** — review the *process*, not blame the individual who clicked.

## Associated source files
| File | Type | Notes |
|------|------|-------|
| `Unit8 Cybersecurity Threat Assessment and Mitigation Plan.docx` | Word | Full case analysis, mitigation plan and ethics discussion |

## Core idea
Defence is technical **and** human — and must stay fair to the people it protects.
