# Control Structures, Scope and Binding

## Control structures

**Control statements** set the order in which a program's statements execute; they are the basic building blocks of programs. The four kinds of control flow are:

- **sequencing:** statements run one after another;
- **selection:** if and switch choose between paths;
- **iteration:** loops repeat statements;
- **recursion:** a function calls itself.

**for and while loops.** A for loop has three parts: initialise the counting variable, test the condition for repeating, and increment the variable after each repetition. Its grammar is `for (Assignment1opt ; Expopt ; Assignment2opt) statement`. Both for and while test the condition **before** each iteration, so the body may never run.

**do statement.** `do statement while (expression);` tests **after** each iteration, so the body runs **at least once**.

**switch statement.** `switch (expression) { cases }` chooses among cases. Each case head is the keyword case, a literal and a colon, and an optional default case comes last. Unlike if, whose test can be any Boolean expression, switch compares for equality with literals.

**break** ends the current case of a switch, or exits a loop. **continue** ends the current iteration and goes straight to the loop test.

## Scope and visibility

The **scope** of a declaration is the collection of statements that can access the variable. C-like languages (C, C++, Java, C#) and Pascal-like languages (ADA) use **static scoping**: references are resolved from the program text alone, without regard to its execution history.

- A **global** variable's scope is every statement in the program.
- A **local** variable's scope is only the function or method where it is declared.

Scopes are therefore **disjoint or nested**, so the same name can be reused in different functions. When an inner scope re-declares a name, the new declaration **hides** the outer one. A name is **visible** where it is in scope and not hidden. Pascal, Modula and ADA allow **nested functions**, while C and Java do not. In Java and C++ the scope of a for-loop variable is limited to the for statement.

## Names, bindings and lifetime

A **name** is an identifier for an entity such as a variable, and its **attributes** include its type, value, scope and lifetime. A **binding** associates a name with an attribute. The **binding time** is when that happens, and the **scope of a binding** is the part of the program where it holds.

The **lifetime** of a binding is the time it exists during execution. A local variable lives only while its function runs; a static variable lives for the whole program. **Aliasing** occurs when two names refer to the same memory location, so changing one changes the other.

Source: CSC 331 Programming Principles and Paradigms.pdf (course book), Study Session 11 (for, while, do, switch, break and continue) and Study Session 12 (scope, visibility, nested functions); the four control flows, lifetime and aliasing are general knowledge, following the CSC 331 past papers (2021/22 and 2024/25 papers)
