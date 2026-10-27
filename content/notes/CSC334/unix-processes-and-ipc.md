# Unix Processes, Signals and IPC

## Creating processes: fork, exec and vfork

In Unix, **fork()** creates a new process by duplicating the caller. It returns **0 in the child** and the **child's process ID in the parent**. **exec()** (execl, execvp and others) replaces the calling process's program with a new one.

Together they give modular execution: a shell forks a child and the child execs the command, while the parent waits. Daemons and servers fork a child for each task or client.

**vfork()** creates a child that **shares the parent's address space**, with the parent suspended until the child calls exec or exits. It avoids copying, so it is faster when the child will exec at once, but it is risky if the child changes memory. Modern fork() uses copy-on-write, which narrows the gap.

## The process lifecycle

A process is created by fork(), becomes **ready**, **runs**, may **wait** (block) for I/O, and finally **terminates** with exit().

- Until its parent collects its exit status with **wait()**, a terminated process remains a **zombie**.
- A child whose parent dies first becomes an **orphan** and is adopted by init.

The OS schedules processes, allocates their memory and resources, and reclaims them at termination.

## Signals

A **signal** is an asynchronous notification sent to a process, such as SIGINT (Ctrl-C), SIGTERM, SIGKILL or SIGCHLD (a child ended). A process can ignore a signal, take the default action, or catch it with a **handler**; SIGKILL and SIGSTOP cannot be caught.

- **Benefits:** a simple, lightweight way to interrupt, stop or notify processes.
- **Limitations:** signals carry almost no data, can arrive at any moment and cause race conditions, and handlers may only safely call async-signal-safe functions.

## Inter-process communication (IPC)

- **Pipes:** unidirectional byte streams between related processes (parent and child), as in `ls | wc`.
- **Named pipes (FIFOs):** pipes with a name in the file system, usable by unrelated processes.
- **Message queues:** processes send and receive discrete messages.
- **Shared memory:** two processes map the same memory region; it is the **fastest** IPC, because data is not copied, but access must be synchronized, usually with **semaphores**.
- **Sockets:** communication on one machine (Unix domain) or across a network, the usual choice for **client-server** applications with real-time data exchange.

## C file handling and number conversion

In C, **fopen** opens or creates a file, **fprintf/fputs** write to it, **fgets/fscanf** read from it, **fclose** closes it, and **remove** deletes it.

A hexadecimal string converts to decimal by multiplying each digit by a power of 16. For example, 2ABC4₁₆ = 2×16⁴ + 10×16³ + 11×16² + 12×16 + 4 = 175,044.

Source: general knowledge, following the CSC 334 past papers (2024/25 paper, Section A and Questions 2 and 3); the CSC 334 course book does not cover Unix processes, signals or IPC
