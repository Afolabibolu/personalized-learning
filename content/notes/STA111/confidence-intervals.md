# Confidence Intervals

## Confidence intervals

A **point estimate** gives one value, such as x̄ or p̂. A **confidence interval** is point estimate ± **margin of error**. The margin of error is the critical value × the standard error. The usual z values are **1.645, 1.96 and 2.576** for 90%, 95% and 99%.

## Means

- **Large samples (or σ known)**: **x̄ ± z(σ/√n)**.
- **Small samples with σ unknown** (normal population): **x̄ ± t(n−1)(s/√n)**. With n = 20 and α = 5%, the two-sided t(19) is **2.093**.
- **Two means**: **(x̄₁ − x̄₂) ± z√(s₁²/n₁ + s₂²/n₂)**. With means 15 and 13, SDs 3 and 4 and n = 36 each, the standard error is √(9/36 + 16/36) = 0.833, so the 95% interval is 2 ± 1.633 = **(0.367, 3.633)**.

**Example (yams)**: 10 weights with x̄ = 10.13 and s = 0.31 give the 99% interval 10.13 ± 3.250 × 0.31/√10 = **10.13 ± 0.32**. (The compiled test's options assume a different s.)

## Proportions

- For a large sample, **p̂ = x/n** and the interval is **p̂ ± z√(p̂(1 − p̂)/n)**.
- 123 of 300 households have colour TV: p̂ = **0.41**, and the 95% margin is 1.96√(0.41 × 0.59/300) = **±0.0557**.
- 12 abnormal embryos out of 50: p̂ = 0.24, so the 95% interval is 0.24 ± 0.118 = **(0.122, 0.358)** and the 99% interval is (0.084, 0.396).
- **Two proportions**: **(p̂₁ − p̂₂) ± z√(p̂₁q̂₁/n₁ + p̂₂q̂₂/n₂)**.

## Interpreting

"95% confidence" means that, in repeated sampling, 95% of intervals built this way would contain the true population parameter. The interval gets **narrower** as **n increases** and **wider** at **higher confidence**, so a larger sample is the way to gain precision without losing confidence.

Source: STA 114 Lectures 7 and 8: Confidence Intervals (Ogunde); STA 111 2025 test; General knowledge of STA 111 for the t value
