# Pseudocode, Flowcharts and Control Structures

## Control structures

Any classical algorithm can be expressed with three constructs, as **Böhm and Jacopini** showed in **1966**:

- **Sequence**: steps run in order, with control passing unconditionally.
- **Selection**: a condition decides which of two actions runs, as in "if A > B print A, else print B".
- **Iteration**: steps repeat while a condition holds.

**Example (iteration)**: fill the kettle; plug it in; **while** the water has not boiled, wait 60 seconds; turn the kettle off; unplug it.

## Pseudocode

**Pseudocode** ("false code") is an informal, high-level description that uses programming structure in plain English. It is written for humans before programming. Its vocabulary includes **READ** (input a value into a variable), **COMPUTE** and **DISPLAY** (output), and a **variable** is a storage placeholder.

```
READ Length, Breadth
COMPUTE Area AS Length * Breadth
DISPLAY Area
```

Selection forms:

- **if**: IF (score >= 45) THEN DISPLAY "Passed" ENDIF. The action runs only if the condition is true.
- **if...else**: adds ELSE DISPLAY "Failed".
- **if ladder** (multiple selection): IF score >= 70 → grade point 4, ELSE IF >= 60 → 3, ELSE IF >= 50 → 2, ELSE IF >= 45 → 1, ELSE 0.

Iteration uses **while** (repeat while a condition is true) and **for**, which has an initialisation, a condition and an increment. Statements can be **nested**.

Other examples: salary = hours × rate, with an error message if either is negative; an integer is even if dividing by 2 leaves no remainder.

## Flowcharts

A **flowchart** is a **graphical representation of an algorithm**. It shows the structure, logic and sequence of operations using standard symbols, each a unique shape. It is independent of any programming language and useful for documentation and for communication between programmers and non-programmers. The symbols:

- **terminal** (start/stop);
- **process** (rectangle);
- **input/output** (parallelogram);
- **decision** (diamond, with Yes and No exits);
- **flow lines**;
- **connector**, joining parts of one flowchart;
- **off-page connector**, continuing to another page.

**Example**: START → input M1, M2, M3, M4 → GRADE ← (M1 + M2 + M3 + M4)/4 → is GRADE < 50? Yes: print "Fail"; No: print "Pass" → STOP.

Source: COS 102 Lecture 7 (algorithms and heuristics); CSC 102 Lecture 5 2024 (flowchart, introduction to programming); COS 102 / CSC 102 practice sheets
