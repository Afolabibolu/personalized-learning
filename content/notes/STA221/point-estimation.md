# Point Estimation

## Estimation

**Estimation** is the process of using a sample value as an estimate of an unknown population value (**parameter**). The formulas computed from the sample are **estimators**; their values are **estimates**. There are two types: **point** estimation (one value) and **interval** estimation (a range).

The usual estimators are **x̄ = Σx/n** for μ, **S² = (Σx² − (Σx)²/n)/(n − 1)** for σ², and **p̂ = x/n** for P. Population parameters are written with Greek letters (μ, σ) and statistics with Roman ones (x̄, S², p̂).

## Properties of a good estimator

1. **Unbiasedness**: an estimator T is unbiased if **E(T) = θ**. **S² with divisor n − 1 is unbiased** for σ²; **Σ(xi − x̄)²/n is biased**. For a Poisson sample, E(x̄) = λ, so x̄ is unbiased for λ.
2. **Efficiency**: among unbiased estimators, the one with the **smallest variance** is most efficient. In general efficiency is judged by the **mean squared error**, **MSE(T) = E[(T − θ)²] = Var(T) + (Bias)²**, where Bias = E(T) − θ, and eff(T) = 1/MSE(T).
3. **Consistency**: as n grows, the probability that the estimator is close to θ tends to one; in practice **Var(θ̂) → 0** and θ̂ becomes unbiased as n → ∞.
4. **Robustness**: the estimate is not seriously affected by a wrong distributional assumption or by atypical values. The **median** is robust (making the largest value 1000 times larger leaves it unchanged); its partner for spread is the **MAD = median|xi − sample median|**.

## Relative efficiency

The efficiency of T1 relative to T2 is **eff(T1, T2) = MSE(T2)/MSE(T1)**, which for unbiased estimators is **Var(T2)/Var(T1)**. A value above 1 means T1 is more efficient.

**Example** (Lecture 1, set again in 2018/19): for n = 5 from an exponential distribution with mean θ, T1 = x̄ and T2 = (2X1 + X2 + X3 − X4 + 3X5)/6 are both unbiased. Var(T1) = θ²/5 and Var(T2) = 16θ²/36 = 4θ²/9, so eff(T1, T2) = (4/9)/(1/5) = **20/9 > 1**: T1 is more efficient.

**Example** (2018/19): for X ~ Binomial(n, π), T1 = X/n has MSE π(1 − π)/n. T2 = (X + 1)/(n + 2) is biased, with bias (1 − 2π)/(n + 2). With n = 100 and π = 0.4, MSE(T1) = 0.0024 and MSE(T2) ≈ 0.00231, so **T2 has the smaller MSE** despite its bias.

**Example** (2020/21): BMI values 23.0, 21.0, 18.5, 17.0, 18.0, 19.0 and 20.5 have mean **19.6** and variance (divisor n − 1) **4.2**.

Source: STA 221 Lecture 1 (Estimation); STA 221 past papers
