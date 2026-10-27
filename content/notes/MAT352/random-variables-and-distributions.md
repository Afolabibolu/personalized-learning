# Random Variables, Distribution Functions and Expectation

## Random variables

A **random variable** X is a function that assigns a real number to each outcome of a sample space. It is:

- **discrete** if it takes a finite or countable set of values;
- **continuous** if it takes values in an interval, with P(X = x) = 0 for every single x.

## Probability functions

- A discrete X has a **probability mass function (pmf)** f(x) = P(X = x), with f(x) ≥ 0 and Σ f(x) = 1.
- A continuous X has a **probability density function (pdf)** f(x) ≥ 0 with ∫ f(x) dx = 1, and P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx.

**Example:** f(x) = C x²(1 − x) on [0, 1] is a valid pdf when C ∫₀¹ (x² − x³) dx = C (1/3 − 1/4) = C/12 = 1, so **C = 12**.

## The distribution function

The **cumulative distribution function (CDF)** is **F(x) = P(X ≤ x)**. It:

1. is non-decreasing;
2. tends to 0 as x → −∞ and to 1 as x → ∞;
3. is right-continuous.

Then P(a < X ≤ b) = F(b) − F(a), and for a continuous X, f(x) = F′(x). A jump in F at x equals P(X = x), so a distribution may be **mixed**, with jumps and continuous parts.

**Example:** if F(x) = (x + 1)/2 for −1 < x < 1, then P(X > ½) = 1 − F(½) = 1 − ¾ = **¼**.

## The indicator function

The **indicator function** of an event A is I_A(ω) = 1 if ω ∈ A and 0 otherwise. It is a random variable with **E(I_A) = P(A)**, which makes many probability calculations a matter of expectation.

## Expectation

The **expected value (mean)** is:

- E(X) = Σ x f(x) for a discrete X;
- E(X) = ∫ x f(x) dx for a continuous X.

More generally, E[g(X)] = Σ g(x) f(x) or ∫ g(x) f(x) dx.

Expectation is **linear**: E(aX + b) = a E(X) + b, and E(X + Y) = E(X) + E(Y).

**Example:** for Y uniform on {1, 2, …, 47}, E(Y) = 24, and P(Y even) = 23/47.

## Variance

The **variance** measures spread:

**Var(X) = E[(X − μ)²] = E(X²) − [E(X)]²**.

The **standard deviation** is √Var(X), and Var(aX + b) = a² Var(X).

For a fair four-sided die, E(X) = 2.5, E(X²) = 7.5, so Var(X) = 7.5 − 6.25 = **1.25**.

Source: Lanre_s 352 note.pdf (a student's handwritten MAT 352 lecture notes, used as secondary) (random variables, discrete and continuous distributions, expectation, variance); the indicator function and the worked examples are general knowledge, following the MAT 352 course outline and past papers (2020/21 Question 1a, 2021/22 Questions 1a, 2a, 3b and 6a, and the 2023/24 test)
