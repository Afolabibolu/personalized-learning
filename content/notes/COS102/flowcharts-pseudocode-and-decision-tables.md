# Flowcharts, Pseudocode, Decision Tables and Decision Trees

A solution is designed before it is coded. Four common tools express the design.

## Pseudocode

**Pseudocode** is a language designed to express algorithms. It is not a real computer language and has no special grammar rules, but it must express these concepts:

- **Variables:** names for places in memory where values are stored, such as sum or counter.
- **Assignment:** storing a value, written `Set sum to 0` or `sum <— 0`.
- **Input/output:** `Read num` for input; `Write "Enter a number"` or `Write sum` for output. Get, Input, Display and Print are equivalent words.
- **Selection:** `IF (condition)` with an optional `ELSE`. The if-then version runs or skips an action; the if-then-else version chooses between two actions.
- **Repetition:** `WHILE (condition)` repeats the indented statements while the condition is true.

Conditions are **Boolean expressions**, which evaluate to true or false. Indentation groups statements, and `//` starts a comment. Be consistent within a project.

```
Set counter to 0
Set sum to 0
Read limit
WHILE (counter < limit)
    Read num
    Set sum to sum + num
    Set counter to counter + 1
Write sum
```

**Following (tracing) an algorithm** means drawing a box for each variable and updating the values step by step, to check that the algorithm works before it is coded.

## Flowcharts

A **flowchart** shows an algorithm as standard symbols joined by arrows (flowlines) that show the order of steps:

- Oval (terminal): Start and Stop
- Parallelogram: input or output
- Rectangle: a process, such as a calculation or assignment
- Diamond: a decision, with one exit for Yes and one for No
- Small circle: a connector to another part of the chart

## Decision tables

A **decision table** lists the **conditions** and the **actions**, and each column (a **rule**) gives one combination of condition values and the actions to take. With n yes/no conditions there are 2ⁿ possible rules. Tables check that every combination is handled.

## Decision trees

A **decision tree** shows the same logic as branches. Each internal node tests a condition, each branch is an outcome, and each leaf is an action. It is easier to read than a table when conditions are tested in sequence.

Source: Computer Science Illuminated, 7th edition (2020), Chapter 6.5 (pseudocode); flowcharts, decision tables and decision trees from general knowledge, following the NUC CCMAS outline for COS 102
