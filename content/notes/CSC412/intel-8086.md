# The Intel 8086 Microprocessor

## The 8086

Intel launched the **8086** in 1978. It is a **16-bit** microprocessor:

- a 16-bit data bus (D0–D15);
- a **20-bit address bus** (A0–A19), so it can reach 2²⁰ = **1 MB** of memory;
- multiplexed address and data lines (AD0–AD15, plus A16–A19);
- up to 64K I/O ports and fourteen 16-bit registers;
- a 40-pin package and a +5 V supply.

## BIU and EU

Its CPU has two parts that work in parallel:

- The **Bus Interface Unit (BIU)** sends out addresses, fetches instructions, and reads and writes memory and I/O ports.
- The **Execution Unit (EU)** tells the BIU where to fetch from, then decodes and executes instructions. It contains the decoder, the 16-bit **ALU** and the registers.

While the EU is busy, the BIU prefetches up to **six instruction bytes** into a FIFO **instruction queue**. The two units work asynchronously, overlapping fetch and execution: **pipelining**. It speeds up execution and uses the bus efficiently; but a jump makes the prefetched bytes useless, so the queue must be refilled.

## Registers

- **General purpose:** AX (accumulator), BX (base), CX (count, for shifts, rotates and LOOP) and DX (data, for multiply and divide).
- **Pointers:** SP (offset of the stack top) and BP (base pointer into the stack).
- **Index:** SI (source) and DI (destination).
- **Instruction pointer (IP):** the offset of the next instruction in the code segment.
- **Segment registers:** CS, DS, SS and ES.
- **Flag register (PSW).**

**Flags.** Six **conditional** flags (CF, PF, AF, ZF, SF, OF) are set from results, and three **control** flags (TF, single step; IF, interrupts; DF, string direction) are set by the program.

## Segmentation

The 1 MB space is used through **four 64 KB segments** at a time: code, stack, data and extra. A segment register holds the upper 16 bits of the segment's 20-bit start address. The BIU appends four zero bits, so CS = 348AH means the code segment starts at 348A0H.

## Minimum and maximum modes

The **MN/MX** pin selects the mode. Logic **1** selects **minimum mode**, a **single-processor** configuration in which the 8086 generates the bus control signals itself. Logic **0** selects **maximum mode**, a **multiprocessor** configuration, for example with an 8087 coprocessor, in which a bus controller produces the control signals.

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

The instruction groups include data transfer, arithmetic and logical, branch, machine control, flag manipulation, shift and rotate, and string instructions. **PUSH** decrements SP by 2 and **POP** increments it by 2; **IN** and **OUT** move data between the accumulator and a port.

Source: CSC 412 MICROPROCESSOR INTERFACING.pdf (Study Session 11); Case Studies Microprocessors and Microcontrollers.pptx (Unit 1)
