# Memory Management

## The memory manager

A program must be in **main memory** before the processor can execute it. The memory manager decides how memory is allocated to processes and responds to changing demands, protecting the OS and each process from the others. The OS itself always occupies a partition, because it is loaded first.

Before larger memories, programmers used **overlays**. They divided a program into sections, kept a small part in memory, and loaded the other sections only when needed, so the programmer, not the OS, managed memory.

## Single-user contiguous allocation

The first scheme: each program is loaded **in its entirety** into **contiguous** memory. A program too large for memory cannot run. It needs only a register for the base address and an accumulator for the program's size, and protection is simple. It supports only one job at a time, with no multiprogramming.

## Fixed partitions

Memory is divided into several partitions, of equal or different sizes, fixed when the system is switched on and changed only by restarting it. Each partition holds one process, so several jobs can be in memory at once. Each partition is protected by a **base register** and a **limit register**.

A job smaller than its partition wastes the rest of that partition, which no other job can use. This is **internal fragmentation**. A job larger than every partition must wait.

## Dynamic (variable) partitions

Each job is given exactly the memory it needs, which removes internal fragmentation. As jobs finish they leave **holes**, and new jobs are placed by one of three strategies:

- **First fit:** the first hole large enough; quick to decide.
- **Best fit:** the hole that fits most closely; leaves little space but small, unusable holes, and searching costs time.
- **Worst fit:** the largest hole; may leave room for another job.

Over time, small scattered holes called **slivers** build up between allocated areas. They are too small to use, because jobs must be contiguous. This is **external fragmentation**.

## Relocatable dynamic partitions

To use the slivers, the OS **relocates** partitions so that the free fragments are merged into one large block. This is **compaction** (defragmentation, or garbage collection), the scheme developed to eliminate fragmentation. It uses memory far more efficiently, but adds considerable overhead, and processes cannot run while compaction takes place.

All four schemes share three rules:

1. a process is loaded in its entirety;
2. into contiguous memory; and
3. stays there until it completes.

Later systems relax these rules with **virtual memory**.

Source: CSC 321 DLC Final.pdf (Computer Operating System course book), Study Session 9 (overlays, single-user contiguous, fixed, dynamic and relocatable dynamic partitions)
