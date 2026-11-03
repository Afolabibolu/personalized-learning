# Programming Languages and Their Generations

## What is a programming language?

A **programming language** is a **formal set of rules and syntax used to write instructions that a computer can understand and execute**. It is the medium through which a programmer communicates logic and algorithms to a machine. Its key characteristics are:

- **Syntax**: the rules that define the structure of valid statements;
- **Semantics**: the meaning behind those statements;
- **Abstraction**: hiding low-level hardware complexity; and
- **Portability**: the ability to run on different platforms.

Languages exist because computers understand only **binary (0s and 1s)**, and writing software directly in binary is tedious and error-prone. Languages provide human-readable syntax, automate translation to machine code and enable code reuse.

## Generations of programming languages

| Generation | Name | Example |
| --- | --- | --- |
| 1GL | Machine language | 10110000 01100001 |
| 2GL | Assembly language | MOV AX, 5 |
| 3GL | High-level language | Java, C++, Python |
| 4GL | Very high-level | SQL, MATLAB |
| 5GL | Natural / AI-based | Prolog, Mercury |

Abstraction increases down the table: languages become easier to write and more removed from the hardware.

- **Machine language (1GL)** is the lowest level, written in binary or hexadecimal, the only form a CPU executes directly. It needs **no translation** and runs extremely fast, but it is **unique to each CPU** and nearly impossible for humans to read.
- **Assembly language (2GL)** uses human-readable **mnemonics**, **one per machine instruction**, and is converted to machine code by an **assembler**. It is still hardware-specific and is used in device drivers and embedded systems.
- **High-level languages (3GL)** have natural-language-like syntax and are converted by a **compiler** or **interpreter**. They are easy to read and debug, have rich libraries and allow faster development.

## Compiled and interpreted languages

A **compiled** language (C, C++) is translated entirely into machine code **before** execution: fast, but it must be recompiled for each platform. An **interpreted** language (Python, JavaScript) is translated and executed **line by line at runtime**: flexible, but slower. **Java is a hybrid**: it compiles to **bytecode** (a .class file), which the **Java Virtual Machine (JVM)** runs, making Java platform-independent.

## A first Java program

In `public class HelloWorld`, the **filename must match** the class name. `public static void main(String[] args)` is the program's **entry point**, `String[] args` holds command-line arguments, `System.out.println()` prints a line, and `//` starts a comment ignored by the compiler. You compile with `javac HelloWorld.java` and run with `java HelloWorld`.

Source: COS 201 Computer Programming I.pdf (Weeks 1-2) (Week 1, Topics A and B)
