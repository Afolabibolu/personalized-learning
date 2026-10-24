# Program Transformation

## What it is

A program transformation is any operation that takes a program and generates another program. It changes the program's structure or syntax while preserving its intended functionality, and it usually follows program analysis. The kinds are:

- **Refactoring:** improves structure without changing external behaviour.
- **Optimization:** improves performance.
- **Translation:** converts code to another language.
- **Specialisation:** tailors a general program to a particular use.
- **Obfuscation:** makes code harder to understand, for security.

**Why it matters:** code maintenance, performance, portability, security, language migration, legacy modernisation and software reuse. It is applied in compiler construction, model-driven engineering, aspect-oriented programming and program synthesis.

## History

- **1950s–60s:** early compilers and optimisation (FORTRAN in 1957, COBOL in 1959).
- **1970s:** Burstall and Darlington introduced formal rules and **unfold/fold** transformations for recursive programs.
- **1980s:** program derivation and the Bird–Meertens formalism ("Squiggol").
- **1990s:** Opdyke's thesis on refactoring, and Fowler's *Refactoring* (1999).
- **2000s onward:** IDE refactoring tools, automated program repair and machine-learning-assisted transformation.

## Techniques

- **Abstract syntax tree (AST) manipulation:** parse, transform the tree, regenerate the code.
- **Term rewriting:** treat programs as terms and apply rewrite rules.
- **Pattern matching and replacement**, **slicing** and **symbolic execution**, which runs a program on symbolic values to cover all inputs.

**Source-to-source transformation** (transpilation) converts code between languages or language versions by parsing it to an AST, analysing it, modifying it and generating new code. Stratego/XT, DMS and TXL are tools for this.

**Refactoring versus optimization.** Refactoring raises readability and maintainability, for example extracting methods or renaming variables. Optimization raises speed or lowers memory use, sometimes at the cost of readability. Common optimizations:

- **Loop unrolling:** expand a loop with a known length to cut loop overhead. For example, sum += i for i < 10 becomes ten separate additions.
- **Constant folding and propagation**, **dead code elimination** and **function inlining**.
- **Algorithmic optimization:** replace a summing loop with n * (n − 1) // 2, or reverse a string with two pointers.
- **Data structure transformation:** change a list to a set to remove duplicates and speed up lookups.

**High-level versus low-level.** High-level transformations work on ASTs or control flow graphs and change algorithms or structure. Low-level transformations work near machine code, for example register allocation, instruction scheduling and peephole optimization. They are often platform-dependent.

## Challenges

The main challenges are preserving correctness, scaling to millions of lines, keeping up with evolving languages, testing safety-critical results, trading readability against speed, and handling legacy and concurrent code.

Source: CSC 554 Group 3 Term Paper.pdf (Program Transformation); Basic Program Analysis .pdf
