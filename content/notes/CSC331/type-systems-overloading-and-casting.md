# Type Systems, Overloading and Casting

## Types and type systems

A **type** is a set of values and a set of operations on them. For example, int has values {…, −1, 0, 1, …} with +, −, * and /, and Boolean has {true, false}.

A **type system** assigns a type to each construct of a program (variables, expressions, functions) to reduce bugs. It checks that the parts of a program connect consistently, **statically** (at compile time), **dynamically** (at run time) or both. A **type error** is an operation attempted on a value for which it is not defined.

Data types are **elementary** (fixed memory: byte, short, int, long, float, double, char, boolean) or **structured** (variable memory: arrays). In Java:

- short uses a half word (16 bits);
- int a word (32 bits);
- long a double word (64 bits);
- float 32 bits and double 64 bits (IEEE 754);
- char 16 bits of **Unicode**.

In C, "hello" takes 6 bytes of ASCII including the terminating null.

## Static versus dynamic, weak versus strong

- **Statically typed** languages (C, Java) fix one type per variable at compile time. **Dynamically typed** languages (LISP, Scheme) let types change at run time.
- A language is **strongly typed** if all its type errors are detected, at compile or run time, before they execute. Java is strongly typed; C is not.

| | Static | Dynamic |
| --- | --- | --- |
| **Weak** | C, C++, Objective-C | (no types to infer) |
| **Strong** | Java | Python, JavaScript, Ruby |

Dynamic languages often use **duck typing**: an object's type is decided by what it can do at run time.

## Overloading

**Overloading** uses one name for several definitions in the same scope, a form of **polymorphism**.

- **Function/method overloading:** methods share a name but differ in their parameters. C++ and Java both support it.
- **Operator overloading:** C++ lets programmers redefine operators for classes, such as + for a Complex class. The operators ::, . and .* cannot be overloaded.
- Java does **not** allow operator overloading, apart from + for strings: it makes code complex, confuses programmers and complicates tools, and method overloading gives the same effect. Critics note that it can change an operator's usual meaning, for example making + non-commutative for strings.

## Conversion and casting

A **conversion (cast)** translates a value from one type to an equivalent value in another.

- In Java arithmetic, if either operand is double, the other becomes double; otherwise float, then long, otherwise int.
- **Widening** converts a narrower type to a wider one safely (int to double).
- **Narrowing** may lose information (1.5 to 1). Java reports it as a compile-time error unless the programmer casts explicitly: `int k = (int) (i / j);`

Source: CSC 331 Programming Principles and Paradigms.pdf (course book), Study Session 7 (type systems, elementary types, static and dynamic, weak and strong typing) and Study Session 10 (overloading, conversion and casting)
