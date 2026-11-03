# Programming Paradigms

## Functional programming

**Functional programming (FP)** treats computation as the **evaluation of mathematical functions**, avoiding changing state and mutable data; it focuses on **what** to compute rather than how. Its principles:

- **Pure functions**: the same input always gives the same output, with **no side effects**. `square(4)` always returns 16; a method that does `count++` on an outside variable is **impure**.
- **Immutability**: data does not change after it is created.
- **First-class functions**, stored in variables and passed as arguments, and **higher-order functions**, which take or return other functions.
- **Recursion** replaces loops.

Java supports a functional style through **lambda expressions** (Java 8+), for example `numbers.stream().map(n -> n * n).forEach(System.out::println)`.

## Declarative programming

**Declarative programming** specifies **what** the program should accomplish without describing **how**, step by step; the system decides the execution strategy. **Imperative** programming gives explicit step-by-step instructions (for loops, if statements) with the programmer controlling the flow. Declarative examples are **SQL**, **HTML** and **Java Streams**: `numbers.stream().filter(n -> n % 2 == 0)` finds even numbers. **SQL is the most widely used declarative language**: four lines of `SELECT name, grade FROM students WHERE grade >= 50 ORDER BY grade DESC` replace a loop, a check, a sort and output code.

## Logic programming

**Logic programming** is based on **formal logic**. Programs are written as **facts** (statements that are unconditionally true), **rules** (statements true under certain conditions) and **queries** (questions asked of the knowledge base). **Unification** matches patterns to find solutions, and the system searches for answers with **backtracking**. The primary language is **Prolog**:

```
parent(tom, bob).  parent(bob, ann).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
?- grandparent(tom, ann).   % true
```

It is used in artificial intelligence, expert systems, natural language processing and theorem proving.

## Scripting languages

A **scripting language** is a high-level language for **automating tasks and rapid development**. Scripts are usually **interpreted**, **dynamically typed** (types are decided at runtime), concise and often embedded in browsers, servers or shells. Examples are **JavaScript** (web front end), **PHP** (web back end), **Python** (automation, AI), **Ruby**, **Bash**, **PowerShell** and **Perl**. By contrast **Java is compiled and statically typed**, suits large systems and needs more boilerplate: printing a list takes about ten lines of Java but three of Python.

The core takeaway: there is **no single best paradigm**. Functional thinks in transformations, declarative in outcomes, imperative in steps.

Source: COS 201 Computer Programming I.pdf (Weeks 1-2) (Week 1, Topics C and D; Week 2, Topics A and B)
