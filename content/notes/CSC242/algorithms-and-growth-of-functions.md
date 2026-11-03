# Algorithms and the Growth of Functions

## Algorithms

An **algorithm** is a **finite set of precise instructions for performing a computation or for solving a problem**. The lectures specify algorithms in **pseudocode**. Every algorithm has these **properties**:

1. **Input** from a specified set.
2. **Output** from a specified set (the solution).
3. **Definiteness** of every step in the computation.
4. **Correctness** of the output for every possible input.
5. **Finiteness** of the number of calculation steps.
6. **Effectiveness** of each calculation step.
7. **Generality** for a class of problems.

Two standard examples are an algorithm that **finds the maximum element in a finite sequence**, keeping the largest value seen while scanning, and **linear search**, which compares the target with each term in turn until it finds a match or reaches the end.

If the terms of a sequence are **ordered**, **binary search** is more efficient than linear search. It compares the target with the middle term, then **iteratively restricts the search to the half** that can still contain it, until one term is left.

## Complexity and growth

We are not so much interested in time and space complexity for **small inputs**. The difference between linear and binary search is meaningless for a sequence of 10 elements but huge for a billion. Suppose algorithm A takes 5,000n steps and algorithm B takes 1.1ⁿ steps: for small n, B may be faster, but for large inputs B becomes unusable while A is still feasible. What matters is the **growth** of the complexity function as the input size grows.

The growth of functions is described with **big-O notation**. Let f and g be functions; we say **f(x) is O(g(x))** if there are constants C and k such that |f(x)| ≤ C|g(x)| whenever x > k. When we analyse the growth of complexity functions, f(x) and g(x) are always positive, so the absolute values can be dropped. Big-O gives an upper bound on growth: for instance, a polynomial of degree n is O(xⁿ), and linear search takes O(n) comparisons, while binary search takes O(log n).

Source: Algorithms & The Big O.pdf; CSC 242.pdf (Discrete Structures lecture slides), the algorithms section
