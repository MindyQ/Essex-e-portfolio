# Unit 9 · Computing and Risk

> How a cloud-reliant organisation identifies threats and builds a resilient disaster-recovery plan to keep its e-commerce services running.

## What risks does a cloud-based organisation face?

A hypothetical organisation relies heavily on cloud-based services. It faces several risks that could disrupt its cloud-based e-commerce operations. A cloud outage could make the storefront unavailable and cause significant revenue loss. Cyberattacks such as ransomware may cause data loss, unauthorised data exposure, or blocked customer access. Operational failures and service interruptions could result from human misconfiguration and network disruptions. Silent data corruption is also a serious risk because corrupted data may spread across systems before being detected.

## How does the disaster-recovery process work?

The disaster-recovery process begins with failure detection through CloudWatch, while PagerDuty immediately alerts the incident response team. The team then assesses the severity, affected systems and potential data loss before the Incident Commander declares a major incident and informs stakeholders. Next, affected systems are contained to prevent cyberattacks or corrupted data from spreading.

To minimise downtime, RDS Multi-AZ, Route 53 and ALB health checks support failover, while AWS Elastic Disaster Recovery can launch replicated workloads in a secondary region during a major outage. Critical data is then restored using RDS Point-in-Time Recovery (PITR), AWS Backup and Bacula, with separate backup copies providing protection against ransomware or corruption. S3 Cross-Region Replication provides additional regional resilience for stored objects, while Terraform can rebuild damaged infrastructure from code. Before services resume, checksums, database consistency checks and recent order reconciliation are used to verify data integrity.

## What are the legal, ethical and security responsibilities?

Disaster recovery involves more than technical availability. The organisation has a legal and ethical responsibility to protect customers' personal and payment information. Backup data should therefore be encrypted, access should follow the principle of least privilege, and recovery activities should maintain appropriate audit logs. Applicable privacy, cybersecurity and breach-notification requirements must also be followed.

## How should the organisation act professionally?

Professionally, employees should have clearly defined responsibilities so that important recovery tasks are not overlooked or duplicated. The organisation should communicate honestly with customers and other stakeholders when a serious incident affects them. Overall, an effective disaster-recovery plan (DRP) combines resilient technology, secure backups, clear accountability, regular testing and responsible data management to minimise downtime while protecting the organisation and its customers.
