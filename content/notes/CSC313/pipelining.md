# Pipelining and Pipeline Hazards

## The idea

There are two ways to speed up a processor: faster circuits, or arranging the hardware so that **more than one operation is performed at the same time**. Since faster circuits are costly, processors use **pipelining**: the arrangement of the CPU's hardware so that its overall performance increases, like an **assembly line**.

In a bottle plant with three one-minute stages (insert, fill, seal), each bottle takes three minutes without pipelining. With pipelining, after the first, **a new bottle comes out every minute**. Stages are joined by **interface registers** on a common clock, and execution is drawn as a **space-time diagram**.

## The five RISC (MIPS) stages

1. **IF:** instruction fetch, from the address in the PC.
2. **ID:** instruction decode and register read.
3. **EX:** execute, or calculate an address.
4. **MEM:** read or write memory operands.
5. **WB:** write the result back to a register.

## Execution time and speedup

For a k-stage pipeline with cycle time Tp and n instructions:

- pipelined time = **(k + n − 1) × Tp**;
- non-pipelined time = **n × k × Tp**;
- **speedup S = n k ÷ (k + n − 1)**, which approaches **k** as n grows.

The ideal pipelined CPI is 1.

In a **uniform delay pipeline**, all stages take the same time, so Tp = stage delay (+ buffer delay). In a **non-uniform** pipeline, **Tp = the maximum stage delay**: with stages of 2, 8, 3 and 10 ns, Tp = 10 ns.

## Hazards (dependencies)

A **stall** is a cycle in which no new instruction is started.

- **Structural hazards:** two instructions need the same hardware resource at once, such as a single memory. They are reduced by duplicating resources, for example separate instruction and data memories.
- **Data hazards:** an instruction needs a result that an earlier instruction has not yet produced. The types are:
  - **RAW** (read after write, a true dependency);
  - **WAR** (write after read);
  - **WAW** (write after write).

  For example, ADD R3 ← R1, R2 followed by SUB R4 ← R3, R1 is a RAW dependency on R3. **Operand forwarding (bypassing)** passes the result straight from the EX stage to the next instruction, removing most stalls.
- **Control hazards (branch hazards):** after a BRANCH, CALL or JMP, the processor does not know the next address until the branch is resolved. Stalls, branch prediction and delayed branches reduce them.

## Faster pipelines

- **Super-pipelining** divides the pipeline into more, shorter stages to raise the clock rate.
- **Superscalar** processors have several pipelines in parallel, for example for integer and floating-point instructions, issuing more than one instruction per cycle.

Source: CSC 313-Computer Organization and Architecture.pdf (course material, T. Oguntunde), Unit 11 (pipelining, the bottle and laundry examples, the five RISC stages, speedup, dependencies), Unit 12a (pipeline types and cycle time) and Unit 13 (super-pipelining and superscalar); RAW, WAR and WAW follow the 2020/21 paper (Question 2c)
