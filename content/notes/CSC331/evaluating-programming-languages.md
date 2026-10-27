# Evaluating Programming Languages

A language's quality must be judged before programmers adopt it. The book gives nine evaluation criteria.

1. **Expressivity:** how clearly the language reflects the programmer's intended meaning, compactly and with uniformly used symbols. The same assignment can be written `C = A + B`, `C := A + B`, `(SETQ C (+ A B))` or `ADD A, B GIVING C`.
2. **Well-definedness:** the syntax and semantics are free from ambiguity and completely specified, so a programmer can predict each expression's behaviour. This encourages portability.
3. **Data types and structures:** support for integers, reals, strings and pointers, for arrays and records, and for dynamic structures.
4. **Modularity:** support for subprograms, and **extensibility** (programmer-defined operators and data types).
5. **Input-output facilities:** support for sequential, indexed and random-access files.
6. **Portability:** implemented on many machines; standardised (ANSI) languages such as ANS FORTRAN and COBOL port best, while BASIC's dialects do not.
7. **Efficiency:** fast compilation and execution; compiled programs are usually more efficient than interpreted ones.
8. **Pedagogy:** easy to teach and learn; BASIC and Pascal were designed for teaching.
9. **Generality:** useful across many applications, as PL/1 and APL were.

The lecture slides group these as **readability, writability and reliability**.

## Other design criteria

- **Simplicity and clarity:** easy to learn and read.
- **Binding:** when an element is bound to a property. This happens at:
  - **language definition time** (int bound to integers);
  - **implementation time** (1.5 bound to its IEEE 754 form);
  - **program writing time** (names bound to types);
  - **compile/load time** (static variables to memory);
  - **run time** (x = 5).

  Binding is **early** or **late**.
- **Orthogonality:** a small set of features combine predictably, and a symbol keeps the same meaning in every context. Java's + for both addition and string concatenation is a counter-example.
- **Reliability:** programs behave the same on every run and platform, helped by exception handling, strong typing, well-defined syntax and resistance to aliasing and memory leaks.
- **Applicability:** suitable support for its application domain.
- **Abstraction:** data and procedural abstraction for code reuse, such as Java's class libraries.
- **Efficient implementation:** ALGOL 68 was elegant but too complex to implement efficiently.

Source: CSC 331 Programming Principles and Paradigms.pdf (course book), Study Session 5 (criteria for evaluating languages and other design criteria); readability, writability and reliability are from the lecture slides and general knowledge, following the CSC 331 past papers (2024/25 paper, Question 1)
