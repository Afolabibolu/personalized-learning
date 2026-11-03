# Programs, Programming Languages and Python Basics

## Programs and languages

A **program** is a sequence of instructions a computer executes to solve a problem. **Software** is a collection of programs and data files. **Programming** is writing, testing, debugging and maintaining those instructions. A good program is **robust, usable, reliable, maintainable, portable, readable, storage-saving and efficient**.

- **Machine language** is binary, machine-dependent and not portable.
- **Assembly language** uses **mnemonics** (Load Price, Add Tax, Store Cost). An **assembler** converts it, one-to-one.
- **High-level languages** use English-like keywords (IF, PRINT, FOR). They are one-to-many, machine-independent and portable.

A **compiler** turns source code (.java, .py) into **object code** (.obj). A **linker** joins it with libraries into an **executable** (.exe). An **interpreter** runs source line by line, so it is easy to debug but slower; Python, Ruby and JavaScript are interpreted, while C, C++ and Java are compiled.

**Paradigms**:

- **procedural**: C, Pascal, BASIC;
- **object-oriented**: Java, C++, Python;
- **functional**: Haskell, Lisp;
- **logic**: Prolog.

**Syntax** is the structure rules; **semantics** is the meaning. "Ade ate the ball" is syntactically fine but semantically odd. Errors:

- **syntax errors** break the language rules, such as a typo or a missing bracket;
- **runtime errors** crash the program, as with division by zero or a missing file;
- **logical (semantic) errors** run but give wrong results, for example from a wrong formula.

The Computer Ethics Institute's **Ten Commandments** start "Thou shalt not use a computer to harm other people."

## Python basics

**Python** was created by **Guido van Rossum** in the early 1990s and is owned by the Python Software Foundation. The course uses **Python 3** in IDEs such as PyCharm, Spyder, IDLE or Pydroid.

- **Variables** hold values: variable = value. A name has only letters, digits and _, cannot start with a digit, cannot be a **keyword** (if, while, class...) and **is case sensitive** (Age, AGE and age differ). Python is **dynamically typed**: count = 0 then count = 3.2 is allowed.
- **=** binds a value; **==** tests equality and gives True or False. Simultaneous assignment works: a, b = 10, 20.
- **Types**: int, float, str and bool. type() shows a value's type. float(3) gives 3.0, int(3.9) gives 3 and round(3.9) gives 4.
- **Operators**: ** first, then * / // %, then + −. Brackets override. 42 + 5 * 3 = 57; 3 // 2 = 1 but 3 / 2 = 1.5.
- **Strings**: + joins ("bat" + "man"), * repeats ("hello" * 5), len() gives the length and .lower() gives lower case. A missing closing quote is a syntax error.
- **input(prompt)** returns a **string**, so use int() or float() before doing arithmetic. **print()** outputs values, and commas separate them with spaces.
- **Comments** start with **#**, and the interpreter ignores them. **import math** gives functions such as math.sqrt().

Source: COS 102 Introduction to Programming (Lecture 3); COS 102 Lecture 8 (introduction to programs and Python)
