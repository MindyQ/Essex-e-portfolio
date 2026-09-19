# Unit 7 · Principles of Artificial Intelligence (AI) II

> A security risk assessment of an Electronic Health Record (EHR) system.

## Task / Assignment
Complete a **Security Risk Assessment Report** for a chosen system, following the standard structure:
executive summary → system overview → identified threats & vulnerabilities → recommendations → conclusion.

### Applied to an EHR system
- **What it is**: digitised patient medical records shared across hospital departments, insurers and even
  other hospitals — so a patient's record travels well beyond one clinic (wider sharing = larger attack surface).
- **Threats & vulnerabilities**
  1. **Excessive access** — many third-party interfaces (insurance, labs, external hospitals) add entry points.
  2. **Insider threats** — over-privileged staff may leak/sell records.
  3. **Data breaches** — e.g. Ireland's HSE attack (2021) exposed millions of patients and disrupted services for weeks.
  4. **Phishing** — staff tricked into revealing credentials.
- **Recommendations**: enforce **MFA** on every login; regular phishing-awareness training; **least-privilege**
  role definitions; encrypt data at rest **and** in transit; continuous maintenance.

## Associated source files
| File | Type | Notes |
|------|------|-------|
| `Unit7 Security Risk Assessment Report.docx` | Word | Full 5-section report on the EHR scenario |

## Core idea
Treat security as a **continuous task** — technology + training + clear policy together give the strongest defence.
