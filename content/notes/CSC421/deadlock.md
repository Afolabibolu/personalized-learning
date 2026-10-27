# Deadlock, Starvation and Race Conditions

## Deadlock

**Deadlock** (the "deadly embrace") is a system-wide tangle of resource requests: two or more jobs are on hold, each waiting for a resource held by another job that is also waiting. It is more serious than starvation because it affects more than one job and ties up the whole system.

Deadlock needs **four conditions at the same time**:

1. **Mutual exclusion:** only one process may use a dedicated resource.
2. **Resource holding:** a process holds a resource while waiting for another.
3. **No preemption:** a resource cannot be taken back temporarily.
4. **Circular wait:** each process waits for another to release a resource.

## Seven cases

Deadlocks can occur on **file requests**, in **databases** (two processes each lock a record the other needs), in **dedicated device allocation** (two tape drives), in **multiple device allocation**, in **spooling**, in **disk sharing** and in a **network** without flow control.

## Modelling with directed graphs

Processes are drawn as circles and resources as squares. A line from a resource to a process means the process holds it; a line from a process to a resource means it is waiting for it. A **cycle** in the graph shows a deadlock.

## Strategies

- **Prevention:** remove one of the four conditions. Mutual exclusion is usually necessary. **Resource holding** is removed by requesting every resource at the start; **no preemption** by letting the OS take resources back; **circular wait** by **Havender's** solution (1968), numbering resources and requesting them in ascending order.
- **Avoidance:** if the OS knows each job's requests in advance, it avoids unsafe states with **Dijkstra's Banker's algorithm**. In a **safe state** there is a sequence that lets every job finish; an **unsafe state** is not yet deadlock but is a candidate for it. The algorithm's drawbacks: jobs must state their maximum needs, resources and the number of jobs must stay fixed, it is costly, and it under-uses resources.
- **Detection:** reduce the directed graph by removing processes that are not waiting or whose requests can be met; if a cycle remains, there is deadlock.
- **Recovery:** choose a **victim**, for example terminate all jobs, only the deadlocked ones, or one at a time; restart from a snapshot; preempt a resource; or stop new jobs. The victim chosen should have the least negative effect (low priority, little CPU time used, few jobs affected).

## Starvation and race conditions

**Starvation** happens when conservative allocation keeps one job waiting forever for resources that never become available. A **race condition** happens when two processes compete for the same resource, for example a read and a write at the same time; serializing access prevents it. A race is **critical** if it changes the end state of the system and **noncritical** if it does not.

Source: Operating System CSC 421 for DLC2.docx (Ibadan Distance Learning Series, CSC 421 Operating System II), Unit 6
