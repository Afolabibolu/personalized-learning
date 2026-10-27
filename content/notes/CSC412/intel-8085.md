# The Intel 8085 Microprocessor

## Features

The **8085** is an **8-bit** microprocessor in a **40-pin** IC, using a +5 V supply. Its address bus is **16 bits** wide, so it can address 2¹⁶ = **64 KB** of memory.

## Registers and flags

- The **accumulator (A)** is an 8-bit register that is part of the ALU; it holds one operand and the result of arithmetic and logic operations.
- Six 8-bit **general-purpose registers** B, C, D, E, H and L can be paired as **BC, DE and HL** for 16-bit operations.
- The **flag register** has five flags set by the result: **Sign (S)**, a copy of bit D7; **Zero (Z)**, set when the result is zero; **Auxiliary Carry (AC)**, a carry from D3 to D4; **Parity (P)**, set when the result has an even number of 1s; and **Carry (CY)**.
- The **program counter (PC)** is a 16-bit register pointing to the next byte to fetch.
- The **stack pointer (SP)** is a **16-bit** register pointing to the top of the stack in R/W memory.

## Buses and control signals

The **data bus** (D0–D7) is 8 bits and **bidirectional**. The address lines A8–A15 carry the high byte, and **AD0–AD7** are multiplexed: address in the first clock cycle, data later. Control and status signals:

- **ALE:** address latch enable, a pulse when an address is on AD0–AD7.
- **RD** and **WR:** active-low read and write.
- **IO/M:** distinguishes an I/O operation from a memory operation.
- **S1** and **S0:** status signals giving the type of operation.
- **HOLD** and **HLDA:** a DMA controller requests the buses, and the 8085 acknowledges.

## Instructions

**By function:** data transfer (copies data; the source is unchanged), arithmetic (results in the accumulator), logical (AND, OR, EXOR, NOT), branching (conditional and unconditional transfers), and **machine control** (interrupt, halt and similar operations, such as HLT, NOP, EI and DI).

**By length:** **one-byte** (MOV A, B; ADD M), **two-byte** (MVI A, 7FH; ADI 0FH, opcode then data) and **three-byte** (JMP 9050H; LDA 8850H, opcode then a 16-bit address, low byte first).

**Addressing modes:** immediate, memory direct, register direct and indirect.

## Interrupts

An interrupt makes the processor save the PC and state on the stack, run an interrupt service routine (ISR), and return. Interrupts are vectored or non-vectored, maskable or non-maskable, and software or hardware. The software interrupts are the eight one-byte **RST 0–7** instructions.

The five **hardware interrupts**, in priority order:

| Interrupt | Vector | Type |
| --- | --- | --- |
| TRAP | 0024H | non-maskable, highest priority |
| RST 7.5 | 003CH | maskable, rising edge |
| RST 6.5 | 0034H | maskable, level |
| RST 5.5 | 002CH | maskable, level |
| INTR | from hardware | maskable, lowest |

DI disables all interrupts except TRAP.

Source: CSC 412 MICROPROCESSOR INTERFACING.pdf (CSC 412 course material, Adebola K. Ojo), Study Session 6
