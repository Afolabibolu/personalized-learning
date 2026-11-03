# Mnemonics, Operands and the 8086 Instruction Set

## Instruction format

The machine mnemonics give the instructions to be performed on the operands, and together they make up the **8086 instruction set**. The general format is **mnemonic, operands**. Each instruction has a fixed number of operands, **0 to 3**, of four types:

1. **Register**: refers directly to the contents of a CPU register.
2. **Memory**: refers to data in memory, by an address given directly or through registers.
3. **Immediate**: fixed values listed in the instruction itself, stored in the **code segment**, not the data segment.
4. **Implied**: not explicitly shown; for example the increment instruction adds one to a register or memory location without listing the 1.

## Basic instructions

- **MOV dest, src** copies the data in src to dest, like the assignment operator in a high-level language. **The operands must be the same size**: mov si, dx copies DX into SI, and mov sp, bp copies BP into SP.
- **ADD** adds integers and **SUB** subtracts them, each taking two operands.
- **INC** increments a value by 1 and **DEC** decrements it by 1.
- **MUL** performs unsigned multiplication and **IMUL** signed multiplication; **DIV** and **IDIV** divide.

In descriptions of the instruction set, **reg** stands for a register operand, **r/m** for a register or memory operand, and **sreg** for a segment register operand.

## Restrictions on segment registers

There are two restrictions on using segment registers with MOV: **you may not specify CS as the destination operand**, and **only one operand can be a segment register**, so data cannot be moved directly from one segment register to another. **Values cannot be loaded directly into a segment register**: to set DS, first load the value into a general register and then move it, as in mov ax, 784h followed by mov ds, ax. MOV cannot set CS or IP at all. Segment registers should only ever hold segment addresses, never arbitrary data. When a 16-bit register receives an 8-bit value, the upper part is zero: mov bx, 5 gives BX = 0005, so BH = 00 and BL = 05.

## Data declarations

Variables are declared with directives such as **DB** (define byte) and **DW** (define word), for example num1 dw 5. Labels end with a colon, and directives such as ORG, INCLUDE and END are reserved words that the assembler recognises.

Source: csc234 assemblylanguage.pdf (CSC 234 course book, I. T. Ayorinde), Study Session 3 (Mnemonics and Operands) and Study Session 7 (exceptions for segment registers)
