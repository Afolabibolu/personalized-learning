# Sequences of Real Numbers

## Convergence

A sequence (a_n) of real numbers **converges to a real number a** if, **for every ε > 0, there is a natural number n(ε) such that |a_n − a| < ε for all n ≥ n(ε)**. We write lim a_n = a. A sequence that does not converge **diverges**.

## Proving a limit

To show lim 1/n = 0: let ε > 0. We need |1/n − 0| = 1/n < ε, that is, n > 1/ε. Take n(ε) = [1/ε] + 1; then for n ≥ n(ε), |1/n − 0| < ε.

To show lim (3n + 1)/(7n − 45) = 3/7: |(3n + 1)/(7n − 45) − 3/7| = |(21n + 7 − 21n + 135) / (7(7n − 45))| = **142 / (7(7n − 45))**. For n large enough that 7n − 45 > 7n/2 (that is, n > 90/7), this is less than **142/(7 · 7n/2) = 284/(49n)**, which is less than ε once n > 284/(49ε). Choosing n(ε) above both bounds completes the proof.

## Key results

- **The limit of a convergent sequence is unique.** If a_n → a and a_n → b, then |a − b| ≤ |a − a_n| + |a_n − b| < 2ε for every ε, so a = b.
- **Every convergent sequence is bounded.**
- **Boundedness does not imply convergence.** The sequence **((−1)^n)** is bounded by 1 but oscillates between −1 and 1, so it diverges. Similarly {84 + (−1)^n} diverges.
- **Limit laws**: limits of sums, products and quotients (with a non-zero denominator limit) are the sums, products and quotients of the limits. For example, lim (4n² + 3n)/(n² − 6) = 4, by dividing top and bottom by n².

## Monotone sequences

A sequence is **monotone increasing** if a_n ≤ a_(n+1) for all n, and **monotone decreasing** if a_n ≥ a_(n+1). **A monotone sequence converges if and only if it is bounded**: an increasing sequence bounded above converges to its supremum. Calculus can test monotonicity: f(r) = 3 − 1/r has f′(r) = 1/r² > 0, so (3 − 1/r) is increasing. A sequence whose terms tend to 0 is called **null**.

## Cauchy sequences

A sequence (a_n) is a **Cauchy sequence** if **for every ε > 0 there is n(ε) such that |a_m − a_n| < ε for all m, n ≥ n(ε)**: its terms get arbitrarily close to **each other**. **Every convergent sequence is a Cauchy sequence**, and in R, by completeness, **every Cauchy sequence converges**. In Q this fails: decimal approximations of √2 form a Cauchy sequence of rationals with no rational limit. The **Bolzano-Weierstrass theorem** states that every bounded sequence has a convergent subsequence.

Source: MAT 223 lecture notes (scanned, Notes 1 to 9) (Examples of Convergent Sequences); MAT 223 past papers
