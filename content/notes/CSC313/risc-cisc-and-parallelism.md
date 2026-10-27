# RISC, CISC and Parallel Processing

## CISC

The goal of a **complex instruction set computer (CISC)** is to provide a single machine instruction for each high-level statement. Examples are the **DEC VAX** and **IBM 370**. Its characteristics are:

- a large number of instructions (100 to 250);
- some instructions for special tasks used infrequently;
- a large variety of addressing modes (5 to 20);
- variable-length instruction formats;
- instructions that manipulate operands in memory;
- control by a **microprogram**, which is complex to design.

## RISC

The **reduced instruction set computer (RISC)** tries to cut execution time by simplifying the instruction set. Its characteristics are:

- relatively few instructions and few addressing modes;
- memory accessed only by **load and store**, with all other operations in registers;
- **fixed-length**, easily decoded instruction formats;
- **single-cycle** instruction execution;
- **hardwired** rather than microprogrammed control;
- many registers and an efficient **pipeline**.

RISC processors often achieve 2 to 4 times the performance of CISC processors, use less chip space and are simpler to design. Some use **overlapped register windows**, so each procedure has its own bank of registers and saving and restoring is not needed.

The **Berkeley RISC I** was a 32-bit CPU with a 32-bit instruction format, 31 instructions and three addressing modes: register, immediate and PC-relative.

## Why parallel processing

A serial computer's speed is limited by how fast data move through its hardware. **Parallel processing** executes a task split across several processors at once, solving large problems in hours instead of years. Pipelining appeared in the CDC 7600 (1969), followed by Cray vector supercomputers.

A **program** is a passive set of instructions; a **process** is a program in execution; a **thread** has its own program counter and registers but shares the process's memory.

## Flynn's taxonomy (1966)

Flynn classified computers by their **instruction streams** and **data streams**:

- **SISD:** one processor, one instruction stream, one data stream; sequential machines.
- **MISD:** several processors with different algorithms on the same data; few real examples.
- **SIMD:** several processors following the same instructions on different data.
- **MIMD:** several processors, each with its own instructions and data; the most flexible.
- **SPMD:** a subset of MIMD that runs the same program on all processors.

SIMD and MIMD are the most common. Networked SISD machines working together form **grid computing**.

## Amdahl's law and granularity

**Amdahl's law** limits speedup by the fraction P of code that can be parallelised:

**Speedup = 1 ÷ ((1 − P) + P ÷ N)** for N processors.

If P = 0 the speedup is 1; if 50 percent can be parallelised, the maximum speedup is 2. **Granularity** is the amount of computation done in parallel relative to communication.

Source: CSC 313-Computer Organization and Architecture.pdf (course material, T. Oguntunde), Unit 8 (CISC, RISC, register windows, Berkeley RISC I), Unit 9 (parallel processing, programs, processes, threads, granularity) and Unit 10 (Amdahl's law, Flynn's taxonomy)
