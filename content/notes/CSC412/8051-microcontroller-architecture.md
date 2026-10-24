# 8051 Microcontroller Architecture

## Features

The **8051** is Intel's **8-bit** microcontroller. Its features:

- **4 KB** of on-chip program memory (ROM), within a **64 KB** program address space;
- **four register banks** (Bank 0 to Bank 3), each with registers R0–R7;
- **32 bidirectional I/O lines** in four 8-pin ports: P0, P1, P2 and P3;
- **two 16-bit timer/counters** (Timer 0 and Timer 1);
- a **UART** for serial communication.

The 8051 is a subset of the **8052**. The **8031** is a ROM-less 8051: adding external ROM costs two ports, leaving only two for I/O.

## Pins and ports

- **Port 0 (P0.0–P0.7):** I/O, and also the multiplexed low-order address and data bus for external memory. When **ALE** = 1 it carries address A0–A7; when ALE = 0 it carries data D0–D7.
- **Port 1:** a simple 8-bit bidirectional I/O port.
- **Port 2:** I/O, and the high-order address byte for external memory.
- **Port 3:** I/O, with extra functions such as the serial lines, interrupts, timer inputs and read/write strobes.
- **EA/VPP:** with EA = 0, the 8051 fetches program code only from external ROM. With EA = 1, it uses internal and external ROM.

## Internal registers

- The **program counter (PC)** points to the next instruction.
- The **stack pointer (SP)** is an 8-bit register holding the address of the stack top.
- The **ALU** does arithmetic and logic, and its flags include carry (C) and auxiliary carry (AC).
- **DPTR** (DPH and DPL) is a 16-bit data pointer.

The **special function registers (SFRs)** include the accumulator A, register B, PSW, SP, DPTR, the port registers P0–P3, the timer registers TMOD and TCON, SCON and SBUF for the serial port, and IE and IP for interrupts.

## Instruction set

There are five instruction groups:

1. **Arithmetic:** for example ADD, INC, DEC, MUL AB and DIV AB. MUL AB puts a 16-bit result in B and A; DIV AB puts the quotient in A and the remainder in B.
2. **Logical:** ANL, ORL, XRL, CPL A and the rotates (RL, RLC, RR, RRC).
3. **Data transfer:** MOV, MOVX for external data memory, PUSH and POP, and XCH.
4. **Boolean (bit):** CLR, SETB, CPL, and ANL/ORL with the carry, for example ANL C,P2.7.
5. **Branching:** short jumps with a 1-byte relative address (−128 to +127), absolute jumps within 2 KB, long jumps within 64 KB, and RET and RETI.

## Addressing modes

- **Immediate:** data in the instruction, marked "#".
- **Register:** between registers.
- **Direct:** the actual memory address is given.
- **Register indirect:** R0 or R1 holds the address, written with "@". R2–R7 cannot be used this way.
- **Relative:** for SJMP and conditional jumps.
- **Absolute and long:** to a label, within 2 KB or the full 64 KB.
- **Indexed:** useful for reading look-up tables.

Source: Case Studies Microprocessors and Microcontrollers.pptx (Unit 4)
