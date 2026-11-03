# Sorting I: Bubble, Selection and Insertion Sort

## Why sorting matters

Arranging data in a required order is **sorting**, and many computer scientists consider it **the most fundamental problem in the study of algorithms**:

1. The need to sort is sometimes inherent in an application: banks sort cheques by number to prepare statements.
2. Algorithms often use sorting as a **key subroutine**, as when rendering layered graphical objects.
3. There is a wide variety of sorting algorithms using a rich set of techniques.
4. Sorting has a provable **lower bound**, and the best algorithms match it, so they are asymptotically optimal.
5. Many engineering issues arise in implementing sorting: the fastest program depends on prior ordering, memory and the software environment.

## Bubble sort

**Bubble sort** works by **repeatedly swapping adjacent elements** that are out of order: the elements are arranged by **forming pairs of adjacent elements** and interchanging them where needed, so the largest value "bubbles" to the end. Sorting n elements takes **n − 1 passes**: the first pass compares n − 1 pairs, the second n − 2, and the last just one. The total number of comparisons is (n − 1) + (n − 2) + … + 1 = n(n − 1)/2, so the order of the algorithm is **O(n²)**.

## Selection sort

**Selection sort** sorts n numbers in an array A by first **finding the smallest element** and exchanging it with A[1], then finding the second smallest and exchanging it with A[2], and so on for the first n − 1 elements. It also makes about n²/2 comparisons, so it is O(n²).

## Insertion sort

**Insertion sort** is one of the simplest sorting algorithms. It works the way we might sort a pile of cancelled cheques by hand: remove one cheque at a time from the unsorted pile and **insert it at the proper position** among the sorted ones. Formally, it takes one element at a time from the unsorted set and inserts it into the sorted part by scanning that part to find where it belongs. Although it may seem to need space for two sets, it actually **sorts in place**. Its best case is an already sorted list, where each element needs one comparison, giving linear time; its worst case, a reversed list, is O(n²).

These three techniques are **iterative**, and they are slow when the data are large; for 500 random items their running times can be compared directly in a practical exercise.

Source: CSC_236_Introduction_to_Algorithm.pdf (CSC 236 course book), Unit 3 (Sorting Techniques I) and Unit 8 (Run Time Analysis of Insertion Sort)
