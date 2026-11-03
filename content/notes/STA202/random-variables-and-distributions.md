# Random Variables and Probability Distributions

## Random variables

A **random variable** X takes values with given probabilities. **Discrete** random variables have a **countable** number of outcomes (dead/alive, dice, counts); **continuous** ones have an **infinite continuum** of values (blood pressure, weight, speed).

- A **probability mass function (pmf)** p(x) gives P(X = x), with **0 ≤ p(x) ≤ 1 and Σ p(x) = 1**. For a fair die, p(x) = 1/6 for x = 1, ..., 6.
- A **probability density function (pdf)** f(x) for a continuous variable satisfies f(x) ≥ 0 and **∫ f(x) dx = 1**; probabilities are areas, **P(a ≤ X ≤ b) = ∫ from a to b of f(x) dx**, and P(X = a) = 0.
- The **cumulative distribution function (CDF)** is **F(x) = P(X ≤ x)**, rising from 0 to 1; for a die it steps up by 1/6 at each value. For a continuous variable, f(x) = F'(x).

An unknown constant k in a pdf is found from ∫ f = 1: f(x) = k/(π(1 + x²)) on 0 < x < 1 gives k(1/π)(π/4) = 1, so **k = 4**.

## Binomial distribution

With **n independent trials**, each a success with probability **p** (q = 1 − p),

**P(X = x) = C(n, x) pˣ qⁿ⁻ˣ**, with **mean np** and **variance npq**,

so the standard deviation √(npq) depends on **n, p and q**. A batter with 205 hits in 522 at bats has p = 205/522, so in 529 at bats the expected number of hits is 529 × 205/522 ≈ **208**.

## Poisson distribution

For counts of rare events with mean λ, **P(X = x) = e^(−λ)λˣ/x!**, x = 0, 1, 2, ..., with **mean and variance both λ**. It approximates the binomial when n is large and p small, with λ = np.

## Uniform distribution

On [a, b], **f(x) = 1/(b − a)**, with **mean (a + b)/2** and **variance (b − a)²/12**.

## Normal distribution

The **normal distribution** N(μ, σ²) is bell-shaped and symmetric about μ. It is standardised by **z = (x − μ)/σ**, giving the standard normal N(0, 1). A woman 72 inches tall, when heights have μ = 65.5 and σ = 2.5, has **z = 2.6**. The **empirical rule**: about **68%** of values lie within 1σ of μ, **95%** within 2σ and **99.7%** within 3σ. So with IQ scores N(100, 15²), about **2.5%** score above 130 (z = 2).

Source: STA 204 Lecture 4 (Probability Distributions); Probability Distributions Guide; STA 201/202/204 quiz (2024/2025 session) (binomial, z-score and normal items). The Poisson and uniform formulas follow the probability distributions guide.
