# Programming Approaches, Pseudocode and Flowcharts

## Programming approaches

A **programming approach** is the **method or strategy used to design and structure a solution**. It describes **how you tackle the problem**, while a paradigm describes what style of constructs you use. The major approaches are:

- **Top-down (stepwise refinement)**: start with the **big picture** and progressively break it into smaller sub-problems. A student result system breaks into: read student data, calculate the average, determine the grade, print the result. It suits **planning new systems**.
- **Bottom-up**: start with **small reusable components** and combine them, for example build `calculateAverage()`, `assignGrade()` and `printResult()`, then combine them into `processResults()`. It suits **building reusable libraries**.
- **Structured programming**: uses only **sequence, selection and iteration**, **no goto statements**, and **one entry and one exit** per block.
- **Modular programming**: divides a program into **independent modules**, each with a **single responsibility**, which are reusable and easier to test and maintain.
- **Object-oriented approach**: models **objects and their relationships**, suited to real-world entities.

In practice programmers **combine approaches**: Java OOP often uses top-down design with bottom-up implementation of individual classes.

## Design before you code

Writing code immediately is like building a house without blueprints. The problem-solving process is: **understand the problem, write pseudocode, draw a flowchart, write the Java code, then test and debug**. Before coding, identify the **inputs**, the **conditions** (decisions), and the **outputs**.

## Pseudocode

**Pseudocode** is a structured but **informal, plain-English description** of an algorithm, mixed with programming constructs. It has no strict syntax and focuses on logic, not language rules. Common keywords are **BEGIN/END**, **INPUT**, **OUTPUT/PRINT**, **SET** (assign a value), **IF/THEN**, **ELSE** and **ENDIF**. Guidelines: use indentation to show structure, write one action per line, be specific but not language-bound, and capitalise keywords. For example:

```
BEGIN
  INPUT score
  IF score >= 40 THEN PRINT "PASS"
  ELSE PRINT "FAIL"
  ENDIF
END
```

Each line maps directly to one or two lines of Java. Always verify pseudocode with a few test values before coding.

## Flowcharts

A **flowchart** represents an algorithm with **standard shapes connected by arrows**:

- **Oval**: terminal (start or end);
- **Rectangle**: process (an action or computation);
- **Diamond**: decision (a yes/no question);
- **Parallelogram**: input or output;
- **Circle**: connector joining flow lines.

Flowcharts make logic easier to communicate to others.

Source: COS 201 Computer Programming I.pdf (Weeks 1-2) (Week 2, Topic C); cos201_weeks3to6.pdf (Week 5, Topic C)
