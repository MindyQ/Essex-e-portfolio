# Unit 4 · Software Engineering

> Two dominant methodologies — where each fits, and why they often work best together.

## Task / Assignment
Analyse the strengths, limitations and best-fit project scenarios of **Agile** and **DevOps**.

### Agile
- Builds software in small increments ("sprints"); continuous feedback from users/stakeholders.
- Strength sits at the **requirements layer** — a backlog lets new requirements land any time, priorities
  re-ranked each sprint.
- Philosophy: **"fail fast"** — break risk into small pieces, surface mistakes cheaply.
- Limitation: shines for **small/medium** projects; practices get quadratically heavier as the project grows,
  and it says little about *delivery*.

### DevOps
- An automated pipeline of CI → automated testing → automated deployment; **"fail safely"**.
- Strength sits at the **delivery layer** — frequent small commits, automatic rollback to last healthy
  version, real-time monitoring.
- Limitation: not fully automatic (humans still review/approve); upfront tooling investment feels heavy for
  small projects.

### Best-fit summary
- **Agile** → startup with uncertain requirements (feedback > scale).
- **DevOps** → large system with thousands of microservices / daily deploys (e.g. Netflix).
- **Both together** → established companies (Spotify, Facebook): Agile plans, DevOps delivers.
- Agile answers *what to build*; DevOps answers *how to deliver it*.

## Associated source files
| File | Type | Notes |
|------|------|-------|
| `Unit4 software development methodologies.docx` | Word | Full comparative essay with examples (Spotify, Facebook, Netflix) |

## Core idea
Pick by **project scale** and **requirement volatility** — and combine the two whenever possible.
