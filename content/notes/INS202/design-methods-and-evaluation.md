# System Design Methods and Human-Centred Evaluation

## System design methods

A **system design method** is a **structured approach to planning, organising and controlling how software gets built**. The choice affects how fast problems surface, how well the interface fits users and how costly change becomes.

- **Waterfall**: a **sequential** method in which each phase (requirements, design, implementation, testing, deployment, maintenance) is completed **once, in order**. It suits stable, well-understood requirements, but **user problems surface late**, when change is expensive.
- **Spiral** (Boehm, 1988): a **risk-driven, iterative** method that combines Waterfall's phases with **repeated cycles of prototyping and risk analysis**, each loop preceded by a risk assessment. It suits **large, complex or high-risk** projects such as ERP rollouts, but needs costly risk-analysis expertise.
- **Agile**: an iterative, values-based approach from the **Agile Manifesto (Beck et al., 2001)**, which values individuals and interactions, working software, **customer collaboration** and **responding to change**. Frequent delivery **reduces the risk of building the wrong product**.
- **Scrum**: Agile in fixed **sprints of 1 to 4 weeks**, with defined roles (the **Product Owner**, who manages the product **backlog**, the **Scrum Master**, who facilitates, and the development team), artefacts and ceremonies.

## Why evaluate?

What a designer builds is at first **only a hypothesis**; **evaluation tests it against real people**. User feedback is indispensable.

- **Formative** evaluation happens **during design** to shape the product, with small groups repeated across iterations.
- **Summative** evaluation happens **after a design is essentially complete**, summing up overall quality against a competitor, an earlier version or a benchmark.

Methods are also **qualitative** (why users struggle) or **quantitative** (how many, how fast).

## Ten methods

1. **Usability testing**: real users perform tasks while observers measure success, time and errors. **Testing with just 5 users uncovers about 85% of usability problems** (Nielsen, 2000), so several small rounds beat one large one.
2. **A/B testing**: two versions are shown to different users to see which performs better.
3. **Heuristic evaluation**: experts check the interface against principles such as Nielsen's heuristics.
4. **Cognitive walkthrough**: experts step through tasks as a new user would.
5. **Questionnaires**, such as the **System Usability Scale (SUS)**.
6. **Interviews**, 7. **observation**, 8. **analytics**, 9. **eye tracking** and 10. **think-aloud**, where users speak their thoughts as they work.

## Scoring the SUS

The SUS has **ten items rated from 1 (strongly disagree) to 5 (strongly agree)**. For **odd (positive) items, subtract 1** from the score; for **even (negative) items, subtract the score from 5**. **Sum the ten adjusted scores (0 to 40) and multiply by 2.5** to get a score out of 100. About **68 is average**; bands are below 51 poor, 51 to 70 marginal, 71 to 85 good and above 85 excellent. Results go into an evidence-based **usability report**.

Source: INS 202 Lecture 7 System Design Methods; INS 202 Lecture 8 Human-Centred Evaluation
