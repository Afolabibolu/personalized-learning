# Searching: Linear and Binary Search

## Searching

Many applications need to search for a particular element. **Searching** means finding whether a given element is present in a list, and the method depends on **how the elements are organised**: for an **unordered** list we use **linear (sequential) search**, and for an **ordered** list, **binary search**.

## Linear search

In **linear search**, the key is compared **sequentially** with the elements of the list, one after another. If an element matches, the search **terminates successfully** and returns the index of the matching element. If the end of the list is reached with no match, the search **terminates unsuccessfully**.

- In the **best case**, the key is the first element, found in one comparison.
- In the **worst case**, the key is the last element inspected, or absent, so every element is examined: n comparisons, **O(n)**.
- On average, the element is found about halfway through.

## Binary search

The **prerequisite for binary search is that the list must be sorted**. The key is compared with the **middle element**:

- if they are equal, the search succeeds;
- if the key is smaller, the search continues in the lower half;
- if it is larger, in the upper half.

Each comparison halves the part of the list that can contain the key, so the number of comparisons is **no more than about log₂ n**, where n is the size of the list. Binary search therefore takes **O(log n)** time: for a million elements, about 20 comparisons instead of up to a million. It can be written **recursively** (calling itself on the chosen half) or **non-recursively** with a loop that moves the low and high bounds.

The difference between linear and binary search is small for small n, but grows quickly as n increases, which is why the search algorithms show that binary search is more efficient than ordinary sequential search. (The course book prints the binary search time as O(n log n); that is a slip, and the bound that follows from its own argument of at most log₂ n comparisons is O(log n).)

A practical exercise is to implement both searches on 500 randomly generated numbers in a linear array and compare their times.

Source: CSC_236_Introduction_to_Algorithm.pdf (CSC 236 course book), Unit 5 (Searching Techniques) and Unit 6 (Analysis of Algorithms)
