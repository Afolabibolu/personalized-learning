# Translators and the Compiler Overview

## Languages and translators

Computer languages are of three kinds: **high-level** (English-like and human-friendly, such as COBOL, FORTRAN, Pascal and C++), **assembly** (mnemonics such as LDA, ADD and JMP, studied for a particular processor) and **machine** language (0s and 1s, the only language the computer understands).

A **translator** takes a program in a source language and produces a program in a target (object) language. Translation involves **lexical analysis** (characters into symbols), **syntax analysis** (symbols into a structure), **type checking** and **code generation**. Translators are compilers, interpreters and assemblers.

- A **compiler** reads the whole source program, may take several passes, and reports all the errors it finds.
- An **interpreter** reads one statement, converts it to an intermediate code, executes it, and stops at the first error.
- An **assembler** translates assembly language into an object file of machine instructions.

**Similarities:** both compilers and interpreters translate high-level programs so they can run, and both check syntactic and semantic correctness. **Differences:** a compiler produces an object program and an interpreter does not; interpreters are more **versatile** (a compiler is made for one machine), better for **debugging** and run-time errors, and can **simulate** a new machine; compiled programs run **ten to a hundred times faster** and are translated only once.

A **linker** merges object files into one executable and resolves references; a **loader**, part of the operating system, loads the executable into memory and starts it.

## Structure of a compiler

- The **analysis phase** (front end) reads the source program, checks lexical, grammar and syntax errors, and produces an intermediate representation and the symbol table.
- The **synthesis phase** (back end) generates the target program.

Logically, a compiler has a **scanner**, **syntax and semantic analysers**, **preparation for code generation** (storage allocation and optimization) and **code generation**, all sharing **tables of information**: the **symbol table** (identifiers with their attributes and addresses), a constant table and a for-loop table.

## Types of compiler

- **Single-pass:** all four processes in one module; **multi-pass:** in separate modules, suited to machines with little RAM.
- **Compiler-compilers:** generators that produce a compiler from a language definition.
- **Cross compilers:** run on platform A and generate code for platform B.
- **Source-to-source compilers:** translate one programming language into another.

A **phase** is a distinguishable stage, such as lexical or syntax analysis; a **pass** is one traversal of the whole program and can contain several phases. A good compiler has good **error diagnostics and reporting**, **speed**, and is **efficient, accurate** and **bug free**.

Source: CSC 431 Compiler Construction.pdf (Ibadan Distance Learning course material), Study Sessions 1 and 5
