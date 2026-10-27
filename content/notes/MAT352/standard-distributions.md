# Standard Discrete and Continuous Distributions

## Discrete distributions

- **Bernoulli(p):** one trial, success (1) with probability p and failure (0) with probability q = 1 − p. The mean is p and the variance pq.
- **Binomial(n, p):** the number of successes in n independent Bernoulli trials. Its pmf is P(X = x) = C(n, x) pˣ qⁿ⁻ˣ for x = 0, 1, …, n. Mean **np**, variance **npq**, MGF (q + peᵗ)ⁿ.
- **Geometric(p):** the number of trials up to the first success. Its pmf is P(X = x) = q^(x − 1) p for x = 1, 2, …. Mean **1/p**, variance **q/p²**, MGF peᵗ ÷ (1 − qeᵗ).
- **Poisson(λ):** the number of events in a fixed interval. Its pmf is P(X = x) = e^(−λ) λˣ / x! for x = 0, 1, 2, …. Mean and variance both **λ**, MGF e^(λ(eᵗ − 1)). It approximates the binomial when n is large and p small, with λ = np.

## Continuous distributions

- **Uniform(a, b):** f(x) = 1/(b − a) on [a, b]. Mean **(a + b)/2**, variance **(b − a)²/12**.
- **Exponential(λ):** f(x) = λe^(−λx) for x > 0. Mean **1/λ**, variance **1/λ²**, MGF λ/(λ − t). It is **memoryless**: P(X > s + t | X > s) = P(X > t). It models waiting times.
- **Gamma(α, λ):** f(x) = λ^α x^(α − 1) e^(−λx) / Γ(α) for x > 0. Mean **α/λ**, variance **α/λ²**, MGF (1 − t/λ)^(−α). With α = 1 it is the exponential.
- **Normal(μ, σ²):** f(x) = (1/√(2πσ²)) e^(−(x − μ)²/(2σ²)). Mean **μ**, variance **σ²**, MGF e^(μt + σ²t²/2). The **standard normal** Z = (X − μ)/σ has mean 0 and variance 1.

## Summary table

| Distribution | Type | Mean | Variance |
| --- | --- | --- | --- |
| Binomial(n, p) | discrete | np | npq |
| Geometric(p) | discrete | 1/p | q/p² |
| Poisson(λ) | discrete | λ | λ |
| Uniform(a, b) | continuous | (a + b)/2 | (b − a)²/12 |
| Exponential(λ) | continuous | 1/λ | 1/λ² |
| Gamma(α, λ) | continuous | α/λ | α/λ² |
| Normal(μ, σ²) | continuous | μ | σ² |

## Choosing a distribution

- Use the **binomial** for a fixed number of independent yes/no trials.
- Use the **geometric** for waiting until the first success.
- Use the **Poisson** for counts of rare events in time or space.
- Use the **exponential** or **gamma** for waiting times.
- Use the **normal** for sums and averages of many small effects.

Source: Lanre_s 352 note.pdf (a student's handwritten MAT 352 lecture notes, used as secondary) (binomial distribution and its MGF); MAT 352 Assignment (gamma distribution); the other distributions are general knowledge, following the MAT 352 course outline and past papers (the scanned CA, Question 3, and the 2023/24 test)
