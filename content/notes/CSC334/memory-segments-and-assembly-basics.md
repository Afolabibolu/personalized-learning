# Memory Segments and Assembly Language Basics

## Program memory segments

A running program's memory is laid out in segments:

- **Code (text) segment:** the compiled machine code, often read-only.
- **Initialised data segment:** global, static, constant and external variables that are given an initial value.
- **Uninitialised data (.bss) segment:** global, static and external variables with no initial value, zero-filled.
- **Stack segment:** local variables, function parameters and return addresses; it grows and shrinks.
- **Heap segment:** dynamically allocated memory (malloc() in C).

The size of the text and data segments is known once compilation finishes; the stack and heap grow at run time.

A **compiler driver** runs the preprocessor, compiler, assembler and linker. It can produce three kinds of object file:

- **relocatable** (static libraries);
- **executable**;
- **shared** (linked dynamically at load time or run time).

Common formats are COFF and ELF.

## Why assembly language

Assembly shows how programs interface with the OS, processor and BIOS, how data is represented, and how instructions access data and devices. It needs **less memory and execution time**, suits **time-critical** jobs and hardware-specific tasks, and is ideal for **interrupt service routines**. The processor's data sizes are word (2 bytes), doubleword (4 bytes) and quadword (8 bytes).

Binary converts to hexadecimal in groups of four bits: 1000 1100 1101 0001 = 8CD1.

## NASM programs

An assembly program has three sections:

- **section .data:** initialised data and constants;
- **section .bss:** variables;
- **section .text:** the code, beginning with **global _start**.

Comments begin with a semicolon. Statements are **executable instructions**, **assembler directives (pseudo-ops)** or **macros**, written as `[label] mnemonic [operands] [;comment]`, for example `MOV TOTAL, 48` or `INC COUNT`.

To build: `nasm -f elf hello.asm`, then `ld -m elf_i386 -s -o hello hello.o`.

## IA-32 registers and flags

IA-32 has ten 32-bit and six 16-bit registers.

- **Data registers:** EAX, EBX, ECX, EDX can be used as 32-bit registers, as 16-bit AX, BX, CX, DX, or as 8-bit AH/AL, BH/BL, CH/CL, DH/DL. AX is the accumulator, BX the base, CX the count and DX the data register.
- **Pointer registers:** IP, SP and BP.
- **Index registers:** SI and DI.
- **Segment registers:** CS, DS, SS, plus ES, FS and GS.

The flags register holds OF, DF, IF, TF, SF, ZF, AF, PF and CF.

## System calls

To make a Linux system call:

1. put the call number in **EAX** (sys_exit is 1, sys_write is 4);
2. put the arguments in EBX, ECX, EDX, ESI, EDI and EBP;
3. execute **int 80h**.

The result returns in EAX.

Source: CSC 334- Systems Programming - new1.docx (course book), Unit 3 (code, data and stack segments; advantages of assembly; number systems) and Unit 4 (syntax, sections, statements, NASM, registers, system calls)
