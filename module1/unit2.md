# Unit 2 · Logical Foundations of Computing: Boolean Algebra, Gates, and Set Theory

Complete both tasks.
**Task A: (Logic, Gates and SET Theory)**
How is Boolean logic applied in modern computing systems? Provide real-world examples. **Research and explain** the role of Boolean logic in modern computing, **including its applications in search engines, programming, and circuit design.**
Identify two real-world applications (e.g., how Google uses Boolean logic in search queries or how CPUs process logic operations).
Write a 400-word reflective report, ensuring you provide academic references to support your arguments.
1.先引用文献解释布尔逻辑是什么？ 
布尔逻辑被广泛地运用到很多领域。在这里我将会讨论一下布尔逻辑在搜索殷勤里的运用，以及它的一些局限性。
布尔逻辑的一个重要运用便是帮助系统根据用户的关键词提高搜索的准确率。在不运用布尔逻辑的情况下， 我们需要处理单次单个条件，并编写算法一个条件一个条件地筛查来缩小搜索范围。搜索引擎运用布尔逻辑`AND/OR/NOT`优化后的关键词，能够一次性处理包含复杂条件的查询。比如：在线上购物时，我们可以用“狗狗and项圈and黑色” 迅速找到理想产品。布尔逻辑把多步操作简化为一步实现。
布尔逻辑在工作种的另一个重要应用，即是通过制定规则来确定不同员工的权限，比如在公司网站种，只有财务部AND员工级别是3以上的才能允许访问财务报表。帮助公司保护敏感数据，避免内部越权访问，降低机密信息暴露的风险。 
  但是布尔逻辑也存在一定的局限性。它往往基于非真即假的逻辑来进行判断。对中间状态的处理存在一定的漏洞。比如：。。。。。
  布尔逻辑能处理真或者假的情况，但是却**无法描述模糊 / 程度类概念**只有绝对真 / 假，不存在中间状态。例：27℃ 到底算 "暖和" 还是 "热"？二值逻辑只能强行一刀切，不符合人对 "高矮、冷热、好看" 这类渐变概念的真实认知 

**无法处理不确定性与概率事件，****只能处理确定的 True/False，面对未知、随机事件无能为力。例："明天会下雨" 无法用布尔判定；AI 图像识别输出的是 0.93 的置信度，不能粗暴归为 "是猫 / 不是猫"**


Boolean logic is widely applied in various fields. Here, I will discuss its application in search engines and some of its limitations.
Using Boolean logic in search engines helps the system improve the accuracy of searches based on users’ keywords. Without Boolean logic, we would need to handle individual conditions separately and write algorithms to screen them one by one to narrow down the search results. Boolean logic allows search engines to process content that includes complex conditions all at once. AND can be used to search for web pages containing two or more keywords. OR can find web pages that list any of the conditions, and NOT can be used to filter out web pages that do not contain a particular condition. Boolean logic simplifies multiple steps into a single implementation.
Parentheses can group expressions to control calculation priority.
Each webpage is judged as logical 1 (matched) or logical 0 (unmatched).
**Task B: Logic Circuit Design: Practical Implementation of Boolean Algebra**
Design a logic circuit that performs a basic control function, such as a 3-input majority voting system or a simple alarm system. Use a logic circuit simulator (e.g., Logisim or Digital Works) to implement the circuit. Create a truth table for the logic circuit, showing all possible input-output combinations.
Create a diagram of the circuit, the truth table, and a 200-word explanation describing the circuit’s functionality and how Boolean logic was applied.
**Skills Developed**
Problem-solving and logical reasoning.
Hands-on technical skills with circuit simulators.











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
From the calculation above, Boolean logic simplifies the complexity of the original product terms involving 3 inputs. We deduced O=AB+BC+AC from it. It means any of AB or, BC or AC is 1, then we have O=1. In the alarm system circuit, we only need to build three two-input AND gates for AB, BC, and AC. A single three-input OR gate O is used to connect the three AND outputs, allowing every instance where at least two gates are 1 to make the single three-input OR gate become 1. In contrast, if 0 or only 1 gate is 1, the output remains 0. In practical applications, this circuit can be used for a security system or for detecting situations. When two key factors are detected, an alarm will be triggered immediately. For example, when entering a password, if both the IP address and the password are incorrect, the system will immediately send a message to the user to alert them. In this logic circuit, Boolean logic simplified the mechanism design greatly, meanwhile, the circuit speed is improved.











你对于AI个性化推荐为用户体验和商业运营带来了极大的收益的观点非常深刻。 同时你也批判性地分析了AI算法限制了用户的多元化视角以及 AI可以低成本快速生成高度逼真的虚假内容带来的危害。这些观点跟我对于AI对以Instagram为代表的社交媒体平台的观察和想法高度契合。在这里，我也想要你对于AI在社交媒体上的运用积极影响和局限性进行一些扩充讨论。 
值得注意的是，AI的运用大大的丰富了社交平台的内容，降低社交媒体创作者的创作成本，使得内容创作者在不需要团队和或者实物的情况下，也能将自己的创意和想法付诸实践。 然而AI创作内容也具有一定的局限性。在可利用的资源里创造出的模型往往是过于典型化而缺乏个性化，以AI生产的人物 画像为例，创造出一个医生的形象往往是白大褂方脸戴眼镜... 这往往能够引起审美疲劳。 AI有运用已有数据进行创作的能力，但是却缺乏创新的能力，这是AI在社交媒体上创作内容的一大局限。

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
