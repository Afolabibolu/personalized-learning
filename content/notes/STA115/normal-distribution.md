# The Normal Distribution

## The normal curve

The **normal (Gaussian)** distribution is the most important distribution in statistics, because many measurements, such as heights and weights, are approximately normal. Its pdf is

**f(x) = (1/(σ√(2π))) e^(−(x − µ)²/(2σ²)), −∞ < x < ∞**.

Its properties:

- it is **bell-shaped and symmetric about µ**;
- **mean = median = mode = µ**, so the centre of the curve is the mean;
- the variance is σ²;
- the total area under the curve is 1.

**Notation**: X ~ N(µ, σ²), where the **second number is the variance**. So N(11, 0.04) has σ = 0.2, and N(75, 100) has σ = 10.

## Standardising

**Z = (X − µ)/σ ~ N(0, 1)** is the **standard normal**, and its cdf Φ(z) = P(Z ≤ z) comes from tables.

**Rules**:

- P(Z > z) = 1 − Φ(z);
- P(a < Z < b) = Φ(b) − Φ(a);
- by symmetry, Φ(−z) = 1 − Φ(z).

**Examples**:

- P(0.53 < Z < 2.06) = 0.9803 − 0.7019 = **0.2784**.
- P(Z > 2.89) = 1 − 0.9981 = **0.0019**. (The slide writes Φ(2.86) but uses the value for 2.89.)
- Test scores N(100, 10²): P(90 ≤ X ≤ 115) = P(−1 ≤ Z ≤ 1.5) = 0.9332 − 0.1587 = **0.7745**.
- N(11, 0.04): P(10.6 < X < 11.2) = P(−2 < Z < 1) = 0.8413 − 0.0228 = **0.8185**.

## From a probability back to a value

To be in the **top 10%** of the test scores, find c with P(X ≤ c) = 0.90. Since Φ(1.2816) = 0.90, c = 100 + 1.2816 × 10 ≈ **112.8**. Useful values: P(Z ≥ c) = 0.025 at c = 1.96, P(|Z| ≤ c) = 0.95 at c = 1.96, and P(Z > c) = 0.05 at c = 1.645.

## Normal approximation to the binomial

For large n, a binomial count is approximately normal with **µ = np** and **σ = √(npq)**. A **continuity correction** of ±0.5 improves the approximation, because the count is discrete. This is how a question such as "25 to 30 correct by guesswork out of 80" is answered: µ = 20 and σ = √15.

Source: STA 115 Lecture 6: Normal (Gaussian) Distribution (Shittu) and the Normal and Sampling Distribution slides; STA 115 tests (2016/17 to 2023) and STA 112 Probability I papers; General knowledge of STA 115 for the normal approximation to the binomial
