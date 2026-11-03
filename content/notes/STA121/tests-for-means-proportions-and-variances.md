# Tests for Means, Proportions and Variances

## Large samples (n ≥ 30): z tests

By the central limit theorem, the test statistics below are approximately standard normal. The critical values are ±1.96 (5%) and ±2.58 (1%) for two tails, and 1.645 (5%) or 2.33 (1%) for one tail.

- **One mean**: **z = (x̄ − µ₀)/(σ/√n)**, using s if σ is unknown. **Bulbs**: n = 400, x̄ = 1570, s = 150 and H₀: µ = 1600 give z = −30/7.5 = **−4**. That is beyond −2.58, so reject at 1%.
- **Two means**: **z = (x̄₁ − x̄₂)/√(σ₁²/n₁ + σ₂²/n₂)**. **Tyres**: 22,400 against 21,800 km, σ = 1000, n = 50 each, gives z = 600/200 = **3**. The firm's belief that A lasts longer is one-sided, H₁: µ_A > µ_B, with a critical value of 1.645. Reject H₀ (two-sided, 3 > 1.96, the same decision).
- **One proportion**: **z = (p̂ − p₀)/√(p₀q₀/n)**.
  - 400 males among 1000 people, H₀: p = 0.5, gives z = −0.1/0.0158 = **−6.32**, so reject.
  - 95 of 100 batches on grade, H₁: p > 0.9, gives z = 0.05/0.03 = **1.667** > 1.645. Reject H₀: the proportion **is** above 90%. (The slide's conclusion says the opposite.)
- **Two proportions**: under H₀: p₁ = p₂, pool **p̄ = (n₁p̂₁ + n₂p̂₂)/(n₁ + n₂)** and use **z = (p̂₁ − p̂₂)/√(p̄q̄(1/n₁ + 1/n₂))**. **Smokers**: 400 of 600 and 450 of 900 give p̄ = 0.567, SE = 0.026 and z = **6.42**, so the habits differ.

## Small samples: t tests

When n < 30 and σ is unknown (normal population):

- **one mean**: **t = (x̄ − µ₀)/(s/√n)** with **n − 1** degrees of freedom;
- **two means**: a pooled-variance t with **n₁ + n₂ − 2** degrees of freedom.

The t distribution is symmetric about 0 with heavier tails than z, and it approaches z as the degrees of freedom grow. It is used for small-sample tests and intervals for means, differences of means and paired data.

## One variance: chi-square

**χ² = (n − 1)s²/σ₀²**, with **n − 1** degrees of freedom.

**Example**: five flow-rate readings (5.84, 5.76, 6.03, 5.90, 5.87) give s² = 0.00975. For H₁: σ² < 0.01, χ² = 4 × 0.00975/0.01 = **3.9**.

- The lower 5% point of χ²(4) is 0.711.
- Since 3.9 > 0.711, **do not reject H₀**: the data do not show the variance is below 0.01. (The slide rejects H₀ here.)

Source: STA 121 Lecture 6: Hypothesis Testing with Large Samples (Olubusoye), the 2018 Lecture 6: Hypothesis Testing II (Shittu) and the Lecture 7 exercise sheet; General knowledge of STA 121 for the two-sample t test and one-tailed critical values
