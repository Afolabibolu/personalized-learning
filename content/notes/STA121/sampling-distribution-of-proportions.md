# Sampling Distribution of Proportions

## The sample proportion

When every unit is a **success** or a **failure** (votes for party A or not, a claim filed or not), the **sample proportion** is

**p̂ = x/n** (number of successes ÷ sample size).

It is the best statistic for inference about the population proportion p. For example, 142 of 200 policies had a claim, so p̂ = **0.71**.

## Its sampling distribution

1. **Mean**: µ_p̂ = **p**, so p̂ is unbiased.
2. **Standard error**: σ_p̂ = **√(pq/n)**, where q = 1 − p, when sampling is with replacement. Without replacement, multiply by √((N − n)/(N − 1)).
3. **Shape**: for a large sample (**n ≥ 30**) with **np ≥ 5** and **n(1 − p) ≥ 5**, p̂ is approximately normal. Then **z = (p̂ − p)/√(pq/n)**.

**Example (late invoices)**: p = 0.20 and n = 140.

- σ_p̂ = √(0.2 × 0.8/140) = 0.0338. The slide rounds this to 0.033.
- P(p̂ > 0.28) = P(Z > 0.08/0.033 = 2.42) ≈ **0.008**.

## Difference of two proportions

For independent samples, **p̂₁ − p̂₂** has:

- **mean p₁ − p₂**;
- **standard error √(p₁q₁/n₁ + p₂q₂/n₂)**.

It is close to normal when n₁ and n₂ are both at least 30. For a sum p̂₁ + p̂₂, the mean is p₁ + p₂ and the standard error is the same.

**Example (machines)**: 10% of company A's machines and 5% of B's are defective, with samples of 250 and 300.

- The mean difference is **0.05**.
- The SE = √(0.10 × 0.90/250 + 0.05 × 0.95/300) = **0.0228**.
- P(p̂_A − p̂_B ≤ 0.02) = P(Z ≤ (0.02 − 0.05)/0.0228 = −1.32) = **0.0934**.

## Why it matters

The same standard error, √(pq/n), will give confidence intervals and tests for proportions in the next topics. A smaller standard error needs a larger n. Quadrupling n halves the standard error.

For small populations sampled without replacement, remember the finite correction factor, which approaches 1 when N is large compared with n.

Source: STA 121 Lecture 3: Sampling Distribution of Sample Proportions (Olubusoye); General knowledge of STA 121 for the remark on quadrupling n
