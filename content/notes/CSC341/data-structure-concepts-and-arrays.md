# Data Structure Concepts and Arrays

## What a data structure is

A **data structure** is a way of organising data in memory so that it can be stored, retrieved and changed efficiently. **Primitive** data types are built into the language (integer, float, character, boolean). **Non-primitive** structures are built from them: arrays, lists, stacks, queues, trees and graphs.

## Linear and non-linear structures

- **Linear:** elements are arranged in a sequence, each attached to its previous and next element, so all of them can be traversed in a single run. Examples: array, stack, queue, linked list. Implementation is easy, but memory is used less efficiently.
- **Non-linear:** elements are attached hierarchically across several levels and cannot be traversed in a single run. Examples: trees and graphs. They are harder to implement but use memory more efficiently.

A **static** structure has a fixed size set before the program runs (an array); a **dynamic** structure grows and shrinks at run time (a linked list). **Data abstraction** means describing a structure by its operations, not its implementation (an abstract data type such as a stack with push and pop). **Encapsulation** hides the stored data inside the structure so it can only be reached through those operations.

## Arrays

An **array** is a collection of items of the same type stored at **contiguous memory locations**. The position of any element is found by adding an offset to the **base address** (BA), the location of the first element.

For a two-dimensional array A(l1:u1, l2:u2):

- **Number of elements** = (u1 − l1 + 1) × (u2 − l2 + 1). For example, P(1:4, 1:6) has 4 × 6 = 24 elements.
- **Row-major order** (row by row): address of A(i, j) = BA + w × [(i − l1)(u2 − l2 + 1) + (j − l2)], where w is the element size.
- **Column-major order** (column by column): address of A(i, j) = BA + w × [(j − l2)(u1 − l1 + 1) + (i − l1)].

Worked example: A(1:7, 1:10) stored by rows with BA = 0 and w = 1. A(5, 7) is at 0 + 1 × [(5 − 1) × 10 + (7 − 1)] = 46.

## Array operations

- **Traversing:** visiting every element once.
- **Insertion and deletion:** shifting elements to make or close a gap.
- **Searching and sorting.**
- **Merging:** combining two arrays into one.
- **Concatenation:** joining one array to the end of another.
- **Copying:** creating a duplicate array.

Source: CSC 341(Data structure).pdf, pages 1–3 (linear and non-linear structures, arrays); primitive types, abstraction and the addressing formulas are general knowledge, following the CSC 341 past papers (2022/23, 2023/24 and 2024/25 papers)
