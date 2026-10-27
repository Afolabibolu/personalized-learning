# Organization, Architecture and the Instruction Cycle

## Organization and architecture

**Computer architecture** is the set of attributes that directly affect the logical execution of a program: the instruction set, the number of bits used to represent data, I/O mechanisms and addressing techniques. **Computer organization** is the operational units and their interconnections that realise the architecture: control signals, interfaces and memory technology, details transparent to the programmer. Like a building, the architect plans what each part is for, and the engineer decides how it is built.

Studying both helps us design better programs and system software, evaluate (benchmark) performance, and understand time, space and price trade-offs.

## Functions and structure

A computer has four basic functions: **data processing, data storage, data movement** (I/O, or data communication over distance) and **control**. Its four main structural components are:

1. the **CPU**, which controls the computer and processes data;
2. **main memory**, which stores data;
3. **I/O**, which moves data to and from the outside world;
4. **system interconnection**, usually a **system bus**.

The CPU itself has a **control unit**, an **ALU**, **registers** and **internal interconnection**.

## Von Neumann and Harvard

Almost all computers follow the **von Neumann architecture** (Institute for Advanced Study, Princeton), based on three concepts:

1. data and instructions are stored in a **single read-write memory**;
2. memory contents are addressable by location, regardless of type;
3. execution is **sequential**, from one instruction to the next, unless modified.

Instead of rewiring hardware for each program, general-purpose hardware takes codes (instructions) as software. The **Harvard architecture** uses separate memories (today, separate caches) for instructions and data.

## The instruction cycle

The **program counter (PC)** holds the address of the next instruction; after each fetch it is incremented. The fetched instruction goes into the **instruction register (IR)**, and the processor performs one of four kinds of action: processor-memory, processor-I/O, data processing or control (changing the sequence).

**Example:** with 16-bit instructions (a 4-bit opcode and 12-bit address, so 2¹² = 4096 words), the program at locations 300–302 runs 1940 (load AC from 940), 5941 (add 941 to AC) and 2941 (store AC at 941).

The instruction cycle states are:

- instruction address calculation (iac);
- instruction fetch (if);
- instruction operation decoding (iod);
- operand address calculation (oac);
- operand fetch (of);
- data operation (do);
- operand store (os).

## Logic gates

Gates are the building blocks of digital systems:

- **AND** gives 1 only when all inputs are 1;
- **OR** gives 1 when any input is 1;
- **NOT** inverts;
- **NAND** and **NOR** are AND and OR followed by NOT;
- **XOR** gives 1 when exactly one of two inputs is 1;
- **XNOR** is its inverse.

Source: CSC 313-Computer Organization and Architecture.pdf (course material, T. Oguntunde), Unit 2 (organization and architecture, functions, structural components, von Neumann architecture) and Unit 3 (instruction fetch and execute, instruction cycle states, logic gates)
