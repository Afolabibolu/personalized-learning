# Code Optimization, Code Generation and Error Handling

## Optimization

**Optimization** transforms code to use fewer resources and run faster. It must not change the meaning of the program, should increase speed, and should itself be fast. It can be done by the user on the source, by the compiler on the intermediate code, and when producing target code.

- **Machine-independent** optimization works on intermediate code without registers or absolute addresses, for example moving a repeated assignment x = 10 out of a loop.
- **Machine-dependent** optimization works on target code, using registers and the memory hierarchy.

**Peephole optimization** examines a small portion of code at a time:

- **Redundant instruction elimination:** MOV x, R0 followed by MOV R0, R1 becomes MOV x, R1.
- **Unreachable code:** a statement after a return is removed.
- **Flow of control:** a jump to a jump goes straight to the final label.
- **Algebraic simplification:** a = a + 0 is removed, and a = a + 1 becomes INC a.
- **Strength reduction:** x * 2 becomes a left shift, x << 1.

**Loop optimization** includes moving loop-invariant code, which computes the same value on every iteration, out of the loop, and induction variable analysis.

## Code generation

The code generator maps the intermediate representation (an abstract syntax tree, Reverse Polish Notation or three-address code) to the target machine's instructions. It must consider the target language and architecture (CISC or RISC), **instruction selection**, **register allocation** and the **ordering of instructions**. It tracks registers with a **register descriptor** and the locations of values with an **address descriptor**, and uses **getReg** to choose a register.

There are four alternatives for generating object code:

1. **Absolute machine language**, if the machine's architecture and registers are known.
2. **Relocatable machine language**, which needs a link loader.
3. **Assembly language**, which needs an assembler.
4. **Another programming language**, such as BASIC or Java source to Pascal or C.

**Bootstrapping** writes a compiler for a small subset L0 of a language in assembly language, rewrites it in L0 itself, and extends it step by step to the full language.

## Error handling

Errors arise in the compiler or its environment, in the program's design, from an incomplete understanding of the language, from transcription and from incorrect data. The error handler **detects** each error, **reports** it and may **repair** it so processing can continue. It should report clearly, recover quickly to find later errors, and add little overhead to correct programs.

Reports are classified by severity: **notes**, **comments** and **warnings** are anomalies; **errors** can be repaired, **fatal errors** stop an executable being produced, and **deadly errors** end compilation. Errors may be **lexical** (misspelt keywords), **syntactic** (a missing semicolon), **semantic** (type mismatch) or **logical** (unreachable code). Parser recovery strategies are **panic mode** (discard input up to a synchronizing token such as a semicolon), **statement mode** (local corrections), **error productions** and **global correction**.

Source: CSC 431 Compiler Construction.pdf (Ibadan Distance Learning course material), Study Sessions 10 and 11
