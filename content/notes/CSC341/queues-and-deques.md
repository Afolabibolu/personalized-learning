# Queues and Deques

## The queue

A **queue** is an abstract data structure that is open at both ends and follows **FIFO** (First In, First Out): the item stored first is accessed first, like a single-lane one-way road or a queue at a ticket window. One end, the **rear**, is used to insert data and the other, the **front**, to remove it.

| Operation | Meaning |
| --- | --- |
| enqueue() | add an item at the rear; if the queue is full, **overflow** |
| dequeue() | remove the item at the front; if the queue is empty, **underflow** |
| peek() / Front | return the front item |
| Rear | return the last item |
| isfull(), isempty() | test the state |

With a one-dimensional array, the queue is full when rear reaches MAXSIZE − 1, and empty when front is below the minimum or front > rear.

**Enqueue:** check whether the queue is full; if it is, report overflow and exit; otherwise increment rear and store the data at queue[rear].

**Dequeue:** check whether the queue is empty; if it is, report underflow and exit; otherwise read queue[front], increment front and return the data.

## Circular queue

In a simple array queue, space freed at the front cannot be reused. A **circular queue** joins the end of the array to the start, so rear moves to (rear + 1) mod size and the freed positions are used again. The practicals ask for a fixed-size circular queue with enqueue, dequeue, isFull and isEmpty.

## Deque

A **deque** (double-ended queue) allows insertion and deletion at both ends; the practicals append numbers to its right and left ends. Two restricted forms:

- **Input-restricted deque:** insertion at one end only, deletion at both ends.
- **Output-restricted deque:** deletion at one end only, insertion at both ends.

## Priority queue

In a **priority queue** each item has a priority and the highest-priority item is served first, whatever its arrival order.

## Applications

Queues suit work that must be processed in order but not immediately: CPU and disk scheduling, a shared printer, asynchronous data transfer (I/O buffers, pipes, file I/O), call-centre phone systems, interrupts in real-time systems, and breadth-first search.

Source: CSC 341(Data structure).pdf, pages 31–37 (queue operations, algorithms and applications); CSC 341 ALL PRACTICALS AND SOLN.pdf (queue, deque and circular-queue practicals); restricted deques and priority queues are general knowledge, following the CSC 341 past papers (2023/24 and 2024/25 papers)
