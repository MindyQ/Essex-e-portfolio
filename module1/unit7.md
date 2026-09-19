# Unit 7 · Principles of Artificial Intelligence (AI) II

> Security risk assessment of an Electronic Health Record (EHR) system.

## Executive summary
An electronic health record (EHR) system stores patients' medical information in digital form. It saves repetitive health-checking work and, with comprehensive information, raises diagnosis accuracy. However, it also carries key threats: data breaches, unauthorised access, and misuse. This report discusses the system's structure, its key threats, and practical steps to reduce those risks.

## System overview
The EHR records a patient's health data at every hospital visit. Medical workers enter examination results and diagnoses into it; the data is shared across hospital departments and even between city hospitals, and insurance institutes use it to verify reimbursement claims. A patient's record therefore travels far beyond one clinic — and the wider the sharing, the larger the attack surface.

## Identified threats & vulnerabilities
- **Excessive access.** The EHR connects to many third-party interfaces (insurers, labs, external institutions); each adds a new entry point for attackers.
- **Insider threats.** Staff with too much access may leak or sell patient details (e.g. to pharmaceutical companies).
- **Data breaches.** In 2021, Ireland's Health Service Executive (HSE) was hacked; millions of patient records were exposed and hospital services disrupted for weeks.
- **Phishing.** Staff may reveal credentials through deceptive emails, giving attackers a legitimate-looking doorway in.

## Recommendations
Enforce **multi-factor authentication (MFA)** on every login; train staff to recognise phishing and understand their legal duties; apply the **principle of least privilege** with precise user roles; encrypt data at rest and in transit; and keep systems patched. Technology, training, and clear policy together give the strongest protection.

## Conclusion
The EHR improves efficiency and accuracy but brings real security risk. The main dangers are excessive access, insider misuse, data breaches, and phishing — so hospitals must treat security as a continuous task, with strong authentication, clear access rules, and staff training.
