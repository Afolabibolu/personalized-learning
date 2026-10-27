# CPU Scheduling

## The process scheduler

There are more jobs than processors, so the **short-term scheduler** picks a process from the ready queue whenever the processor becomes free. Its functions are:

1. keep track of the status of all processes;
2. decide which process gets the processor;
3. allocate the processor; and
4. deallocate it when necessary.


## Metrics

- **Arrival time:** when a process became ready.
- **Waiting time:** time spent waiting for the CPU.
- **Service (run) time:** time executing on the CPU.
- **Turnaround time:** waiting time plus service time, or finish time minus arrival time.
- **Response time:** how long the system takes to react to a request.

A good policy maximises **throughput** and CPU efficiency while minimising turnaround, waiting and response times.

**Preemptive** algorithms can take the processor away from a running process, which requires context switching. **Non-preemptive** algorithms let a process run until it finishes or waits.

## The algorithms

- **First-come, first-served (FCFS/FIFO):** non-preemptive; jobs run in arrival order. A long job makes short jobs wait, so turnaround depends on the arrival order and it suits interactive users poorly.
- **Shortest job next (SJN/SJF):** non-preemptive; the job with the shortest run time runs next. It lowers average turnaround and is optimal when all jobs are present and their CPU estimates are accurate. It suits batch systems, but long jobs may starve.
- **Shortest remaining time (SRT):** the preemptive version of SJN. A newly arrived job with a shorter remaining time pre-empts the running one, giving lower average turnaround than SJN.
- **Round robin (RR):** preemptive; processes are dispatched in FIFO order, each for a **time quantum**. If a process is not done when its quantum ends, it goes to the back of the queue. A very large quantum makes RR behave like FCFS; a small one is fair and responsive but must stay well above the context-switch time.
- **Priority scheduling (PS):** the highest-priority job runs first, with FCFS among equals. The book describes it as non-preemptive. Priorities are set by the administrator or by the processor manager from memory needs (high means low priority), total CPU time (long means low) and waiting time.

A low-priority job may be postponed indefinitely (**starvation**). **Aging** prevents this by raising a process's priority the longer it waits, until it exceeds incoming jobs.

## Worked FCFS example

| Job | Run time | Arrival | Start | Finish | Turnaround |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 h | 10:00 | 10:00 | 12:00 | 120 min |
| 2 | 1 h | 10:10 | 12:00 | 13:00 | 170 min |
| 3 | 30 min | 10:30 | 13:00 | 13:30 | 180 min |

Source: CSC 321 DLC Final.pdf (Computer Operating System course book), Study Session 8 (process scheduling, metrics, policies, FIFO, SJF, SRT, round robin, priority scheduling and the worked example)
