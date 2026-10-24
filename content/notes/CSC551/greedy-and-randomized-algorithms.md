# Greedy and Randomized Algorithms

## Greedy algorithms

A greedy algorithm solves a problem by picking the best option available at each moment. It does not consider whether that choice leads to the best overall result, and it never reverses an earlier decision, even a wrong one. It works top-down. A greedy approach suits a problem with two properties:

- **Greedy choice property:** an optimal solution can be reached by taking the best choice at each step without reconsidering earlier steps.
- **Optimal substructure:** the optimal overall solution corresponds to optimal solutions of the sub-problems.

**Advantages:** it is easy to describe, and it can perform better than other algorithms, though not in every case. **Main drawback:** it does not always find the optimal solution. In the course example, the root of a tree weighs 20, with children 2 and 3. Greedy picks 3, then that node's only child, 1, giving 20 + 3 + 1 = 24. The longest path is actually 20 + 2 + 10 = 32.

**Steps.** Start with an empty solution set. At each step add an item. Keep it if the set is still feasible; otherwise reject it and never consider it again.

**Coin change example.** To make N18 from N5, N2 and N1 coins, always take the largest coin that fits: 5, 5, 5, then 2 (another 5 would exceed 18), then 1.

**Activity selection.** Repeatedly choose the activity with the earliest finish time whose start is no earlier than the last chosen finish. From {(5,9), (1,2), (3,4), (0,6), (5,7), (8,9)} it selects (1,2), (3,4), (5,7) and (8,9). The cost is O(n log n) unsorted and O(n) if the list is already sorted.

**Types listed in the course** include knapsack, job scheduling, Prim's, Kruskal's, Dijkstra's and Huffman coding.

## Randomized algorithms

A deterministic algorithm gives the same output every time for the same input. A randomized algorithm adds random bits to its logic. The input is not randomised, only the logic. Because a randomized algorithm can give a wrong answer, **amplification** runs parts of it several times to raise the chance of a correct one.

- **Las Vegas:** never gives an incorrect output; the running time is the random variable. Example: randomized quicksort.
- **Monte Carlo:** finishes within a fixed time but may be wrong with a small probability. Example: Karger's minimum cut.

**Why randomise?** In the zero-sum game view, one player designs the algorithm and the other chooses the worst input. Quicksort on an already sorted list hits its O(n²) worst case. Choosing the pivot at random makes that worst case much rarer. Merge sort's time does not depend on the input, so randomising it gains nothing.

**Karger's minimum cut** repeatedly picks a random edge and contracts its two vertices into a supernode, removing self-loops, until two nodes remain. The edges between them form the cut.

Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Sessions 4 and 5
