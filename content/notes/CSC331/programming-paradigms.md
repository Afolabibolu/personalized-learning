# Programming Paradigms

## What a paradigm is

A **programming paradigm** is a fundamental programming style, which in turn gives differently structured code.

- **Imperative** programming states **which steps** the program completes and in what order (the "how"), like a recipe.
- **Declarative** programming describes only **what** the result should be, like a photo of the finished meal.

Its sub-types are **functional** and **logic** programming.

## Imperative styles

- **Structured:** replaces jump (GOTO) commands with control structures (sequence, selection, iteration) and breaks a program into **modules**. Each module has a name, does one task, has one entry and one exit point, and calls only modules below it.
- **Procedural (POP):** divides algorithms into sub-programs, routines or functions, as in COBOL, FORTRAN and C. Data is often **global**, so any function can change it and bugs spread. It emphasises algorithms over data, works top-down, and models real-world problems poorly.
- **Modular:** a procedural style for large projects; independent modules are tested separately and then linked.
- **Object-oriented (OOP):** a program is a collection of interacting **objects**, each wrapping its data with methods, receiving and sending messages. Implementation details are hidden, and objects inherit from more general ones. Pure OO languages include Smalltalk, Scala and Eiffel; mainly-OO languages with procedural parts include C++, Java, C# and Python.

## Imperative languages

Imperative languages follow the **von Neumann architecture**, in which program and data share memory. Their principal operation is **assignment**, so computing is done by side effects. A language is **Turing complete** if it has integer variables, values, operations, assignment, sequencing, conditionals and branching. Imperative code is easy to learn and read, but grows long for complex problems.

## Functional programming

A functional program is a string of function calls. Functions are **first-class objects**: they can be stored, passed as parameters and returned. There is **no assignment statement**; recursion replaces loops, and values pass through parameters and return values. Pure functional languages, such as Scheme, have **no side effects**.

| Advantages | Disadvantages |
| --- | --- |
| Stateless programs | Data cannot be changed |
| Well suited to parallelisation | Poor for retrieving large amounts of data |
| Easily testable, shorter code | Not suitable for every task |

## The lambda calculus

Functional languages derive from the **lambda calculus** of **Alonzo Church and Stephen Kleene** (1930s). In it, a function maps a domain to a codomain: **λx.x³** is the function bound to cube. A Turing machine and the lambda calculus have been proven **equivalent in power**, so functional and imperative languages compute exactly the same things.

Source: CSC 331 Programming Principles and Paradigms.pdf (course book), Study Session 3 (meaning of paradigms, structured, procedural, modular and object-oriented programming) and Study Session 8 (imperative languages, functional programming, lambda calculus)
