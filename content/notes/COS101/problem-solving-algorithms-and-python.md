# Problem Solving: Algorithms, Flowcharts and Python

## The software development method

**Problem solving** turns a problem description into a solution using knowledge of the domain and suitable strategies and tools. The **software development method** has six steps:

1. **Specification of needs**: what the problem is and what the solution must provide.
2. **Problem analysis**: inputs, outputs, constraints and formulas. Converting miles to kilometres has input miles, output kilometres and the formula 1 mile = 1.609 km.
3. **Design and algorithmic representation.**
4. **Implementation**: write the program in a language such as Python.
5. **Testing and verification**: testing runs the program to show it is correct; verification checks it meets the requirements.
6. **Documentation**, including comments.

## Algorithms

An **algorithm** is a **finite sequence of steps in a specific logical order** that solves a problem. It must have **input and output**, be **unambiguous**, **general**, **correct**, **terminate in finite time** and be **efficient**. Written in a programming language, it becomes a **program**. It is represented as **pseudocode**, a semiformal English-like language, or as a **flowchart**, a graphical form.

Flowchart symbols:

- **terminal** (oval) for start and stop;
- **process** (rectangle);
- **input/output** (parallelogram);
- **selection/decision** (**diamond**, two-way);
- connectors and **flow lines**.

**Example**: input four marks M1 to M4, set GRADE ← (M1 + M2 + M3 + M4)/4, then if GRADE < 50 print "FAIL", else print "PASS" (ENDIF closes the IF block).

**Böhm and Jacopini (1966)** showed that any algorithm needs only three **control structures**:

- **sequence**: steps run in order;
- **selection**: IF ... THEN ... ELSE;
- **repetition (iteration)**: WHILE condition ... END_WHILE repeats while the condition holds.

## Python basics

In Python:

- A **variable** is assigned with =.
- Arithmetic operators are + − * / and ** (power). **Relational** operators are < > <= >= == !=, and **logical** operators are and, or, not.
- ** is evaluated before * and /, which come before + and −.
- not binds before and, which binds before or, so True or True and False is True.
- '2' + '3' joins strings to give '23'.
- Using a variable before it is assigned is an error.
- input() reads text, so float(input(...)) converts it to a number.
- Blocks are marked by **indentation** after a colon: if, elif, else and while lines end with ":". A missing colon or indentation is a syntax error.
- In an if ... elif chain, only the **first true branch** runs.
- A counter such as i = i + 1 (or i += 1) controls a while loop.
- Python 3 writes print("hi"); older Python 2 wrote print "hi".

Source: CSC 101 compiled by SISTER IZA.pdf (the CSC 101 slides compiled by a student) (problem solving slides); COS 101 / CSC 101 past questions; General knowledge of COS 101 for the Python details, which the folder's slides do not cover
