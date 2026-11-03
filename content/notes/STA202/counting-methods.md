# Counting: Permutations and Combinations

## The basic principle of counting

Many statistical problems need the number of possible outcomes. **Theorem (the multiplication rule)**: if an operation consists of two steps, the first done in **n1** ways and, for each of these, the second in **n2** ways, the whole operation can be done in **n1·n2** ways. It extends to k steps: n1·n2·...·nk. For example, travelling by bus, train or plane to one of five states can be done in **5 × 3 = 15** ways.

## Factorials

**n! = n(n − 1)(n − 2)...(2)(1)**, with **0! = 1**. For example, 5! = 120.

## Permutations

A **permutation** is an **ordered arrangement**. The number of permutations of n distinct objects taken r at a time is

**nPr = n!/(n − r)!**,

and all n objects can be arranged in **n!** ways. Three-digit numbers formed from the 8 digits 1 to 8 **without repetition** number 8P3 = 8 × 7 × 6 = **336**; **with repetition allowed**, there are 8³ = **512**.

- Arranging n objects **in a circle** gives **(n − 1)!** arrangements.
- If n objects include n1 alike, n2 alike and so on, the number of distinct arrangements is **n!/(n1! n2! ... nk!)**. The letters of STATISTICS give 10!/(3! 3! 2!) = 50,400.

## Combinations

A **combination** is an **unordered selection**. The number of ways to choose r objects from n is

**C(n, r) = nCr = n!/(r!(n − r)!)**.

Choosing a committee of 3 from 8 people can be done in C(8, 3) = **56** ways. Order matters for permutations but not for combinations, so **nPr = r!·nCr**.

The number of possible **samples of size n from a population of N without replacement** is **C(N, n)**; **with replacement** (ordered), it is **Nⁿ**.

## Identities

- **C(n, r) = C(n, n − r)**: choosing r to include is the same as choosing n − r to exclude. So if C(n, 12) = C(n, 8), then n = 20.
- **Pascal's rule**: **C(n, r) = C(n − 1, r) + C(n − 1, r − 1)**.
- **Vandermonde's identity**: **Σ over k of C(m, k)C(n, r − k) = C(m + n, r)**.
- **Binomial theorem**: (a + b)ⁿ = Σ C(n, r) aʳ bⁿ⁻ʳ, so Σ C(n, r) = 2ⁿ.

Source: STA 204 Lecture 2 (Combinatorial methods) (Combinatorial methods); the identities follow the counting questions set in the STA 211 test filed in this folder.
