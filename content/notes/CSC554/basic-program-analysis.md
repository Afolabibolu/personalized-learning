# Basic Program Analysis

## What it is

Program analysis is the systematic examination of programs to understand their behaviour, structure, correctness and performance. Its goals are to improve the reliability, efficiency and security of software. It is used in compiler design, software testing, program verification and optimisation, and it usually precedes program transformation.

**Why it matters:**
- bug detection before users meet the bugs
- optimisation of speed and resource use
- security, by finding buffer overflows and SQL injection
- quality assurance, documentation and maintainability

## Static analysis

Static analysis examines code **without executing it**. It is also called compile-time analysis, and it uses tools such as linters and static analysers.

- **Syntax analysis** checks the code against the language's grammar, for example finding a missing colon in Python.
- **Type analysis** checks that data types are used consistently, for example adding an int to an array.
- **Linting**, for example with Pylint, finds likely errors, style issues and convention breaches. **Type checking**, for example with mypy, catches type bugs early. **Complexity analysis**, for example with Radon, measures cyclomatic complexity and Halstead metrics.

**Control flow analysis (CFA)** examines the paths a program can take during execution. A **control flow graph** has a node for each basic block, a sequence of statements with no branching, and edges for the jumps between blocks, with an entry node and an exit node. Within one function, CFA finds code that never runs and variables used before they are assigned. **Interprocedural** analysis follows calls between subprograms using a **call graph**. Polymorphism and dynamic binding make that harder.

**Data flow analysis (DFA)** traces how values move through a program. It finds where each variable is defined and used and builds a **def-use graph**. From it, DFA works out **reaching definitions**, **live variables** and **available expressions**, and flags variables that may be used before they are defined. Pointers and aliases make it complex.

## Dynamic analysis

Dynamic analysis runs the program and observes it. It is also called run-time analysis. Dividing by zero in divide(10, 0), for example, is only detected when the code runs.

- **Dynamic testing:** unit, integration, system and acceptance tests.
- **Program slicing:** extracts the part of the code that affects, or is affected by, a chosen variable or statement.
- **Profiling:** measures execution time, resource use and call frequency, for example with Python's cProfile.

**Performance analysis** looks for bottlenecks. Memoizing a recursive factorial, for example, cuts repeated work. Static and dynamic analysis complement each other.

## Tools

- **LLVM:** modular, many languages, but a steep learning curve.
- **GCC:** widely supported, with built-in static checks.
- **SonarQube:** continuous code-quality inspection for 27+ languages.
- **Clang Static Analyzer:** for C, C++ and Objective-C.
- **FindBugs:** for Java.
- **Valgrind:** dynamic analysis.

Source: Basic Program Analysis .pdf; CSC 554 Group 3 Term Paper.pdf (Basic Program Analysis)
