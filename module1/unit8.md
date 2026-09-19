# Unit 8 · Principles of Cyber Security

> A phishing case study — threat analysis, mitigation, and the ethics of security.

## Scenario
At a trading company, employees received a phishing email titled "Your 2026 Salary Increase: Confirm Payroll Before Friday". The sender showed "HR Department" but came from an external mailbox. It urged staff to click a link and verify bank and identity details within 48 hours, warning that failure would forfeit the raise.

## Threat analysis
This is a typical phishing attack: the email lures employees into sharing sensitive information, and a virus in the link could give attackers access to the internal network, risking data leakage. It shows that firewalls and email filters alone cannot fully protect an organisation's cybersecurity.

## Mitigation
- **Training** — teach staff never to click suspicious links and to check the true sender address.
- **Data protection** — separate sensitive databases from public ones and limit who can access them (least privilege).
- **Multi-factor authentication** — a stolen password alone is no longer enough for a successful attack.
- **Network segmentation** — firewalls should separate the customer database from general office traffic.
- **Compliance** — follow lawful data-handling policies, notify the regulator of a serious breach within 72 hours, and adopt **ISO/IEC 27001** to meet an international benchmark.

## Ethical considerations
- **User privacy** — companies must be transparent about data collection and give users control over their information.
- **Duty of care** — employee bank and identity data deserve the same rigour as client records; a breach harms workers directly.
- **Just culture** — blame-free post-incident review fixes the process, not the person, building stronger security than punishment.
- **Simulation ethics** — fake-phishing drills exploit trust and financial pressure, so informed consent or a clear debrief should accompany any test.
