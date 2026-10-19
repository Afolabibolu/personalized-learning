# Expert Systems

## What the topic is

An expert system is a computer system that emulates the decision-making ability of a human expert. It uses a knowledge base of facts and rules and applies logical reasoning to reach conclusions, in a specific, well-defined area that human experts have already solved successfully. Expert systems are among the most successful AI-related technologies.

## Subtopics

**Architecture.**
- **Knowledge base:** domain facts and rules.
- **Inference engine:** applies logic to the knowledge base.
- **User interface:** communicates with the user.
- **Explanation facility:** justifies the reasoning.
- **Knowledge acquisition module:** adds new knowledge.

Working memory holds the current facts, and an agenda orders the rules waiting to fire.

**How the inference engine works.** Forward chaining starts with known facts and applies rules to derive conclusions (data-driven). Backward chaining starts with a goal and works backward to find supporting facts (goal-driven). The engine matches patterns, triggers rules and keeps applying them until it reaches a conclusion.

**A forward-chaining example.** Facts: has_wings, lays_eggs. Rules: IF has_wings AND lays_eggs THEN is_a_bird; IF is_a_bird AND swims THEN is_a_duck. The first rule fires and adds is_a_bird. The second fires only if swims is also a fact.

**MYCIN case study.** Developed at Stanford in the 1970s, MYCIN diagnosed bacterial infections and recommended antibiotics, using over 600 rules. It performed comparably to human physicians in tests but was not deployed because of legal and ethical concerns.

**Expert systems and human experts.** Expert systems are rule-based, consistent, scalable and unemotional. Human experts draw on experience, can be inconsistent, tire, and can adapt intuitively. Expert systems work best in well-structured domains with clear rules.

**When to use one.** One expert cannot cover every dimension of the problem; the knowledge can be written as rules or heuristics; the task has been solved by experts before; consistency is needed; the domain is limited; there are many rules; or experts are scarce.

**When not to.** Very few or too many rules, well-structured numerical problems, areas too wide and shallow, disagreement among experts, or problems humans solve better.

**Advantages.** Never distracted, forgetful or tired; preserves the expertise of scarce or departing experts; consistent decisions; helps non-experts decide better.

**Case-based reasoning.** CBR matches a new case to solved cases in a database. With no exact match it asks the user for more information; if there is still no match, a human expert must solve it.

## Key terms

- **Inference engine:** the reasoning component that applies rules to facts.
- **Explanation facility:** shows how and why a conclusion was reached.

## Exam-style point

Past papers show the expert-system schematic and ask how each element fits a proposed system. For each element, say what it holds or does in that domain. For a medical-care system, the knowledge base holds diagnosis rules and the explanation facility tells the doctor why a drug was suggested.

Source: Lecture 4; Intelligent Systems-4.pdf
