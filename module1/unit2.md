# Unit 2 · Logical Foundations of Computing: Boolean Algebra, Gates, and Set Theory

> How Boolean logic powers search engines and access control — and where binary thinking falls short.

## Boolean logic in search engines
Boolean logic lets a search engine process complex multi-condition queries in a single step. With operators AND / OR / NOT, a query such as "dog AND collar AND black" returns only the pages that satisfy every condition, instead of filtering one condition at a time. Constrained Boolean query expressions pre-filter eligible resources, cutting unnecessary inspection and lowering resource consumption (Wang et al., 2026).

## Boolean logic in enterprise access control
The same binary framework assigns permissions automatically. For example, only users who satisfy "belong to the finance department AND have a staff level above 3" may open confidential financial documents. This automatic judgement protects sensitive data, avoids unauthorised internal access, and reduces the risk of leaks.

## Limitations of binary logic
Boolean logic is built on an absolute true/false split, so it struggles with vague or graded concepts. A price of £80 is "affordable" for one shopper but "expensive" for another; pure Boolean logic forces such fuzzy ideas into two rigid categories, which often mismatches real user needs and lowers search accuracy (Salton, Fox and Wu, 1983). It also cannot represent uncertainty or probability — "it will rain tomorrow" is not a clean true/false, and an AI image classifier outputs a 0.93 confidence rather than a hard yes/no.

## Logic-circuit design: a 3-input alarm (majority voting)
The alarm has three inputs (A, B, C) and one output (O). The output triggers when **two or more** inputs are 1.

| A | B | C | O |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

The truth table yields four product terms for O = 1: O = BC + AC + AB + ABC. Applying the idempotent law (A + A = A) and complement law (X + X' = 1), this simplifies to **O = AB + BC + AC**. In the circuit we therefore need only three two-input AND gates (for AB, BC, AC) feeding a single three-input OR gate. Whenever at least two inputs are 1, the OR gate outputs 1 and the alarm triggers — e.g. when both the IP address and the password are wrong, the system immediately alerts the user.

## Reference
- Salton, G., Fox, E.A. & Wu, H. (1983) 'Extended Boolean Information Retrieval', *Communications of the ACM*, 26(11), pp. 1022–1036. DOI: 10.1145/182.358466
- Tanenbaum, A.S. et al. (2013) *Structured Computer Organization*. 6th edn. Boston: Pearson.
- Wang, S. et al. (2026) *Search, Inspect, Fetch: Exploiting Boolean Retrieval for DeepResearch Agents*. arXiv:2608.02751. Available at: https://arxiv.org/pdf/2608.02751 (Accessed: 11 August 2026)
