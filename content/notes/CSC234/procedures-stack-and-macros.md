# Procedures, the Stack, Macros and Interfacing with C

## Procedures

A **procedure** is a part of code that can be called from a program to perform a specific task; it makes programs more structured and easier to understand, and returns to the point it was called from. Its declaration is

name PROC
   ; the code of the procedure
   RET
name ENDP

The same name must appear at the top and bottom. **PROC and ENDP are compiler directives**, not assembled into machine code. **CALL** calls a procedure and **RET** returns to the caller (it also returns a program to the operating system, which sees the program as a procedure). Procedures avoid repeating commands and reduce coding and debugging time. Parameters are passed in **registers or on the stack**.

## The stack

The **stack** is an area of memory for keeping temporary data. CALL uses it to keep the **return address**, and RET takes the value back; INT stores the flags, CS and offset on it, and IRET restores them. Two instructions work with it directly: **PUSH** stores a 16-bit value on the stack, and **POP** gets a 16-bit value from it. The stack uses the **LIFO (Last In, First Out)** principle: values pushed in the order 1, 2, 3 are popped as 3, 2, 1. SS and SP locate the top of the stack.

## Macros

**Macros look like procedures, but exist only until the code is compiled**: after compilation, every macro is replaced with real instructions, and an unused macro is ignored. emu8086.inc is a file of such macros. Unlike procedures, macros must be **defined above** the code that uses them, and their end is marked by **ENDM**.

Differences between macros and procedures:

- A procedure is used with **CALL**; a macro by typing its name.
- A procedure is located at one address, and the CPU transfers control there each time; CALL takes about 3 bytes, so the executable grows little however often it is called. A macro is **expanded directly in the code**, so using it 100 times inserts its instructions 100 times and makes the file larger.
- Parameters go to a procedure via the stack or registers; to a macro, they are typed after its name.

Because macros are expanded in place, labels inside them cause a "duplicate declaration" error when the macro is used twice; the **LOCAL** directive avoids this.

## Interfacing with C

Machine language is executed directly; assembly matches it roughly one for one, and high-level languages are closer to English. All must be converted to machine language by **translators**: an **assembler**, or a **compiler** or **interpreter**. Many programmers prefer C, a mid-level language, and call assembly routines from it, or use inline assembly, for speed-critical parts.

Source: csc234 assemblylanguage.pdf (CSC 234 course book, I. T. Ayorinde), Study Sessions 9 to 12 (Procedures, Stack, Macros, Interfacing C with Assembly Language)
