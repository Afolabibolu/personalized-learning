# Processes, Threads and Concurrency

## Tracking processes

The OS keeps key data structures to track processes:

- a **process list** of all ready processes;
- a record of which process is running;
- a record of blocked processes, so that when an I/O event completes it wakes the right one.

The structure holding one process's information is the **process control block (PCB)**. For a stopped process it stores the register context; restoring those registers resumes the process, which is a **context switch**.

## Process life cycle

A process is **created**, **executed** and **terminated**. Creation requires four actions:

1. set up the process description (a PCB);
2. allocate an address space;
3. load the program into it;
4. pass the description to the process scheduler.

During execution a process is **ready**, **running** or **waiting**, and finally **terminated**. Systems may also have an initial state, and a final **zombie** state: the process has exited but its parent has not yet called wait(). Scheduling may be preemptive or non-preemptive.

## Threads

A **thread** is a lightweight process. Each has its own **program counter, registers and stack**, which identify it. Threads have three advantages over processes:

1. less time to create and terminate;
2. less time to switch between threads of the same process;
3. less communication overhead, since they share the address space.

- **User-level threads** are created and managed by users at the application level, with no OS involvement.
- **Kernel-level threads** are implemented by the OS and take longer.

They are related by the **many-to-many**, **many-to-one** and **one-to-one** models.

## Concurrent and parallel execution

- **Concurrent execution** follows the N-client, 1-server model: only one client is served at any moment, as threads are interleaved on one processor.
- **Parallel execution** follows the N-client, N-server model: several are served at the same time, each thread on its own processor.

Parallelism can come from the hardware without explicit concurrency in the language. **Granularity** is the amount of computation done in parallel relative to the whole program.

ADA made concurrency primitives available, and Java offers concurrency through its APIs.

## Multithreading

**Uses:**

- processing large data in parts;
- validate-and-save or produce-and-consume tasks;
- games;
- background API calls in Android;
- asynchronous calls in web applications.

**Benefits:** economy, resource sharing, responsiveness and scalability. A downloading video can be played while it is still downloading, with one thread fetching the data and another playing it back.

Source: CSC 334- Systems Programming - new1.docx (course book), Unit 9 (process list, PCB, process life cycle, threads, concurrent and parallel execution, granularity, multithreading); the video-download example follows the 2020/21 questions copied in the CSC 334 answer file
