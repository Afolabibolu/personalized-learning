# Microcomputer and Microprocessor Basics

## The microcomputer

Computers are classed as **supercomputers**, **mainframes**, **minicomputers** and **microcomputers**. A microcomputer has four basic blocks:

- **Input unit:** accepts coded information, for example from a keyboard, mouse or scanner.
- **Memory unit:** **primary memory** (RAM) holds the programs and data being executed, organized in words with an address each, with access times of 10 to 100 ns; **secondary memory** (hard disk, CD, tape) stores large amounts of data.
- **Processor:** the **ALU** performs arithmetic and logic, using fast **registers** (5 to 10 times faster than memory), and the **control unit** coordinates all units and generates timing and synchronization signals.
- **Output unit:** decodes binary data for the outside world, for example a printer.

## Computer architecture

**Computer architecture** is the conceptual design and operational structure of a computer. It has three parts:

- **Instruction set architecture (ISA):** what a machine or assembly language programmer sees: instructions, addressing modes, registers and data formats.
- **Microarchitecture (computer organization):** how the parts are connected to implement the ISA.
- **System design:** buses, memory controllers and mechanisms such as DMA.

## Von Neumann and Harvard

- The **von Neumann architecture** uses a processing unit and a **single storage** for both instructions and data. Sharing one path between them limits performance: the **von Neumann bottleneck**. Most microprocessor-based machines use it.
- The **Harvard architecture** has **separate memories** for instructions and data, named after the Harvard Mark 1. The two memories need not share characteristics, and separate channels allow instruction and data access at the same time. It suits embedded applications, though most Harvard machines still connect memory through a single bus.

## The microprocessor

A **microprocessor** is a VLSI single-chip implementation of a CPU: a programmable chip with computing and decision-making ability. Intel introduced the first, the **4004**, in 1971. Key terms:

- **Bit:** one binary digit. **Word:** the data size the ALU processes at once.
- **Address bus:** carries the address of a memory location or I/O port; unidirectional.
- **Data bus:** carries data between processor, memory and I/O; bidirectional, and an 8-bit processor generally has an 8-bit data bus.
- **Control bus:** carries control signals.

**Manufacturing technologies** are Transistor-Transistor Logic (**TTL**), Emitter Coupled Logic (**ECL**) and Complementary Metal-Oxide Semiconductor (**CMOS**). Microprocessors are **classified** as 4-, 8-, 16- or 32-bit, and by architecture:

- **CISC:** many complex instructions.
- **RISC:** fewer, simpler instructions that execute faster, as in Apple's PowerPC.
- **VLIW** (very long instruction word) and **superscalar** processors, which issue several instructions at once.

**Factors in choosing a microprocessor** include the **word size**, set by the length of the internal registers, and the clock speed.

Source: CSC 412 MICROPROCESSOR INTERFACING.pdf (CSC 412 course material, Adebola K. Ojo), Study Sessions 1 to 4
