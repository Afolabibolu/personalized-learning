# Threads and Multithreading

## What a thread is

A **thread** is a path of execution within a process. It has its own **program counter, registers, stack and state**, but shares the process's **code, data and open files** with the other threads of the same process. Because it has some properties of a process at a fraction of the cost, it is called a **lightweight process**. A traditional (heavyweight) process has a single thread of control.

**Examples:**

- A word processor may use one thread to check spelling, another to process keystrokes, another to load images and another to save backups.
- A web server uses a thread per request, so many users are served at once.
- Each browser tab can be a different thread.

Creating new threads in this way is sometimes called **spawning**.

## Benefits of multithreading

1. **Responsiveness:** one thread can respond quickly while others are blocked or busy calculating.
2. **Resource sharing:** threads share code, data and resources in a single address space.
3. **Economy:** creating threads and switching between them is much faster than for processes.
4. **Scalability:** a multithreaded application can spread across several processors, while a single-threaded process runs on only one CPU.

On a single-core chip the threads are interleaved (**concurrency**); on a multi-core chip they can run at the same time (**parallelism**).

## User and kernel threads

- **User threads** are supported above the kernel, without kernel support, by the application's thread library.
- **Kernel threads** are supported within the OS kernel itself; all modern OSes support them.

User threads must be mapped to kernel threads by one of three models:

- **Many-to-one:** many user threads map to one kernel thread. Thread management is efficient, but one blocking system call blocks the whole process, and the process cannot use several CPUs. Examples: Solaris green threads, GNU Portable Threads.
- **One-to-one:** each user thread gets its own kernel thread. This avoids those problems but adds overhead, so the number of threads is usually limited. Examples: Linux, Windows 95 to XP.
- **Many-to-many:** many user threads are multiplexed onto an equal or smaller number of kernel threads. There is no limit on threads, a blocking call does not block the whole process, and processes can be split across processors. A variation, the **two-tier model**, also allows one-to-one mapping.

## Thread libraries

A thread library gives programmers an API for creating and managing threads, in user space or kernel space:

- **POSIX Pthreads** (user or kernel level);
- **Win32 threads** (kernel level on Windows);
- **Java threads** (implemented with whichever library the JVM's host system uses).

Source: CSC 321 DLC Final.pdf (Computer Operating System course book), Study Session 6 (6.2.1) and Study Session 7 (threads, benefits, multithreading models, thread libraries); spawning is general knowledge, following the 2021/22 paper (Question 7)
