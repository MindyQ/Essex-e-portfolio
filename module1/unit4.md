# Unit 4 · Software Engineering

> Agile and DevOps — two dominant methodologies, their strengths, limits, and the projects they fit best.

## Agile
Agile builds software in small increments called "sprints" and continuously gathers feedback from users and stakeholders. Its strength lies at the *requirements* layer: a backlog lets new requirements from customers, developers, or others be added at any time, with priorities re-ranked every sprint. Agile follows a "**fail fast**" philosophy — risks are broken into small pieces and moved forward, so the team discovers mistakes at the lowest cost.

Limitation: Agile suits small and medium projects because practices like stand-ups, communication, and retrospectives stay light only in small teams. As the project grows, that complexity rises quadratically and Agile can turn chaotic. It also says little about delivery.

## DevOps
DevOps connects development and operations through an automated pipeline of continuous integration, automated testing, and automated deployment. Its strength lies at the *delivery* layer: the pipeline replaces repetitive manual checking, so releases are fast and stable. DevOps follows a "**fail safely**" philosophy — small frequent commits, automatic rollback to the last healthy version, and real-time monitoring make anomalies visible immediately, so even when something breaks users are barely affected and recovery takes minutes.

Limitation: DevOps is not fully automatic. Humans must still review monitoring feedback, decide fix-vs-rollback, and give final approval, so its speed depends on timely human response. The upfront investment in tooling and test systems also feels heavy for small projects.

## Which to choose?
- A startup with uncertain requirements → **Agile** (fast feedback matters more than delivery scale).
- A large system with thousands of microservices and daily deployments (e.g. Netflix) → **DevOps** (such a system cannot run without automation).
- An established company such as Spotify or Facebook → **both together**: Agile manages changing requirements, DevOps lands each change quickly and safely.

In short, Agile answers "what to build"; DevOps answers "how to deliver it".
