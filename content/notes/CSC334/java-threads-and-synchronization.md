# Java Threads and Synchronization

## Thread states

At any time a Java thread is in one of several states:

- **New:** the thread's life begins here, and it stays here until the program starts it, which makes it runnable.
- **Runnable:** executing its task. To the OS this hides two states, **ready** and **running**; giving a ready thread a processor is **dispatching** it.
- **Waiting:** waiting for another thread to perform a task; it returns to runnable when signalled.
- **Timed waiting:** waiting for a set interval, for example while **sleeping**. It returns to runnable when the interval expires or the event occurs. A thread sleeps when it momentarily has no work, rather than looping and wasting processor time.
- **Terminated:** it completed its task or ended through an error.

## Scheduling

Each thread runs for a **quantum (time slice)**. The **thread scheduler** decides which thread runs next, keeping the highest-priority thread running and sharing the processor **round robin** among threads of equal priority.

- Java priorities run from **MIN_PRIORITY (1)** to **MAX_PRIORITY (10)**, with NORM_PRIORITY (5) as the default.
- When a higher-priority thread becomes ready, the running thread is **pre-empted**.
- Low-priority threads can suffer **starvation** (indefinite postponement).

## Executors

The preferred way to create threads is to implement **Runnable** (whose single method is **run**) and pass the task to an **Executor**'s execute method. An executor manages a **thread pool**. ExecutorService adds life-cycle methods such as **shutdown**, and Executors.newFixedThreadPool(3) creates one with three threads.

## Synchronization with locks

When several threads share and modify an object, results can be wrong. **Synchronization** gives one thread at a time exclusive access, using a **Lock**, such as ReentrantLock.

- A **fairness policy** (constructor argument true) gives the lock to the **longest-waiting** thread, which avoids indefinite postponement but can greatly reduce efficiency, so it is needed only in extreme cases. With false, there is no guarantee which waiting thread gets the lock.
- A thread that cannot continue until a condition holds calls **await** on a **Condition**, and another thread wakes it with **signal** or **signalAll**.
- Calling these without holding the lock throws **IllegalMonitorStateException**.
- Always call unlock in a **finally** block, call await inside a loop that tests the condition, and never forget to signal.

**Deadlock** occurs when a waiting thread cannot proceed because it waits for another thread that is itself waiting for the first.

## Producer/consumer

A **producer** thread generates data and places it in a shared **buffer**, and a **consumer** thread reads it. Without synchronization, values can be lost or read twice. With a lock and conditions, every value is consumed exactly once.

Source: CSC 334- Systems Programming - new1.docx (course book), Unit 10 (thread priorities, scheduling, creating threads with executors, synchronization) and Unit 11 (producer/consumer with and without synchronization)
