# 8086 Architecture and Programming

## The 8086

Intel launched the **8086** in 1978. It is a **16-bit** microprocessor:

- a 16-bit data bus (D0–D15);
- a **20-bit address bus** (A0–A19), so it can reach 2²⁰ = **1 MB** of memory;
- multiplexed address and data lines (AD0–AD15, plus A16–A19);
- up to 64K I/O ports and fourteen 16-bit registers;
- clock speeds of 5 MHz (8086), 8 MHz (8086-2) and 10 MHz (8086-1).

## BIU and EU

Its CPU has two parts that work in parallel:

- The **Bus Interface Unit (BIU)** sends out addresses, fetches instructions, and reads and writes memory and I/O ports.
- The **Execution Unit (EU)** tells the BIU where to fetch from, then decodes and executes instructions. It contains the instruction decoder, control system, a 16-bit **ALU** and the registers.

While the EU is busy, the BIU prefetches up to **six instruction bytes** into a FIFO **instruction queue**. Fetching the next instruction while the current one executes is called **pipelining**.

## Registers

- **General purpose:** AX (accumulator), BX (base), CX (count, for shifts, rotates and LOOP) and DX (data, for multiply and divide). Each splits into 8-bit halves (AH/AL).
- **Pointers:** SP (offset of the stack top) and BP (base pointer into the stack).
- **Index:** SI (source) and DI (destination), used by string instructions.
- **Instruction pointer (IP):** the offset of the next instruction in the code segment.
- **Segment registers:** CS, DS, SS and ES.
- **Flag register (PSW).**

**Flags.** Six **conditional** flags are set from results: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF) and overflow (OF). There are three **control** flags: trap (TF, single-step mode), interrupt (IF, enables masked interrupts) and direction (DF, the direction for string processing).

## Segmentation

The 1 MB space is used through **four 64 KB segments** at a time: code, stack, data and extra. A segment register holds the upper 16 bits of the segment's 20-bit start address. The BIU appends four zero bits, so CS = 348AH means the code segment starts at 348A0H.

## Addressing modes

1. **Register**
2. **Immediate**, where the data is in the instruction
3. **Direct**, where the address is in the instruction
4. **Register indirect**, through a register
5. **Indexed**, index register plus displacement
6. **Based**, BX or BP plus displacement
7. **Based and indexed**
8. **Based and indexed with displacement**

## Instructions

An **opcode** says which operation to perform, **operands** are the data, **mnemonics** are symbolic codes and an **assembler** converts them into machine code.

The groups include data transfer, arithmetic and logical, branch, machine control, flag manipulation, shift and rotate, and string instructions.

Source and destination cannot both be memory. **PUSH** decrements SP by 2 and **POP** increments it by 2; the stack is last-in, first-out. **IN** and **OUT** move data between the accumulator and a port, and DX is the only register that can hold a port address.

Source: Case Studies Microprocessors and Microcontrollers.pptx (Unit 1)
