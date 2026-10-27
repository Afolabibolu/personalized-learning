# Sorting, Searching and Hashing

## Sorting

Sorting arranges data in a particular order, usually numerical or lexicographical, so that searching can be optimised (telephone directories, dictionaries). In **internal sorting** all the data fits in main memory; in **external sorting** it must be kept on disk.

- **Bubble sort:** compares adjacent elements and swaps them if they are out of order, repeating until the list is sorted. It takes O(n²) time.
- **Selection sort:** finds the smallest element and exchanges it with the first position, then the second smallest with the second position, and so on.
- **Insertion sort:** builds the sorted array one item at a time, like sorting playing cards. It is efficient for small data sets, needs a single extra memory space, and is **stable** (equal keys keep their order).
- **Quick sort:** chooses a pivot (the notes use the highest index), partitions the list so smaller values lie on one side and larger on the other, then sorts each partition recursively.

## Searching

- **Linear search:** compares the target with each element from the left, returning its index or −1. It takes O(n) time.
- **Binary search:** needs a sorted array. It compares the target with the middle element and repeats on the lower or upper half, giving T(n) = T(n/2) + c, which is **O(log n)**.
- **Interpolation search:** needs sorted data and estimates the target's position from its value.

## Hashing

**Hashing** stores and finds a record by computing its position from the key with a **hash function**, for example h(k) = k mod m for a table of m slots. A hash table therefore gives fast search, insertion and deletion, such as finding a phone number from a contact's name.

A **collision** happens when two keys hash to the same slot; **overflow** happens when a bucket has no room left. Ways to resolve collisions:

- **Linear probing:** try the next slots in turn, h(k) + 1, h(k) + 2, ... (mod m), until an empty one is found.
- **Quadratic probing:** try h(k) + 1², h(k) + 2², ...
- **Random probing / double hashing:** use a second function for the step.
- **Chaining:** keep a linked list of all keys at each slot.

With linear probing, a deleted slot is marked "deleted" rather than empty. An empty slot would stop a later search early and hide keys stored beyond it.

## File organisation

- **Sequential:** records are stored and read one after another in key order, which suits processing the whole file.
- **Indexed sequential:** an index of keys points into the sorted file, so a record can also be reached directly without reading all those before it.

Source: Graph Adj List.pdf, pages 23–39 (sorting and searching); hashing and file organisation are general knowledge, following the CSC 341 past papers (2021/22, 2023/24 and 2024/25 papers). The notes' claim that binary search takes constant time is left out; it takes O(log n)
