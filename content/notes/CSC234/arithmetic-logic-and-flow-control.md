# Arithmetic, Logic and Program Flow Control

## Arithmetic and logic

Most arithmetic and logic instructions affect the processor status register, the **flags**. The first group of instructions, **ADD, SUB, CMP, AND, TEST, OR and XOR**, take two operands, each a register, memory or immediate value (but not two memory operands). Others include INC and DEC, MUL and IMUL, DIV and IDIV, NEG and NOT. Logical AND, OR and NOT follow the bit rules: AND gives 1 only when both bits are 1, OR when either is, NOT inverts. They are used, for example, to evaluate a logical expression such as A := ((X = Y) and (Z ≠ S)) or (X ≤ Y).

## The flags register

The flags register has 16 bits; each bit is a **flag** that is 1 or 0:

- **Carry Flag (CF)**: set to 1 on an **unsigned overflow**, as when adding bytes 255 + 1.
- **Zero Flag (ZF)**: set to 1 when the **result is zero**.
- **Sign Flag (SF)**: set to 1 when the result is **negative**; it takes the value of the most significant bit.
- **Overflow Flag (OF)**: set to 1 on a **signed overflow**, as when adding bytes 100 + 50, whose result is outside −128 to 127.
- **Parity Flag (PF)**: 1 when the result has an **even number of one bits** (only the low 8 bits are checked).
- **Auxiliary Flag (AF)**: unsigned overflow of the low nibble.
- **Interrupt enable Flag (IF)**: when 1, the CPU reacts to external interrupts.
- **Direction Flag (DF)**: 0 processes data chains forward, 1 backward.

## Program flow

The basic instruction that transfers control to another point is **JMP**, an **unconditional** jump to a **label**. A label is a name followed by ":"; it cannot start with a number. **Conditional jumps** jump only when a condition holds, as set by **CMP** (which subtracts without storing the result) or by arithmetic:

- **JE** jumps if the first operand is **equal** to the second; **JNE** if **not equal**.
- **JZ** jumps if **zero**, set by CMP, SUB, ADD, TEST, AND, OR and XOR.
- **JLE** jumps if the first operand is **less than or equal** to the second, and **JG**, **JL**, **JA** and **JB** test greater, less, above and below.

## Loops

A program that sums many numbers or repeats an operation does so by **looping**: initialise a counter (often **CX**), perform the operation, decrement the counter and jump back while it is not zero. Adding ten numbers stored in memory with register + offset addressing is the course's standard loop example.

Source: csc234 assemblylanguage.pdf (CSC 234 course book, I. T. Ayorinde), Study Session 7 (Arithmetic and Logic Functions) and Study Session 8 (Program Flow Control)
