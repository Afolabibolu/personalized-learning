# Virtual Memory

## The idea

**Virtual memory** gives users the impression that their whole program is in main memory throughout processing, as if memory were unlimited. Job size is no longer limited by main memory, memory is used more efficiently, multiprogramming increases, external fragmentation is eliminated, and code and data can be shared. The costs are more hardware, overhead for page interrupts and complex software to prevent **thrashing**.

## Paged memory allocation

Each job is divided into **pages** of equal size, and memory into **page frames** of the same size; any page can go in any frame. Pages stay logically contiguous though frames are not. Three tables track this:

- **Job Table (JT):** for each active job, the size and location of its page map table.
- **Page Map Table (PMT):** one per job; each page number and its frame address.
- **Memory Map Table (MMT):** one per system; each frame's location and free or busy status.

Internal fragmentation remains, but only on a job's last page. The whole job must still be loaded.

## Demand paging

**Demand paged memory management (DPMM)** loads only the pages needed. **Swapping** moves pages between secondary storage and memory. The PMT gains fields for whether a page is in memory, whether it was **modified** (so it must be written back) and whether it was **referenced** recently. When a needed page is absent, a **page fault** occurs and the **page interrupt handler** loads it, choosing a page to swap out if all frames are busy.

Efficiency depends on **locality of reference**: **temporal** (a referenced location is soon referenced again) and **spatial** (nearby locations are soon referenced). A job's **working set** is the set of pages in memory it can use without a page fault.

## Page replacement policies

- **FIFO:** removes the page that has been in memory longest.
- **LRU (least recently used):** removes the page not referenced for the longest time.
- Others: optimal (the page not needed for the longest time in future), random, least frequently used, **NUR** (not used recently, a cheap approximation of LRU), working set and page fault frequency.

## Segmentation

**Segmented memory management** divides a job into logical **segments** of different sizes, such as a subroutine, tracked by a **Segment Map Table** (segment numbers, lengths, access rights, status). It supports **dynamic linking** (load a subroutine's segment only when referenced) and **shared segments** (one copy of a common procedure for many jobs), but variable-size segments are hard to manage. **Segmented/demand-paged** memory divides each segment into pages, combining the logical benefits of segments with the physical benefits of paging.

Source: Operating System CSC 421 for DLC2.docx (Ibadan Distance Learning Series, CSC 421 Operating System II), Unit 3
