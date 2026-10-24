# Algorithm Fundamentals and Analysis

## What the topic is

An algorithm is a finite sequence of instructions, each with a clear meaning, that can be carried out with finite effort in finite time and always terminates. Every algorithm must satisfy five criteria: **input** (zero or more quantities supplied), **output** (at least one quantity produced), **definiteness** (each instruction is clear), **finiteness** (it stops after a finite number of steps) and **effectiveness** (each step could be done with pencil and paper).

## Performance and design goals

Performance is the memory and time an algorithm needs. **Time complexity** is the running time as a function of problem size; its behaviour as size grows is the asymptotic time complexity. **Space complexity** has three parts: instruction space, data space and environment stack space. The three design goals are to save time, to save space and to "save face" by never locking up or producing garbled data.

## Classifying algorithms

- **By implementation:** recursion or iteration; exact or approximate; serial, parallel or distributed.
- **By design method:** greedy, divide and conquer, dynamic programming, linear programming, reduction (transform and conquer), backtracking, branch and bound.
- **By design approach:** top-down (decompose a large problem) or bottom-up (build from solved parts).

Common growth rates, from best to worst: 1, log n, n, n log n, n², n³ and 2ⁿ. When n doubles, an n² algorithm takes four times as long and an n³ algorithm eight times as long.

## Asymptotic notation

Big-O gives an **upper bound** (growth ≤ g(n)); Big-Theta means the same order; little-o means strictly slower growth; little-omega means strictly faster. Rules for Big-O: ignore constant factors, so O(20n³) = O(n³); ignore smaller terms, so O(n² + n) = O(n²); and an O(n) algorithm is also O(n²).

## Recurrences

Recursive algorithms give recurrences, for example merge sort's T(n) = 2T(n/2) + cn. They are solved by the substitution method, the recurrence tree method, the master method or the iteration method. The **master theorem** handles T(n) = aT(n/b) + f(n), with a ≥ 1 and b > 1. Compare log_b a with c, the power of n in f(n): greater gives case 1, equal gives case 2 (θ(n^c log n)), and smaller gives case 3 (θ(f(n))). For example, T(n) = 4T(n/4) + 5n has log₄4 = 1 = c, so it is θ(n log n).

## Amortized analysis

Amortized analysis averages the cost over a sequence of operations, so an occasional expensive operation is spread over many cheap ones. There are three methods. **Aggregate analysis** bounds the total T(n) and divides by n. The **accounting method** stores credit from cheap operations. The **potential method** computes that credit from the state of the data structure. A dynamic array that doubles when full has O(1) amortized insertion cost, even though a single resize costs O(n). The analysis involves no probability.

Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Sessions 1 and 7
