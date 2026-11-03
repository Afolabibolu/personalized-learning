# Recurrences and the Master Theorem

## Divide-and-conquer recurrences

When an algorithm contains a recursive call to itself, its running time can often be described by a **recurrence**: **an equation or inequality that describes a function in terms of its value on smaller inputs**. For a divide-and-conquer algorithm, let T(n) be the time on a problem of size n. If the problem is small enough (n ≤ c), it takes constant time, Θ(1). Otherwise it is divided into **a** subproblems, each **1/b** the size of the original; dividing takes D(n) and combining C(n), giving the **general recurrence**

T(n) = Θ(1) if n ≤ c, and T(n) = **aT(n/b) + D(n) + C(n)** otherwise.

For **merge sort**, a = b = 2, dividing takes Θ(1) and merging Θ(n), so **T(n) = 2T(n/2) + Θ(n)**, whose solution is **T(n) = Θ(n lg n)**.

## Solving recurrences

- The **substitution method**: **guess** the form of the solution, then use **mathematical induction** to prove it correct and find the constants. It can establish upper or lower bounds. Good guesses come from experience with similar recurrences (T(n) = 2T(n/2 + 17) + n behaves like 2T(n/2) + n) and from recursion trees.
- The **recursion-tree method**: convert the recurrence into a **tree whose nodes represent the costs at the various levels** of recursion, **sum the costs within each level**, then sum all the levels. It is especially useful for divide-and-conquer algorithms, and is usually used to produce a good guess that the substitution method then verifies.
- The **master method**: a "cookbook" for recurrences of the form **T(n) = aT(n/b) + f(n)** with **a ≥ 1, b > 1** and f(n) asymptotically positive. Comparing f(n) with n^(log_b a):
  1. If f(n) = O(n^(log_b a − ε)) for some ε > 0, then T(n) = Θ(n^(log_b a)).
  2. If f(n) = Θ(n^(log_b a)), then T(n) = Θ(n^(log_b a) lg n).
  3. If f(n) = Ω(n^(log_b a + ε)) and af(n/b) ≤ cf(n) for some c < 1, then T(n) = Θ(f(n)).

For T(n) = 16T(n/2) + n, n^(log₂ 16) = n⁴ dominates, so case 1 gives Θ(n⁴). For T(n) = 2T(n/2) + n, case 2 gives Θ(n lg n). The master method needs memorising three cases, and it does not apply when the recurrence is not in this form (for example when subproblems are of unequal size, as in an unbalanced quicksort, or when f(n) falls in the gaps between the cases).

Source: CSC_236_Introduction_to_Algorithm.pdf (CSC 236 course book), Unit 9 (Analyzing Divide and Conquer Algorithms) and Units 11 to 13 (Recurrences: Overview and Substitution, Recursion-Tree Method, The Master Method)
