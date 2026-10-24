# Divide and Conquer

## What the topic is

Divide and conquer is an algorithmic paradigm that solves a problem in three steps:

1. **Divide** the problem into smaller sub-problems.
2. **Conquer** the sub-problems by calling the algorithm recursively until they are solved.
3. **Combine** the sub-problem answers into the solution of the whole problem.

## Standard divide-and-conquer algorithms

- **Quicksort** picks a pivot, moves smaller elements to its left and larger ones to its right, then sorts each side recursively.
- **Merge sort** divides the array into two halves, sorts them recursively and merges the sorted halves.
- **Closest pair of points** can be solved in O(n²) by checking every pair; divide and conquer solves it in O(n log n).
- **Strassen's algorithm** multiplies matrices faster than the O(n³) triple loop.
- **Cooley–Tukey FFT** runs in O(N log N).
- **Karatsuba's algorithm** multiplies two n-digit numbers with fewer single-digit products than the classical n² method. For n = 1024 it needs 3¹⁰ = 59,049 instead of 1,048,576.

## How merge sort works

Merge sort keeps splitting the array in half until each piece has one element, which is always sorted. It then merges the sorted pieces back into bigger sorted arrays. For example, {38, 27, 43, 10} is split into {38, 27} and {43, 10}, then into single elements. Those merge into {27, 38} and {10, 43}, and finally into {10, 27, 38, 43}.

**Complexity.** The recurrence is T(n) = 2T(n/2) + θ(n). It falls in case 2 of the master method, so merge sort is θ(n log n) in the best, average and worst case: it always halves the array and merges in linear time. It needs O(n) auxiliary space, because elements are copied into an auxiliary array.

**Applications:** sorting large datasets, external sorting (data too large for memory), custom sorting of partially sorted data, and the inversion count problem.

**Advantages:** it is stable (equal elements keep their order), its worst case is guaranteed O(n log n), and it is naturally parallelizable.

**Drawbacks:** it needs extra memory, it is not in-place, and it is not always optimal for small datasets, where insertion sort can be faster.

## Closest pair of points

Given n points in the plane, the task is to find the pair with the smallest distance. The points are sorted by x and by y and divided into two halves by a middle line. The smallest distance on each side is found recursively. A strip of points closer to the middle line than that distance is then checked, because the closest pair might straddle the line. When three or fewer points remain, every pair is compared directly. For the points (2, 3), (12, 30), (40, 50), (5, 1), (12, 10) and (3, 4), the minimum distance is 1.41421 units. The algorithm runs in O(n log n).

Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Session 2
