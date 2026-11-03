# Programming Languages, C# and .NET

## Programming languages

A **programming language** is a set of rules that provides a way of telling a computer what operations to perform: **a set of rules for communicating an algorithm**. Like English, it has words, symbols and grammatical rules; the grammatical rules are its **syntax**, and learning one means learning new vocabulary, syntax and semantics. The first languages appeared in the 1950s, and thousands have been developed since.

- **First generation (machine language)**: binary, machine dependent and the only language the computer understands directly; very efficient but very difficult to write.
- **Second generation (assembly language)**: symbolic operation codes replace binary ones; the program is assembled, each instruction becoming one machine instruction.
- **Third generation**: closer to English with simple mathematical notation. **Source code** is translated to **object code** by a **compiler**, or run by an **interpreter**. Examples: FORTRAN, COBOL, C, C++, Visual Basic.
- **Fourth generation**: fewer instructions per task; query languages, report generators and forms designers used with databases. Then the **fifth generation**.

Paradigms include **imperative** (C), **object-oriented** (C++), **logic/declarative** (Prolog) and **functional** (Lisp). Traditional languages are sequences of instructions; object-oriented languages create objects.

A little history: **FORTRAN** (formula translation) was developed at IBM in the mid-1950s for scientific work; **COBOL** in 1959 for business; **BASIC** at Dartmouth College in the mid-1960s for students; **C** at Bell Laboratories in the early 1970s (UNIX is written in C). **Simula** (Ole Johan Dahl, 1960s) was the first object-oriented language and **Smalltalk** (Xerox, mid-1970s) the first purely object-oriented one. **Java**, similar to C++ without many of its problematic features, aims to be machine, platform and operating-system independent.

## C# and .NET

With the **.NET framework**, Microsoft introduced **C#** (C Sharp): a simple, modern, general-purpose, **object-oriented** language that borrows key ideas from other languages, most notably **Java**, and is approved by ECMA. In practice it is always used with the .NET framework, so it is sometimes called *the* .NET language. Its features include Boolean conditions, **automatic garbage collection**, a standard library, properties and events, delegates, generics, indexers, conditional compilation, simple multithreading, and LINQ and lambda expressions.

C# is designed for the **Common Language Infrastructure (CLI)**: executable code and a runtime environment that let many high-level languages run on different platforms. The .NET framework's components include the **Common Language Runtime (CLR)**, the Framework Class Library, the Common Language Specification and the Common Type System. C# code is compiled to **Intermediate Language** code, which **Just-In-Time (JIT) compilation** turns into machine code as the program runs. An **IDE** such as Visual Studio provides the editor and tools.

Source: Introduction to C# Programming Language, weeks 1-3 slides; QuickGuideCsharp.pdf (C# Quick Guide, filed with the course), introduction and environment (the IL and JIT sentence expands the slide headings from general knowledge)
