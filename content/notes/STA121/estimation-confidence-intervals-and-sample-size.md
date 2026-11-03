# Estimation, Confidence Intervals and Sample Size

## Point and interval estimates

- A **point estimator** (x̄, s, p̂) gives one value, the **point estimate**, such as "10% defective". It does not say how precise it is.
- An **interval estimate** (confidence interval) combines three things: a point estimate, a margin of error, and a degree of confidence.

**Interval = point estimate ± margin of error**, where the margin = **z_c × standard error**. The usual values of z_α/2 are **1.645, 1.960 and 2.576** for 90%, 95% and 99%.

A 95% interval means that **95% of all intervals** built this way from samples of the same size contain the true value.

## Good estimators

- **Unbiased**: the estimator's mean over all samples equals the parameter. x̄ and p̂ are unbiased, but **s is not unbiased for σ** (the bias shrinks as n grows).
- **Consistent**: the estimator gets closer to the parameter as n grows, since σ/√n → 0.
- **Efficient**: of two unbiased estimators, the one with the smaller standard error.

## Intervals

- **µ with σ known (n ≥ 30)**: **x̄ ± z_α/2 σ/√n**. For 100 families averaging 1250 units with σ = 150: 1250 ± 1.96 × 15 = 1250 ± 29.4, so **1220.6 ≤ µ ≤ 1279.4**. (The slide prints the upper limit as 1274.40.)
- **σ unknown, large n**: use s in place of σ.
- **Small n**: use **x̄ ± t_α/2,(n−1) s/√n**, from the **t-distribution**. It is symmetric with mean 0 but has heavier tails, and it approaches the normal as the degrees of freedom n − 1 grow.
  - **Dental expenses**: 10 employees with x̄ = 32 and Σ(x − x̄)² = 2358 give s = √(2358/9) = 16.19 and SE = 5.12.
  - With t(9) = 3.250 for 99%, the interval is **32 ± 16.6**. (The slide uses 5.11 as s and t = 1.833.)
- **Proportion**: **p̂ ± z_α/2 √(p̂q̂/n)**. With 48 of 144 families, p̂ = 1/3, so 1/3 ± 1.96 × 0.0393 gives **0.256 to 0.410**.

## Sample size

Setting the margin equal to the tolerable error E gives:

- for a mean, **n = (z_α/2 σ/E)²**. With σ = 8.6, E = 0.5 and 99%, n = (2.576 × 8.6/0.5)² ≈ **1964**;
- for a proportion, **n = z²pq/E²**. With p = 0.10, E = 0.07 and 99%, n = 121.9, so **122** filters.

Always round **up**. Sample size also depends on the study's purpose, how varied the population is, the time, money, staff and equipment available, and the precision required.

Source: STA 121 Lecture 4: Estimation and Confidence Intervals and Lecture 5 Part 1: Sample Size Determination (Olubusoye)
