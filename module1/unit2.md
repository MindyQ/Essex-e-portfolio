# Unit 2 · Logical Foundations of Computing: Boolean Algebra, Gates, and Set Theory

> Binary logic, real-world applications, and a hands-on logic-circuit build.

## Task A — Reflective report (≈400 words)
Explain how **Boolean logic** underpins modern computing, with two real-world applications and academic
references. The work covers:

- **Search engines** — `AND / OR / NOT` collapse multi-step filtering into a single query
  (e.g. `"dog AND collar AND black"`).
- **Enterprise access control** — `department = Finance AND level > 3` gates confidential data.
- **Limitations** — strictly true/false cannot express fuzzy / graded concepts
  ("affordable", "comfortable") or probabilistic events (a 0.93 model confidence is not simply "cat / not cat").

## Task B — Logic circuit design
Design and simulate a **3-input majority / alarm system**: output `O = 1` when **≥ 2 of A, B, C are 1**.

Truth table (excerpt) and Boolean simplification:

```
O = BC + AC + AB + ABC
  = AB(C+C') + BC(A+A') + AC(B+B')     # idempotent + complement laws
  = AB + BC + AC
```

So only **three 2-input AND gates** feed a single **3-input OR gate**. Practical use: trigger an alert
when two key signals are both present (e.g. wrong password **and** wrong IP).

## Associated source files
| File | Type | Notes |
|------|------|-------|
| `Unit2 task .docx` | Word | Task brief + Boolean-logic report + circuit derivation |
| `unit2 case study.docx` | Word | Extended Boolean essay (search engines, access control) with references (Tanenbaum 2013; Salton, Fox & Wu 1983; Wang et al. 2026) + same alarm-circuit truth table |

## Skills developed
Problem-solving, logical reasoning, hands-on work with circuit simulators.
