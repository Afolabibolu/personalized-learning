# Memory Management: Early Systems

## The memory manager's job

The memory manager is in charge of main memory (RAM). System performance depends on how much memory is available and how well it is used. Memory management keeps track of each location's status, decides who gets memory and how much, chooses where to allocate it, and deallocates it.

Storage management strategies are of three kinds:

- **Placement:** where to put an incoming job (first fit, best fit, worst fit).
- **Replacement:** which job or data to remove to make room.
- **Fetch:** when to bring the next piece from secondary storage, either on **demand** or by **anticipating** what will be needed.

## Single contiguous allocation

The first scheme: one job is loaded completely into one contiguous region. It is simple, but memory is poorly used, the CPU is idle while the job waits for I/O, a job cannot be bigger than memory, and there is no multiprogramming.

## Fixed partitions

Memory is divided into **fixed (static) partitions** before any job runs, one job per partition; partition sizes change only when the system is restarted. More jobs run and memory is better used, but there is **internal fragmentation** (unused space inside a partition), and a large job must wait for a large partition.

## Dynamic partitions

Partitions are created as jobs arrive, and each job gets only the memory it asks for. The OS keeps a list of free areas and uses:

- **First fit:** the first free area big enough, with the free list sorted by memory location. Fast, but may not be the most efficient choice.
- **Best fit:** the free area closest in size to the job. Wastes less memory per allocation, but leaves many tiny slivers.
- Also **next fit** (search from the last allocated block) and **worst fit** (the largest free block).

Dynamic partitions suffer **external fragmentation**: free space split into pieces too small to use.

## Relocatable dynamic partitions

The memory manager **relocates** programs to gather the empty blocks into one large block: **compaction**. Everything waits while it runs, and every address in the moved programs must be corrected. Two registers help:

- **Bounds register:** the highest (or lowest) location a program may access, so it cannot go out of bounds.
- **Relocation register:** the value added to each address so the program reaches the right location after it has been moved (zero if not moved).

Compaction removes fragmentation and allows more multiprogramming, but the hardware costs more and compaction time can be large.

All these schemes need the whole program loaded, stored contiguously, and kept in memory until the job finishes.

Source: Operating System CSC 421 for DLC2.docx (Ibadan Distance Learning Series, CSC 421 Operating System II), Unit 2
