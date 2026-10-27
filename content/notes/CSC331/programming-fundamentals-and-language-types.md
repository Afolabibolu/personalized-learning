# Programming Fundamentals and Types of Languages

## Programming and its stakeholders

**Computer programming** is the craft of writing useful, maintainable and extensible **source code** that a computing system can interpret or compile to perform a meaningful task. It is one part of **software engineering**, which also covers design and quality control. Three groups are involved with programming languages:

- **programmers**, who use languages to build applications;
- **language designers**, who design a language's vocabulary and rules;
- **language implementers**, who write its compiler or interpreter for a machine.

A good designer must be a good programmer.

## Levels of language

1. **Declarative:** English-like command languages that say **what** to do rather than how (SQL, SAS, SPSS).
2. **High-level:** readable and **portable**, so programs can move between machines (Pascal, C, FORTRAN).
3. **Assembly:** symbolic mnemonics with a one-to-one match to machine instructions.
4. **Machine:** numeric codes the CPU executes directly.

Assembly and machine languages are **machine dependent**.

## Compilers and interpreters

Both translate programs into machine language and check them for correctness. A **compiler** translates once into an **object program**, and the compiled program runs faster. An **interpreter** produces no object program; it translates line by line, so it is more versatile and makes debugging easier.

## Types of language

- **Scientific (algorithmic):**
  - FORTRAN (1957, John Backus at IBM);
  - ALGOL (1958–60, which gave block structure and BNF);
  - LISP (about 1960, John McCarthy at MIT, used for AI);
  - C (1972, Dennis Ritchie, for operating systems).
- **Business-oriented:** COBOL (1959, CODASYL; English-like, introduced the **record**), SQL and Visual Basic.
- **Education-oriented:** BASIC (Dartmouth, Kemeny and Kurtz), Pascal (Niklaus Wirth, for structured programming), Logo (turtle graphics) and Hypertalk.
- **Object-oriented:** Simula (1967), Smalltalk (1980), C++ (Bjarne Stroustrup), ADA, Java (Sun Microsystems, with the Java Virtual Machine) and Visual Basic.
- **Functional:** LISP, ML and Haskell, which treat functions as data.
- **Declarative/logic:** Prolog, which states logical relations and answers queries with an inference engine.
- **Scripting:** Perl; and web scripting with JavaScript, VBScript and PHP.

By variable declaration, the book also groups languages as:

- **strongly typed:** variables must be declared before use (C, C++, Java);
- **weakly typed:** implicit declaration, as in FORTRAN, where names starting I to N are integers;
- **loosely typed:** a variable's type changes with its current value, as in PHP.

Source: CSC 331 Programming Principles and Paradigms.pdf (course book), Study Session 1 (programming, stakeholders, levels, compilers and interpreters) and Study Session 2 (types of programming languages and categories by variable declaration)
