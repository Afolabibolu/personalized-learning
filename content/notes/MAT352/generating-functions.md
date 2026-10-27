# Moment and Probability Generating Functions

## Moments

The **r-th moment about the origin** is μ′ᵣ = E(Xʳ), and the **r-th moment about the mean** is μᵣ = E[(X − μ)ʳ]. The first moment is the mean, and the second moment about the mean is the variance: Var(X) = μ′₂ − (μ′₁)².

## The moment generating function

The **moment generating function (MGF)** of X is

**Mₓ(t) = E(e^(tX))**,

that is, Σ e^(tx) f(x) for a discrete X or ∫ e^(tx) f(x) dx for a continuous X, wherever it exists near t = 0. Expanding e^(tX) as a series shows that the coefficient of tʳ/r! is E(Xʳ), so:

**E(Xʳ) = Mₓ⁽ʳ⁾(0)**, the r-th derivative at t = 0.

Hence **E(X) = M′(0)** and **Var(X) = M″(0) − [M′(0)]²**.

## Examples

- **Binomial(n, p):** M(t) = (q + p eᵗ)ⁿ, where q = 1 − p. Then M′(0) = np and M″(0) = n(n − 1)p² + np, so the mean is **np** and the variance is **npq**.
- **Poisson(λ):** M(t) = Σ e^(tx) e^(−λ) λˣ / x! = e^(−λ) e^(λeᵗ) = e^(λ(eᵗ − 1)). Both the mean and the variance equal **λ**.
- **Gamma(α, λ):** M(t) = (1 − t/λ)^(−α) for t < λ, giving mean **α/λ** and variance **α/λ²**.
- **Normal(μ, σ²):** M(t) = e^(μt + σ²t²/2), so the mean is μ and the variance σ².

**Example:** if f(x) = e^(−2x) + ½e^(−x) for x > 0, then M(t) = 1/(2 − t) + 1/(2(1 − t)) for t < 1. So E(X) = M′(0) = ¼ + ½ = ¾, and E(X²) = M″(0) = ¼ + 1 = 5/4.

## Properties

1. **Uniqueness:** if two random variables have the same MGF on an interval around 0, they have the same distribution.
2. **Linear transformation:** M_(aX + b)(t) = e^(bt) Mₓ(at).
3. **Sums:** if X and Y are independent, M_(X + Y)(t) = Mₓ(t) M_Y(t). This finds the distribution of sums of independent variables; for example, a sum of independent Poissons is Poisson.

## The probability generating function

For a discrete variable on {0, 1, 2, …}, the **probability generating function (PGF)** is **G(s) = E(sˣ) = Σ P(X = x) sˣ**. Then:

- G(1) = 1;
- **E(X) = G′(1)**;
- **Var(X) = G″(1) + G′(1) − [G′(1)]²**.

For Poisson(λ), G(s) = e^(λ(s − 1)).

**A useful expectation:** for X ~ Poisson(λ), E[1/(1 + X)] = (1 − e^(−λ)) ÷ λ.

Source: Lanre_s 352 note.pdf (a student's handwritten MAT 352 lecture notes, used as secondary) (moment generating function, binomial MGF, mean and variance); MAT 352 Assignment (gamma MGF); the PGF, properties and other worked examples are general knowledge, following the MAT 352 course outline and past papers (2020/21 Questions 4b and 5b, 2021/22 Questions 3b and 5b, the 2023/24 test)
