# Computer Architecture and 8086 Registers

## Architecture and buses

The basic operational design of a computer is its **architecture**. John Von Neumann is credited with the architecture of most computers in use today, including the 80x86 family: the **Von Neumann architecture** has a **CPU**, **memory** and **input/output**, connected by the **system bus**, a collection of wires carrying signals between components. The 80x86 has three major buses:

- The **data bus** moves data between memory, I/O and the processor, and its size defines the "size" of the processor: 8 bits on the 8088, 16 on the 8086, 32 on the 80386DX and 80486, and 64 on the Pentium.
- The **address bus** says *which* memory location or I/O device: with n address lines the processor can address 2ⁿ locations. The 8086's **20-bit address bus** reaches **1,048,576 (1 MB)** locations.
- The **control bus** carries the read and write lines, which set the direction of data flow, along with clocks, interrupt and status lines.

## Machine and assembly language

**Machine language** is what the CPU executes directly; **assembly language** writes the same instructions as readable **mnemonics**. An **assembler** is a program that converts assembly code into machine code; it is much simpler than a compiler, because **every assembly statement represents a single machine instruction**. Each type of CPU has its own machine and assembly language. Assembly programs are fast, small and give total control of the machine, which suits device drivers, firmware and time-critical code.

## Registers

Registers are temporary storage **inside the CPU**, much faster than memory because no bus access is needed. The 8086 has eight general purpose registers, the first four split into high and low 8-bit halves:

- **AX**, the accumulator (AH/AL); **BX**, the base address register (BH/BL); **CX**, the count register (CH/CL); **DX**, the data register (DH/DL).
- **SI** (source index), **DI** (destination index), **BP** (base pointer) and **SP** (stack pointer).

The **segment registers** point at blocks of memory: **CS** (code segment, the current program), **DS** (data segment, the variables), **ES** (extra segment, defined by the coder) and **SS** (stack segment). They should not hold arbitrary data. The CPU forms a **physical address** as **segment × 10h + offset**: DS = 1230h and SI = 0045h give 12345h. By default BX, SI and DI work with DS, and BP and SP with SS. **IP** works with CS and points to the current instruction, and the **flags register** records the CPU's state after operations.

Source: csc234 assemblylanguage.pdf (CSC 234 course book, I. T. Ayorinde), Study Session 2 (Introduction to Assembly Language)
