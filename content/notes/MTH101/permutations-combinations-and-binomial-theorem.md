# Permutations, Combinations and the Binomial Theorem

## Permutations

A **permutation** is an arrangement in a definite order. Arranging n different objects gives **n! = n(n − 1)...2·1** ways, with **0! = 1**. Choosing r of them in order gives **nPr = n!/(n − r)!**. The variations:

- With repetition allowed there are **nʳ** ways.
- With r₁ alike of one kind, r₂ of another and so on, there are **n!/(r₁!r₂!...)** ways. MATRICULATION (13 letters, with A, T and I twice each) gives 13!/(2!2!2!).
- A circle of n objects can be arranged in **(n − 1)!** ways.
- For 4 boys and 2 girls with the girls together, treat the girls as one unit: 5! × 2 = **240**. Apart, it is 6! − 240 = **480**.

## Combinations

A **combination** is a selection where order does not matter: **nCr = n!/(r!(n − r)!)**, with nCr = nCₙ₋ᵣ and nCr + nCr+1 = n+1Cr+1.

- Choosing 2 boys from 5 and 1 girl from 10 gives 5C2 × 10C1 = **100** ways.
- A committee of 5 from 8 people can be chosen in 8C5 = 56 ways. If a brother-sister pair must be included, it is 6C3 = 20.
- Dividing 12 people into groups of 3, 4 and 5 gives 12!/(3!4!5!) = **27720** ways.

## The binomial theorem

**Pascal's triangle** has 1 at the ends of each row, and each other number is the sum of the two above it. For a positive integer n,

**(x + y)ⁿ = Σ nCr xⁿ⁻ʳ yʳ**, and the **(r + 1)th term** is **Tᵣ₊₁ = nCr xⁿ⁻ʳ yʳ**.

The coefficients are symmetric. There is **one middle term if n is even** and two if n is odd. For (x − y)ⁿ the signs alternate: (3 − x)⁵ = 243 − 405x + 270x² − 90x³ + 15x⁴ − x⁵.

To find a particular power or the **term independent of x**, write the general term and set the power of x as required. In (x²/3 − 2/x³)⁶, the power is 12 − 5r = 2, so r = 2 and the x² coefficient is **20/27**.

## Other indices

For |x| < 1 and any rational q, **(1 + x)^q = 1 + qx + q(q − 1)x²/2! + ...**, an infinite series. (1 − x)⁻² = 1 + 2x + 3x² + ... + (r + 1)xʳ + ...

Used for approximations, this gives (0.98)⁶ = (1 − 0.02)⁶ ≈ 1 − 0.12 + 0.006 − 0.00016 = **0.8858**. For (a + bx)⁻ⁿ, take out a⁻ⁿ first; the series is valid for |bx/a| < 1.

Source: MAT 111 Lecture 7: Permutations and Combinations (Sangodapo); MAT 111 Lecture 8: Binomial Theorem (Sangodapo); MAT 111 past papers
