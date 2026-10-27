# Inequalities, Convergence and Limit Theorems

## Markov's inequality

If X takes only non-negative values and E(X) exists, then for any a > 0:

**P(X ≥ a) ≤ E(X) ÷ a**.

**Proof:** E(X) = ∫ x f(x) dx ≥ ∫ₐ^∞ x f(x) dx ≥ a ∫ₐ^∞ f(x) dx = a P(X ≥ a).

**Example:** a coin lands heads with probability 0.2 and is flipped 20 times. The number of heads X has E(X) = 4, so Markov gives P(X ≥ 16) ≤ 4/16 = **0.25**, far above the true probability (about 1.4 × 10⁻⁸). It is a weak bound.

## Chebyshev's inequality

For any X with mean μ and variance σ², and any k > 0:

**P(|X − μ| ≥ k) ≤ σ² ÷ k²**,

or equivalently P(|X − μ| ≥ kσ) ≤ 1/k². It follows by applying Markov's inequality to the non-negative variable (X − μ)² with a = k².

In the coin example, Var(X) = 20 × 0.2 × 0.8 = 3.2, so P(X ≥ 16) ≤ P(|X − 4| ≥ 12) ≤ 3.2/144 ≈ **0.022**, much better than Markov. For X ~ Exponential(λ), P(|X − 1/λ| ≥ a) ≤ 1/(λ² a²).

## Modes of convergence

A sequence X₁, X₂, … may converge to X:

- **in probability:** P(|Xₙ − X| > ε) → 0 for every ε > 0;
- **in distribution (in law):** Fₙ(x) → F(x) at every point where F is continuous;
- **in mean square:** E[(Xₙ − X)²] → 0;
- **almost surely (with probability 1):** P(Xₙ → X) = 1.

Almost-sure and mean-square convergence each imply convergence in probability, which implies convergence in distribution.

## The weak law of large numbers

If X₁, X₂, … are independent with common mean μ and finite variance σ², the sample mean X̄ₙ = (X₁ + … + Xₙ)/n satisfies

**P(|X̄ₙ − μ| ≥ ε) ≤ σ² ÷ (nε²) → 0**,

so X̄ₙ converges to μ **in probability**, by Chebyshev's inequality. This justifies the relative-frequency view of probability.

## The central limit theorem

If X₁, X₂, … are independent and identically distributed with mean μ and variance σ², then

**Zₙ = (X̄ₙ − μ) ÷ (σ/√n)**

converges **in distribution** to the standard normal N(0, 1). So sums and averages of many independent variables are approximately normal, whatever their original distribution.

## Normal approximation to the binomial

For large n, Binomial(n, p) is approximately Normal(np, npq), with a **continuity correction** of ±0.5. A common rule is to use it when np and nq both exceed about 5.

Source: general knowledge, following the MAT 352 course outline and past papers (2020/21 Question 4a and 2021/22 Question 4, and the course outline's modes of convergence and elementary limit theorems)
