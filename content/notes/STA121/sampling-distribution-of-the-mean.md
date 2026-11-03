# Sampling Distribution of the Mean

## Sampling distributions

If all possible samples of size n are drawn and a statistic is computed for each, the values form the statistic's **sampling distribution**.

From a population of N:

- there are **Nⁿ** possible samples **with replacement**;
- there are **NCn** samples **without replacement**.

For the population {0, 2, 4, 6} (µ = 3, σ = √5), samples of 2 number 4² = **16** with replacement and 4C2 = **6** without.

The standard deviation of a sampling distribution is the **standard error** of the statistic. It differs from σ:

- σ measures variation among the members of the population;
- the standard error measures variation in the statistic due to sampling.

Standard errors are used in tests and confidence intervals.

## The three properties of x̄

1. **Centre**: the mean of all sample means equals µ, so x̄ is **unbiased**. The six means above (1, 2, 3, 3, 4, 5) average 3.
2. **Spread**: the standard error is **σ_x̄ = σ/√n**, which shrinks as n grows. When σ is unknown, use s/√n. Without replacement from a finite population, multiply by the **finite correction factor √((N − n)/(N − 1))**.
3. **Shape**:
   - from a **normal** population, x̄ is normal for **every** n;
   - otherwise the **central limit theorem** says x̄ approaches normal as n grows, and **n ≥ 30** is usually enough.

So **z = (x̄ − µ)/(σ/√n)** is approximately standard normal. When σ is unknown and estimated by s, (x̄ − µ)/(s/√n) follows **Student's t distribution** for small samples.

## Two means

For independent samples, **x̄₁ − x̄₂** has mean µ₁ − µ₂ and standard error **√(σ₁²/n₁ + σ₂²/n₂)**.

**Example**: wire from company A has mean strength 4500 kg (σ = 200), and from B, 4000 kg (σ = 300).

- With 50 and 100 wires tested, the SE = √(40,000/50 + 90,000/100) = √1700 = **41.23**.
- P(x̄_A − x̄_B ≥ 600) = P(Z ≥ 100/41.23 = 2.43) ≈ **0.0075**.

Source: STA 121 Lecture 2: Sampling Distribution of a Statistic (Olubusoye)
