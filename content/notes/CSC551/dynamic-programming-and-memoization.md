# Dynamic Programming and Memoization

## What the topic is

Dynamic programming (DP) breaks an algorithmic problem into sub-problems, saves their results, and combines them into the overall solution, usually a maximum or minimum. Richard Bellman introduced it in the 1950s. DP is mainly an optimisation over plain recursion: when a recursive solution calls itself repeatedly with the same inputs, storing the results reduces exponential time to polynomial time. For example, recursive Fibonacci is exponential, while filling an array f[i] = f[i − 1] + f[i − 2] is linear.

## When DP applies

Two signs show that a problem suits DP:

- **Overlapping subproblems:** the same sub-problem is needed more than once. F(n − 2) is reused when computing F(n) and F(n − 1). Binary search has no overlap, so it is divide and conquer, not DP. Merge sort and quicksort are not DP problems either.
- **Optimal substructure:** the best answer is built from the best answers to the sub-problems. Shortest paths have it: if p is on the shortest path from t to w, that path is the shortest t-to-p path plus the shortest p-to-w path. The longest path problem does not have it.

The development steps are:

1. Characterise the structure of an optimal solution.
2. Define its value recursively.
3. Compute that value bottom-up.
4. Construct the solution from the computed information.

## Top-down and bottom-up

**Top-down** recursion with stored results is memoization. It is easy to understand and debug, but it uses call-stack memory and can overflow the stack. **Bottom-up** tabulation solves the smallest sub-problems first. It removes recursion, so there is no stack overflow or call overhead.

## Classic DP algorithms

- **Longest common subsequence (LCS):** the longest subsequence shared by the sequences. Its elements need not be consecutive. For MNOP and MONMP the LCSs are MNP and MOP. It is used in genome sequencing.
- **Floyd–Warshall:** shortest paths between all pairs of vertices in a weighted graph, in O(n³). A negative number on the diagonal reveals a negative cycle.
- **Bellman–Ford:** shortest paths from one source, even with negative edge weights. It works by relaxation and is slower than Dijkstra's algorithm.

## Memoization

The word memoization comes from the Latin *memorandum*, "to remember". It is a form of caching: it stores a function's results so repeated calls with the same input are not recomputed. With several factorial queries, storing each factorial gives every later answer in O(1).

Memoization is called 1-D, 2-D or 3-D by how many arguments change between recursive calls. Fibonacci is 1-D.

**Memoization versus tabulation.** Tabulation is faster and fills every table entry from the first one, but its state transitions are harder to think out. Memoization is easier to write, fills the table on demand and solves only the sub-problems actually needed. It is slower because of its many recursive calls.

Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Sessions 3 and 6
