# Linked Lists

## Nodes and pointers

A **linked list** is a linear data structure made of **nodes**. Each node holds the **data** and a **pointer** (link) to the next node. The first node is reached through the **head** pointer, and the last node's pointer is NULL. Unlike an array, the nodes need not be next to each other in memory, so the list can grow and shrink while the program runs.

The course notes implement a stack with linked-list nodes (`struct StackNode` holding `data` and `next`, created with `malloc`). The notes give the trade-off: the linked-list version "can grow and shrink according to the needs at runtime" but "requires extra memory since it uses pointers".

## Kinds of linked list

- **Singly linked list:** each node points to the next node only; movement is one way.
- **Doubly linked list:** each node has three fields, a pointer to the previous node, the data and a pointer to the next node, so the list can be traversed in both directions.
- **Circular linked list:** the last node points back to the first instead of to NULL, so the list can be traversed from any node round to itself.

## Operations

- **Traversal:** follow the pointers from the head, visiting each node.
- **Insertion:** at the beginning (new node points to the old head, head moves to the new node), at the end, or at a given position by relinking pointers.
- **Deletion:** make the previous node point past the node being removed, then free it.
- **Search:** compare each node's data in turn.
- **Reversal:** walk the list, turning each node's pointer back towards the previous node, then make the old last node the head.

The practicals build a list, add 1, 2, 3 and 4, delete the node holding 3, and insert a value at a given position.

## Arrays compared with linked lists

| Array | Linked list |
| --- | --- |
| Fixed size, contiguous memory | Grows and shrinks, nodes anywhere in memory |
| Direct access to any element by index | Access by following pointers from the head |
| Insertion and deletion shift elements | Insertion and deletion relink pointers |
| No pointer overhead | Extra memory for each pointer |

Source: CSC 341(Data structure).pdf, pages 14–16 (linked-list stack); CSC 341 ALL PRACTICALS AND SOLN.pdf (linked-list practical); node kinds, operations and the comparison are general knowledge, following the CSC 341 past papers (2020/21, 2021/22 and 2023/24 papers)
