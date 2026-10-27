# Process Management

## Processes

A **job** is a request submitted by a user. When it takes hold of the processor it becomes a **process**: a program loaded into memory and in execution. Each process has its own address space, holding its instructions and data.

When a program starts, the **high-level scheduler** loads it and creates a **process control block (PCB)**. The OS also keeps a **process table** listing every process by its unique **process identification number (PID)**, with the address of its PCB.

## Process states

The simple model has three states:

- **Ready:** waiting for a processor.
- **Running:** being executed; only one process at a time on a uniprocessor.
- **Blocked:** waiting for an event such as I/O.

Processes enter in the ready state, reach running only from ready, and normally leave from running. The book's five-state model adds **ready suspended** and **blocked suspended**, for processes swapped out of memory. The five-state diagram is also often drawn as new, ready, running, waiting and terminated.

A **system timer** stops one process from monopolising the processor. When its time is up, an interrupt returns control to the OS, which moves the process from running to the back of the ready queue and dispatches the next one. A running process also leaves the processor if it requests I/O (becoming blocked) or is pre-empted by a higher-priority request. When the I/O completes, the blocked process returns to ready.

## The process control block

Every process has a PCB, the data structure the OS uses to manage it. It holds:

- **process identification**;
- **process status** (ready, running, blocked);
- the **process status word** (instruction counter);
- **register contents**;
- the **main memory address**;
- the **resources** allocated;
- **process priority**;
- **accounting information** (CPU time used, total time in the system, storage occupancy).

## Context switching

A **context switch** saves the running process's information in its PCB and loads the next process's PCB into the registers so it can run. Preemptive algorithms must context switch often.

## Levels of scheduling

- **Long-term (high-level) scheduler:** decides which jobs are admitted to the system, and so controls the **degree of multiprogramming**. It should admit a balanced mix of I/O-bound and CPU-bound jobs.
- **Medium-term scheduler:** handles **swapping**: it moves inactive or blocked processes out to virtual memory (a suspend queue) and back, which can correct an imbalanced mix.
- **Short-term (low-level) scheduler, or dispatcher:** chooses which ready process runs next whenever the running process stops. It is essential in preemptive scheduling, where switches are frequent.

Source: CSC 321 DLC Final.pdf (Computer Operating System course book), Study Session 6 (process, states, PCB, context switch, process scheduling); new, ready, running, waiting and terminated as five states, and the I/O-bound mix point, are general knowledge, following the 2022/23 and 2024/25 papers
