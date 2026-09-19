# Unit 2 · Logical Foundations of Computing: Boolean Algebra, Gates, and Set Theory

Boolean logic is a binary algebraic system that categorizes all logical propositions into two states: true (represented by 1) and false (represented by 0), which is the core mathematical foundation of all digital computing systems (Tanenbaum et al., 2013). This binary framework has been widely used across various areas of modern computing and plays an important role in optimizing workflows and increasing efficiency. Here, I will discuss its applications in search engines and enterprise access control, as well as some of its limitations.
One of the most important applications of Boolean logic is helping search engines improve search accuracy according to user keywords. Constrained query expressions using Boolean logic filter eligible resources in advance, cutting unnecessary inspection and lowering resource consumption dramatically (Wang et al., 2026, p.3). Before Boolean logic was integrated into search engines, systems had to process only one condition at a time and filter results step by step to narrow the search scope, which was inefficient and error-prone. Modern search engines allow users to construct optimized queries with Boolean operators AND/OR/NOT and can process complex multi-condition queries in one go. For example, when shopping online for pet supplies, using the query "dog AND collar AND black " can quickly find products that meet customers' needs. Boolean logic simplifies the original multi-step manual filtering into a one-step system operation.
Another core application of Boolean logic in enterprise work is assigning permissions. For example, in the company, only users who meet the two conditions belong to the finance department AND have a staff level above 3 are allowed to access confidential financial documents. This automatic Boolean judgment helps enterprises protect sensitive data, avoid unauthorized internal access, and reduce the risk of confidential information leakage.
However, Boolean logic still has obvious limitations: it is completely based on a binary "either true or false" judgment logic and has inherent flaws when dealing with uncertain intermediate states. For example, when a user searches for affordable AND comfortable running shoes on an e-commerce platform, the concepts of "affordable" and "comfortable" are inherently ambiguous: a price of £80 is affordable for some users but too expensive for others. Pure Boolean logic can only force these vague concepts into binary categories, which often mismatch user needs and reduce search accuracy ( (Salton, Fox and Wu, 1983).

Reference:
Salton, G., Fox, E.A. & Wu, H. (1983) 'Extended Boolean Information Retrieval', Communications of the ACM, 26(11), pp. 10221036. DOI: 10.1145/182.358466

Tanenbaum, A.S. et al. (2013) Structured Computer Organization. Sixth international edition. Boston: Pearson.

Wang, S. et al. (2026) Search, Inspect, Fetch: Exploiting Boolean Retrieval for DeepResearch Agents. arXiv preprint arXiv:2608.02751. Available at: https://arxiv.org/pdf/2608.02751 (Accessed: 11 August 2026)




This is an alarm system. It consists of 3 inputs (A, B, C) and 1 output (O). If 2 or more inputs are 1, then output = 1. Alarm will be triggered. If 1 or 0 input is 1, then output = 0. 
**Truth table:**
| **Input A** | **Input B** | **Input C** | **Output O** |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |


**The****diagram of the****alarm system****circui****t:**




This 3-input alarm system circuit uses core Boolean algebra laws to implement a control mechanism. The truth table contains four product terms that can make O=1: O=BC+AC+AB+ABC. 
Simplify using Boolean algebra rules, A+A=A（idempotent law）and X+=1（complement law）:
O=O+O=BC+AC+AB+ABC+BC+AC+AB+ABC
  =AB(C+) + BC（+A）+AC(B+)   
  =AB+BC+AC
From the calculation above, Boolean logic simplifies the complexity of the original product terms involving 3 inputs. We deduced O=AB+BC+AC from it. It means any of AB or, BC or AC is 1, then we have O=1. In the alarm system circuit, we only need to build three two-input AND gates for AB, BC, and AC. A single three-input OR gate O is used to connect the three AND outputs, allowing every instance where at least two gates are 1 to make the single three-input OR gate become 1. In contrast, if 0 or only 1 gate is 1, the output remains 0. In practical applications, this circuit can be used for a security system or for detecting situations. When two key factors are detected, an alarm will be triggered immediately. For example, when entering a password, if both the IP address and the password are incorrect, the system will immediately send a message to the user to alert them. In this logic circuit, Boolean logic simplified the mechanism design greatly, meanwhile, the circuit speed is improved
