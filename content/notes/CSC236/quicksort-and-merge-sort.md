# Sorting II: Quicksort and Merge Sort

## Quicksort

The iterative sorts are slow for large data, so faster recursive algorithms are used. In **quicksort**, an array a[1..n] is sorted by **selecting some value in the array as a key (pivot) element**. The first element is swapped with the key so the key is at the start, and the list is **partitioned**: elements less than the key go to one side and greater ones to the other, after which each side is sorted recursively. Like merge sort, quicksort follows **divide and conquer**:

- **Divide**: partition A[p..r] into A[p..q − 1] and A[q + 1..r] around A[q].
- **Conquer**: sort the two subarrays by recursive calls.
- **Combine**: nothing is needed, because the subarrays are sorted in place.

The bulk of the work is in **partitioning**. Choosing the **first element as the key in an already sorted list** is a poor choice: no element is less than the key, so the partition is **imbalanced** and quicksort degrades to **O(n²)**, its worst case. A better choice is a key near the **middle of the list**, or a random one, in the hope that about half the elements end up on each side; a balanced partition gives **O(n log n)**, its best and average case.

## Merge sort

**Merge sort** closely follows divide and conquer:

1. **Divide** the n-element sequence into two subsequences of n/2 elements each.
2. **Conquer** by sorting the two subsequences recursively with merge sort.
3. **Combine** by **merging** the two sorted subsequences into the sorted answer.

The recursion "bottoms out" when a sequence has length 1, which is already sorted. The key operation is the **MERGE(A, p, q, r)** procedure, which merges the sorted subarrays A[p..q] and A[q + 1..r], like merging two face-up sorted piles of cards into one face-down pile by repeatedly taking the smaller top card. MERGE takes **Θ(n)** time for n = r − p + 1 elements. Sorting A = ⟨5, 2, 4, 7, 1, 3, 2, 6⟩ merges pairs into sorted runs of length 2, then 4, then 8.

Merge sort's running time satisfies T(n) = 2T(n/2) + Θ(n), giving **Θ(n log n)** in every case. So the best-case time of both quicksort and merge sort is **O(n log n)**, but quicksort's worst case is O(n²).

Source: CSC_236_Introduction_to_Algorithm.pdf (CSC 236 course book), Unit 4 (Sorting Techniques II) and Unit 9 (Analyzing Divide and Conquer Algorithms)
