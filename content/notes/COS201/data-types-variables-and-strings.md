# Data Types, Variables and Strings

## Data types

A **data type** defines the kind of value a variable can hold, how much memory it occupies and what operations it supports. **Java is strongly typed**: every variable must be declared with a type before use. There are two categories:

- **Primitive types** are built into the language, store values directly and have a fixed size. There are **eight**: `byte` (8 bits, -128 to 127), `short` (16 bits), `int` (32 bits, about plus or minus 2.1 billion), `long` (64 bits, needs the **L** suffix), `float` (32 bits, about 7 digits, needs the **f** suffix), `double` (64 bits, about 15 digits), `char` (16 bits, a single Unicode character) and `boolean` (true or false).
- **Reference types** are defined by classes and store **memory addresses**: String, arrays and objects.

Rule of thumb: `int` for whole numbers, `double` for decimals, `boolean` for true/false and `char` for single characters.

## Type casting

**Type casting** converts a value from one type to another. **Widening** (smaller to larger, byte → short → int → long → float → double) is **automatic** and loses no data: `double d = x;`. **Narrowing** (larger to smaller) needs an explicit **cast operator** and may lose data: `int x = (int) 9.99;` gives **9**, because the decimal part is **truncated, not rounded**.

## Variables and constants

A **variable** is a **named memory location** whose value can change during execution, declared as `dataType variableName = value;`. Names must start with a letter, `_` or `$`, contain no spaces, are **case-sensitive** (`age` differs from `Age`), cannot be keywords, and use **camelCase** by convention. Variables are **local** (in a method), **instance** (in a class) or **static** (shared across all instances).

A **constant** is declared with **final** and cannot be changed after initialisation; by convention it is written in **ALL CAPS**, as in `static final double PI = 3.14159;`. Assigning to it again is a compile error.

## Strings

A **String** is a **sequence of characters**. Unlike the primitives it is a **reference type (a class)**, and Strings are **immutable**: once created, their content cannot change. Concatenation uses `+`, and `"Age: " + 21` converts the number automatically. Useful methods:

- `length()`; `charAt(i)`; `substring(i, j)` (from index i to j-1, so `"Hello".substring(1,3)` is `"el"`);
- `toUpperCase()` and `toLowerCase()`;
- `contains()`, `indexOf()`, `replace()` and `trim()`;
- `equals()` and `equalsIgnoreCase()`.

Compare strings with **`equals()`, not `==`**: `"Java".equals("java")` is false, while `equalsIgnoreCase` gives true.

The **Scanner** class (`java.util.Scanner`) reads keyboard input with `nextLine()`, `nextInt()` and `nextDouble()`, and should be **closed** when done.

Source: cos201_weeks3to6.pdf (Week 3: Basic Data Types and Strings)
