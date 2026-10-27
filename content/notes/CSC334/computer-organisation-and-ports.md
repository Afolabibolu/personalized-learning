# Computer Organisation, Registers and Ports

## Systems programming

**Systems programming** produces software that serves the hardware or other software, and often deals directly with peripheral devices. Its essential characteristics are:

- access to system resources, including memory;
- it can be written in assembly language;
- it gives a deep understanding of the "layer below".

Its limitations include that systems programs often cannot run in debugging mode.

**Computer organisation** refers to the operational units and how they are connected to realise the architecture. It involves the processor (ALU and registers), the memory and the I/O processor.

## Registers

Registers are the fastest storage, at the **top of the memory hierarchy**, holding data and instructions the CPU needs immediately. The hierarchy runs registers → cache → main memory → magnetic disk → optical disk → magnetic tape.

- Going **up**, cost per bit increases.
- Going **down**, capacity and access time increase.

The hierarchy is based on **locality of reference**: a program tends to access the same set of memory locations, or nearby ones, over a short period.

Registers perform **fetch** (take instructions from memory), **decode** (interpret them) and **execute** (carry them out). The main registers are:

- **Accumulator (AC):** stores results produced by the system.
- **Data register (DR):** temporarily stores data sent to or from a peripheral.
- **Address register (AR):** holds memory addresses of data and instructions.
- **Program counter (PC):** the instruction pointer; the address of the next instruction.
- **Memory data register (MDR):** data written to or read from memory, paired with the MAR.
- **Index register:** modifies operand addresses.
- **Memory buffer register (MBR):** contents read from or written to memory.

Registers are **user-visible** (general purpose, address, segment pointers, index, stack pointer) or **control and status** registers (MAR, MBR and the **program status word**). The PSW's flags are sign, zero, carry, equal, overflow, interrupt enable/disable and supervisor.

## Ports

A **port** is a point of connection between the computer and its peripherals.

- **Serial ports** send data one bit at a time over one line: DB-25 was the original RS-232 port, and **DE-9** (often miscalled DB-9, also the COM port) became the main one.
- **Parallel ports** send several bits at once over several lines, like the 36-pin Centronics printer port.

Other ports include:

- **PS/2** (IBM, for mouse and keyboard);
- audio (3.5 mm TRS, S/PDIF/TOSLINK);
- video (VGA with 15 pins, DVI-I/DVI-D/DVI-A, Mini- and Micro-DVI, Display Port, RCA, component, S-Video, HDMI with 19 pins);
- **USB** (Type-A, Type-C with 24 pins);
- **RJ-45** (8-pin Ethernet) and RJ-11 (telephone);
- e-SATA.

Source: CSC 334- Systems Programming - new1.docx (course book), Unit 1 (systems programming, registers, memory hierarchy, ports) and Unit 2 (serial, parallel, audio, video, USB and network ports)
