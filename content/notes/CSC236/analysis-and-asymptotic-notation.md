# Analysis of Algorithms and Asymptotic Notation

## Analysing algorithms

**Analysing an algorithm** means **predicting the resources it requires**, most often its running time; by analysing several candidate algorithms, the most efficient can be identified and inferior ones discarded. Inputs are grouped by **size n**, and **T(n)** is the **running time** of the program on an input of size n: the number of statements executed, counted up to a constant factor. A program with T(n) = cn runs in time linearly proportional to n. Each line of pseudocode takes a constant time cᵢ, and the running time is found by assigning a cost and a number of times to each line and summing. Running times are not based on a computer's own measured times, because those depend on the machine, while T(n) describes the algorithm itself.

For many algorithms T(n) depends on the data as well as n, so three cases are distinguished:

- **Tmax(n)**, the **worst-case** complexity: the maximum over all inputs of size n;
- **Tmin(n)**, the **best-case** complexity: the minimum;
- **Tavg(n)**, the **average-case** complexity.

Algorithms are generally analysed by their **worst case**, for four reasons: many algorithms perform at their worst case a large part of the time; the best case says little, since nearly all searches can succeed in one step; the average case is hard to define and compute; and **the worst case gives an upper bound on performance**, a guarantee.

## Big O and growth rate

**O-notation** expresses the **upper bound** of a function within a constant factor: f(n) = O(g(n)) if there are constants c and n₀ with f(n) ≤ c·g(n) for all n ≥ n₀. What matters is the **growth rate** (order of growth) of f, which describes how efficient the algorithm is for arbitrary inputs. Simplification rules:

- **Constant terms are ignored**, expressed as O(1): for T(n) = n + 50 with n = 1024, the 50 is under 5% of the time.
- **Multiplicative constants are omitted**: O(cT) = cO(T) = O(T).
- **Only the highest-order term is kept**: n² + n is O(n²), and 3n² + 10n + 10 + lg n is O(n²).

Other notations: **Ω (big omega)** gives a **lower bound**; **Θ (theta)** **asymptotically bounds a function from above and below**, a tight bound; **little o** is an upper bound that is not tight, and **little ω** a lower bound that is not tight. Common growth rates, slowest growing first, are O(1), O(lg n), O(n), O(n lg n), O(n²) and exponential.

Source: CSC_236_Introduction_to_Algorithm.pdf (CSC 236 course book), Unit 6 (Analysis of Algorithms), Unit 7 (The Big 'O' Notation) and Unit 10 (Growth of Functions)
