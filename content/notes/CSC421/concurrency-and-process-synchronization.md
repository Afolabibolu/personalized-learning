# Concurrent Processing and Process Synchronization

## Multiprocessing

A **multiprogramming** system shares one CPU among several jobs; a **multiprocessing** system has several processors. In **parallel processing**, two or more processors execute instructions at the same time, which gives **increased reliability** (if one fails, others take over) and **faster processing**. Levels of parallelism range from multiple processes and threads down to pipelining, superscalar processing and multiple ALUs.

## Configurations

- **Master/slave (asymmetric):** a master processor manages all files, devices, memory and processors and schedules the slaves. Simple, but if the master fails everything fails, free slaves wait for the master, and interrupts increase.
- **Loosely coupled:** several complete computers, each with its own memory, I/O devices, CPU and OS. A job stays on the processor it was given. A single failure is not catastrophic, but it can be hard to detect.
- **Symmetric (tightly coupled):** processors share main memory and I/O devices, with one copy of the OS and decentralized scheduling. More reliable, better use of resources and load balancing, and it degrades gracefully, but it needs careful synchronization.

## Critical regions and mutual exclusion

A **critical region** is a part of a program that must complete before other processes may use the same resource. Synchronization works like a lock and key: test whether the key is free and take it, in **a single machine cycle**, to enforce **mutual exclusion**.

- **Test-and-set (TS):** an indivisible IBM 360/370 instruction that tests a condition code and sets it to busy. Simple, but can cause **starvation** and **busy waiting**.
- **WAIT and SIGNAL:** WAIT blocks a process and queues it when the region is busy; SIGNAL wakes one waiting process when the region is freed, removing busy waiting.
- **Semaphores** (Dijkstra, 1965): a non-negative integer flag with two indivisible operations, **P** (proberen, test: if s > 0 then s := s − 1) and **V** (verhogen, increment: s := s + 1). A semaphore used for mutual exclusion is called **mutex**.

## Process cooperation

- **Producers and consumers:** one process produces data another consumes, for example CPU output to a slower printer, using a buffer with semaphores for full and empty positions and a mutex.
- **Readers and writers:** many readers may share a resource when no writer is active; a writer needs exclusive access, as in an airline reservation system.

## Concurrent programming

A language can mark statements that may run at the same time, with **COBEGIN** and **COEND**. The expression A = 3 * B * C + 4 / (D + E) ** (F − G) takes seven steps serially but four with concurrent processing. Concurrency also speeds array operations, matrix multiplication, database searches and sorting, though not in direct proportion to the number of processors.

Source: Operating System CSC 421 for DLC2.docx (Ibadan Distance Learning Series, CSC 421 Operating System II), Units 4, 5 and 12; Parallelism.pptx
