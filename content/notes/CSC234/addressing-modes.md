# The 80x86 Addressing Modes

## Addressing modes

When Intel designed the 8086, it provided a flexible, though limited, set of ways to access operands; mastering them is the first step to mastering 80x86 assembly. The three groups are **immediate**, **register** and **memory** addressing.

- **Immediate addressing**: the data is part of the instruction, as in mov ax, 0035h, where 0035h is a constant. Adding constants directly into AX is immediate addressing.
- **Register addressing**: the operand is a register, named in the instruction: mov si, dx. Most 8086 instructions can operate on the general purpose registers, and both operands must be the same size.

## Memory addressing modes

The effective address (EA) is formed from an offset, and the physical address is segment × 10h + EA.

1. **Direct addressing**: a 16-bit memory address (offset) is given directly in the instruction, as in mov ax, [5000h] or mov ax, num1. The physical address is **10h × DS + 5000h**. Several numbers can be added "directly in memory" using one label with offsets, or several labels.
2. **Register indirect addressing**: the offset of the data is in **BX, SI or DI**, and the default segment is DS or ES: mov ax, [bx] reads from **10h × DS + [BX]**. This suits stepping through an array by changing BX.
3. **Indexed addressing**: the offset is in an **index register, SI or DI**, with DS and ES the default segments for SI and DI respectively; it is a special case of register indirect.
4. **Based indexed addressing**: the EA is the sum of a **base register (BX or BP)** and an **index register (SI or DI)**, as in mov ax, [bx][si].
5. **Register relative addressing**: the EA is an **8-bit or 16-bit displacement** plus BX, BP, SI or DI: mov ax, 50h[bx] reads from **10h × DS + 50h + [BX]**.
6. **Relative based indexed addressing**: the EA is a displacement plus a base register plus an index register: mov ax, 50h[bx][si].

Choosing the right addressing mode is a key to good assembly language: register and immediate operands avoid memory access and are fastest, while the memory modes let one instruction work through arrays and tables. Writing small programs, such as adding three numbers stored in memory, in each mode is the best practice.

Source: csc234 assemblylanguage.pdf (CSC 234 course book, I. T. Ayorinde), Study Session 4 (The 80x86 Addressing Modes)
