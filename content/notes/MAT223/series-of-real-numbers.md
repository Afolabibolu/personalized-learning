# Series of Real Numbers

## Series

A **series** Σ a_i of real numbers is defined through the double sequence {a_n, S_n}, where **S_n = a_1 + a_2 + ... + a_n** is the **nth partial sum** and **a_n = S_n − S_(n−1)** is the **general term**. The series is **convergent** if its sequence of partial sums (S_n) converges to some number a, called the **sum**, and we write Σ a_i = a. Otherwise it is **divergent**. The number a − S_n = Σ from i = n+1 of a_i is the **remainder**.

## Geometric series

For a geometric series with first term a and ratio r, **S_n = a(1 − r^n)/(1 − r)**. If **|r| < 1**, r^n → 0 and the series converges to **a/(1 − r)**; if |r| ≥ 1, it diverges. For example:

- Σ (2/3)^i from i = 1: S_n = (2/3)(1 − (2/3)^n)/(1/3) = **2(1 − (2/3)^n) → 2**.
- 1 + 1/2 + 1/4 + 1/8 + ... = 1/(1 − 1/2) = **2**.
- Σ (3/5)^k from k = 1 = (3/5)/(2/5) = **3/2**; Σ (1/3)^i from i = 1 = **1/2**; Σ 2^(−n) from n = 1 = **1**.

The series 1 + 3 + 5 + ... diverges, since its partial sums n² grow without bound.

## Tests for convergence

- **nth-term test**: **if Σ a_n converges, then a_n → 0**. So a series whose terms do not tend to 0 diverges. The converse is false: the **harmonic series Σ 1/n diverges** although 1/n → 0.
- **Telescoping**: Σ 1/((2n − 1)(2n + 1)) = Σ (1/2)(1/(2n − 1) − 1/(2n + 1)), whose partial sums tend to **1/2**.
- **Comparison test**: if 0 ≤ a_n ≤ b_n and Σ b_n converges, so does Σ a_n; if Σ a_n diverges, so does Σ b_n.
- **Ratio test**: let L = lim |a_(n+1)/a_n|. If **L < 1** the series converges (absolutely); if **L > 1** it diverges; if L = 1 the test is inconclusive. For Σ n/(n + 1)!, the ratio tends to 0, so it converges.
- **Absolute convergence**: **if Σ |a_n| converges, then Σ a_n converges**. A series that converges but not absolutely, such as Σ (−1)^(n+1)/n, is **conditionally convergent**.

Series obey linearity: if Σ a_n = s and Σ b_n = t, then **Σ (a_n + b_n) = s + t** and **Σ αa_n = αs**.

Source: MAT 223 lecture notes (scanned, Notes 1 to 9) (Series of Real Numbers); MAT 223 past papers. The ratio and comparison tests and the telescoping example are from general knowledge of MAT 223, as the papers set them but the scanned notes do not show them.
