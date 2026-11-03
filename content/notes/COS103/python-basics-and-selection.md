# Python Basics and Selection Statements

## Elements of a program

An **expression** is the most basic instruction: a literal (3.9, "hello"), a variable (age) or a combination with operators ("bat" + "man", age ** 2). A **variable** is a named box in memory, created with **name = value**. A valid name has only letters, digits and _, does not start with a digit and is not a keyword. So **var1** and **_var** are legal, while **my-name** and **class** are illegal. Python is **dynamically typed**: count = 0 can later hold 3.2, which statically typed Java would not allow.

**Precedence**: ** first; then * / // % left to right; then + − left to right. Brackets override, so 42 + 5 * 3 = 57 but (42 + 5) * 3 = 141. Also 3 // 2 = 1 and 3 / 2 = 1.5. Simultaneous assignment works: a, b = 10, 20.

**Data types**:

- text: str;
- numeric: int, float, complex;
- sequences: list, tuple, range;
- set and frozenset;
- dict;
- bool;
- binary types.

type(x) shows the type. **Type casting** uses int(), float(), str(), list(), tuple() and dict(): int("100") gives 100. int("Hello") raises **ValueError**, and float to int **truncates**.

**Escape characters** start with a backslash: \' and \" for quotes, \\ for a backslash, \n for a new line and \t for a tab. **Multi-line strings** use triple quotes (""" ... """) or a backslash at the line end. **f-strings** (Python 3.6+) embed expressions: f"The sum of {a} and {b} is {a + b}." Comments start with #.

## Selection

- **if** condition: then an **indented** block, which runs only if the condition is True. Python uses indentation to define blocks.
- **else**: runs when the condition is False.
- **elif**: checks conditions in order, so score = 65 gives "Grade Point: 3" with the 70/60/50/45 ladder.
- **Nested if**: an if inside another, for example age ≥ 18 and then has_license.
- **Conditional expression (ternary)**: value_if_true if condition else value_if_false. result = "Positive" if number > 0 else "Negative". Expressions can be chained: "Child" if age < 18 else "Adult" if age < 65 else "Senior".

**Logical operators**:

- **and** is True only if both conditions are true;
- **or** is True if at least one is;
- **not** inverts.

Python **short-circuits**: it stops once the result is known. Use parentheses for clarity, as in has_id_card and (valid_passcode and is_admin). With x = 15 and y = 10, "x > 10 and y > 20" is False but "x > 10 or y > 20" is True.

Source: CSC 103 Lecture 2 (2024): elements of Python, selection and iteration; CSC 103 2023/24 examination
