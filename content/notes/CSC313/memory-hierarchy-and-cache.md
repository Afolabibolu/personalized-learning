# Memory Hierarchy and Cache

## The memory hierarchy

The **memory hierarchy** organises memory to minimise access time. It is based on **locality of reference**. Its levels are:

1. **registers**;
2. **cache memory**;
3. **main memory**;
4. **secondary memory** (magnetic disk, then optical disk and magnetic tape).

It is divided into **internal (primary) memory** (registers, cache and main memory, directly accessible by the processor) and **external (secondary) memory**. Its characteristics are:

- **Capacity:** increases from top to bottom.
- **Access time:** increases from top to bottom.
- **Performance:** it narrows the speed gap between registers and main memory.
- **Cost per bit:** increases from bottom to top, so internal memory costs more than external.

## ROM

**Read-only memory** holds **firmware**.

- **Mask ROM** is written at manufacture.
- **PROM** (one-time programmable) is written once with a PROM programmer.
- **EPROM** is erased with **ultraviolet light** through a quartz window, and lasts over 1000 erase cycles.
- **EEPROM** is erased **electrically** without removing the chip, but writing is slow.
- **EAROM** can be modified one bit at a time.
- **Flash memory** (1984) is a type of EEPROM that erases and rewrites faster.

## RAM

**Random-access memory** is the main memory that the CPU reads and writes directly. It is **volatile**: data is lost when power goes off.

- **SRAM (static RAM):** each cell is a latch of transistors (two cross-coupled inverters) that holds data while power is applied. It is **fast but expensive**, and is used for cache.
- **DRAM (dynamic RAM):** each cell stores a charge on a **capacitor** with one transistor, which leaks and must be **refreshed** periodically. It is cheaper and denser, and makes up main memory.

**SDRAM** is synchronised with the CPU's clock, so it has no wait states.

## Cache memory

**Cache** is very fast memory acting as a buffer between the CPU and RAM, in levels L1, L2 and L3.

**Locality of reference** is a program's tendency to reuse the same or nearby locations, as in loops.

- **Temporal locality:** data just used is likely to be used again soon, so it is kept in the cache.
- **Spatial locality:** data near the current location is likely to be needed, so neighbouring words are brought in too.

Finding data in the cache is a **cache hit**; otherwise it is a **cache miss**. Performance is measured by the **hit ratio** = hits ÷ (hits + misses). With hit ratio h, cache time Tc and main-memory time Tm, the average access time can be written h × Tc + (1 − h) × (Tc + Tm).

**Cache mapping** decides where a main-memory block goes:

- **direct mapping:** each block has one fixed cache line;
- **associative mapping:** a block can go anywhere;
- **set-associative mapping:** a block can go anywhere within one set.

Source: CSC 313-Computer Organization and Architecture.pdf (course material, T. Oguntunde), Unit 12b (memory hierarchy, ROM types, RAM) and Unit 13 (SRAM, DRAM, cache memory, locality of reference, hit ratio, cache mapping)
