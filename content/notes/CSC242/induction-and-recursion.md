# Mathematical Induction and Recursion

## Mathematical induction

The **principle of mathematical induction** proves that a statement P(n) is true for every positive integer n in two steps:

1. **Basis step**: show that P(1) is true.
2. **Inductive step**: show that P(n) → P(n + 1) for every n. The assumption that P(n) holds is the **induction hypothesis**.

Like a row of dominoes, if the first falls and each knocks over the next, all fall. For example, to prove 1 + 2 + … + n = n(n + 1)/2: P(1) is 1 = 1·2/2, true; and assuming the formula for n, adding n + 1 gives n(n + 1)/2 + (n + 1) = (n + 1)(n + 2)/2, which is P(n + 1).

The **second principle of mathematical induction** (strong induction) allows the inductive step to assume P(k) for all k ≤ n. The lectures use it to show that every integer greater than 1 can be written as a product of primes. If n + 1 is prime, it is trivially a product of one prime; otherwise n + 1 = a · b with a and b smaller, and by the induction hypothesis both are products of primes.

## Recursion

Recursion is a principle closely related to induction. In a **recursive definition**, an object is defined in terms of itself. We can recursively define **sequences**, **functions** and **sets**.

- A **recursively defined sequence**: the powers of 2, aₙ = 2ⁿ, can be defined by a₀ = 1 and aₙ₊₁ = 2aₙ.
- A **recursively (inductively) defined function** gives its value at 0 and a rule for f(n + 1) from f(n). The factorial: f(0) = 1, f(n + 1) = (n + 1) · f(n).
- A **recursively defined set** needs a starting element and a rule to build new elements, for example 3 ∈ S, and if x and y are in S then x + y is in S. Induction then proves properties of every element.

An algorithm is **recursive** if it solves a problem by reducing it to an instance of the same problem with smaller input. Two examples are the **recursive Euclidean algorithm**, gcd(a, b) = b if a = 0 else gcd(b mod a, a), and the **recursive Fibonacci algorithm**, f(0) = 0, f(1) = 1, f(n) = f(n − 1) + f(n − 2). For every recursive algorithm there is an equivalent **iterative** one. Recursive algorithms are often shorter and more elegant, but recursive Fibonacci evaluation repeats work and is far slower than the iterative version.

Source: CSC 242.pdf (Discrete Structures lecture slides), the induction and recursion sections; Recursive.pdf
