# Sequences, Series and Mathematical Induction

## Progressions

- An **arithmetic progression (A.P.)** a, a + d, a + 2d, ... has nth term **a + (n − 1)d** and sum **Sₙ = (n/2)[2a + (n − 1)d]**. The arithmetic mean of a and c is (a + c)/2. If the 3rd and 7th terms are −1 and 11, then a = −7 and d = 3, so the nth term is 3n − 10, and **n = 20** terms sum to 430.
- A **geometric progression (G.P.)** a, ar, ar², ... has nth term **arⁿ⁻¹** and sum **Sₙ = a(1 − rⁿ)/(1 − r)** (or a(rⁿ − 1)/(r − 1) for r > 1). The geometric mean of a and c is ±√(ac). If |r| < 1, the **sum to infinity** is **S∞ = a/(1 − r)** (from general knowledge; the slides do not state it). With second term 6 and fourth term 54, a = 2 and r = 3, so the nth term is **2 × 3ⁿ⁻¹**.
- A **harmonic progression (H.P.)** has terms 1/a, 1/(a + d), ..., the reciprocals of an A.P. The harmonic mean of a and c is 2ac/(a + c).

## Recurrences and sums

A sequence may be defined by a **recurrence**: aₙ₊₁ = aₙ + 2n with a₁ = 1 gives 1, 3, 7, 13, ..., so **aₙ = n² − n + 1**.

A **telescoping series** cancels in pairs once it is split by partial fractions: **Σ 1/(k(k + 1)) = 1 − 1/(n + 1) = n/(n + 1)**.

Standard sums: **Σk = n(n + 1)/2**, **Σk² = n(n + 1)(2n + 1)/6** and **Σk³ = n²(n + 1)²/4**. They combine: Σk(k + 1)² = Σk³ + 2Σk² + Σk = n(n + 1)(n + 2)(3n + 5)/12.

The **first differences** of a sequence are Δxₙ = xₙ₊₁ − xₙ, and the **second differences** are Δ²xₙ = xₙ₊₂ − 2xₙ₊₁ + xₙ.

## Mathematical induction

**If P(1) is true, and P(k) true implies P(k + 1) true, then P(n) is true for every positive integer n.** The steps:

1. Check n = 1.
2. Assume the result for n = k.
3. Prove it for n = k + 1.

**Example**: 1·2 + 2·3 + ... + n(n + 1) = n(n + 1)(n + 2)/3. Adding the next term (k + 1)(k + 2) to the assumed sum gives (k + 1)(k + 2)(k + 3)/3.

**Divisibility example**: 9 divides 5²ⁿ + 3n − 1. For n = 1 the value is 27. Assume 5²ᵏ = 9N − 3k + 1; then 5²⁽ᵏ⁺¹⁾ + 3(k + 1) − 1 = 25(9N − 3k + 1) + 3k + 2 = 9(25N − 8k + 3).

Source: MAT 111 Lecture 10: Sequences and Series (Sangodapo); MAT 111 Lecture 6: Mathematical Induction (Sangodapo); MAT 111 past papers; General knowledge of MTH 101 for the sum to infinity
