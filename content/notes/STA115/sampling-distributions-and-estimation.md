# Sampling Distributions and Point Estimation

## Terms

- A **population** (size N) is everything under study, and a **sample** (size n) is a representative part of it.
- A **parameter** (µ, σ, P) is a population value. It is fixed: a constant.
- A **statistic** (x̄, s, p̂) is computed from a sample, so it **varies from sample to sample**.
- The **sampling distribution** of a statistic is its distribution over all possible samples of size n.

## The sample mean

For any population, **E(x̄) = µ**.

- **With replacement** (or an infinite population), **Var(x̄) = σ²/n**.
- **Without replacement** from a finite population, Var(x̄) = **(σ²/n) × (N − n)/(N − 1)**. The factor (N − n)/(N − 1), the **finite population correction**, approaches 1 as N grows.

**Example**: the population {3, 5, 6, 8, 2, 9} has µ = 5.5 and σ² = 6.25.

- The 6C2 = 15 samples of size 2 without replacement give E(x̄) = 5.5.
- Var(x̄) = (6.25/2)(4/5) = **2.5**, matching the direct calculation.

For balls numbered 1 to 6 (σ² = 2.9167), samples of 2 give Var(x̄) = 1.4583 with replacement and 1.1667 without. The sample mean's expectation is µ either way.

For large n, x̄ is approximately normal (the **central limit theorem**). For two independent normal populations, **x̄ − ȳ ~ N(µₓ − µᵧ, σₓ²/nₓ + σᵧ²/nᵧ)**.

## The sample proportion

**E(p̂) = P** and the **standard error** is **√(PQ/n)**. For a family of 2 boys and 1 girl, P = 2/3, and samples of 2 with replacement give SE = √((2/3)(1/3)/2) = **1/3**.

For **sums or differences** of independent proportions, the mean is P₁ ± P₂ and the SE is **√(P₁Q₁/n₁ + P₂Q₂/n₂)**. (The slide repeats P₁Q₁ in the second term.) With proportions A = (1/5, 2/5) and B = (1/2, 1/3, 1/6), the mean of the sum is 3/10 + 1/3 = **19/30**.

## Estimation

- An **estimator** is the statistic used, and the **estimate** is its value.
- A **point estimate** is one number (x̄ for µ, p̂ for P).
- An **interval estimate** gives a range, such as "95% confident that µ is between 40 and 60".
- A **population total** is estimated by N × x̄: 1000 groups with a sample mean of 17 give **17,000**.
- An estimator is **unbiased** if its expected value equals the parameter, as with x̄ for µ.

Source: STA 115 Lectures 8 to 10: Sampling Distributions I to III (Shittu; Dr O.E. Olubusoye) and Inference 1: Point Estimation (Dr A.U. Chukwu); STA 115 tests (2016/17 to 2023) and STA 112 Probability I papers; General knowledge of STA 115 for the central limit theorem and unbiasedness
