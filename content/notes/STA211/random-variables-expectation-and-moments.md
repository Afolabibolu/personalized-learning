# Random Variables, Expectation, Moments and Chebyshev's Inequality

## Probability functions

A **probability density function** satisfies **f(x) ≥ 0** and **Σ f(x) = 1** (discrete) or **∫ f(x) dx = 1** (continuous). The **cumulative distribution function** is **F(x) = P(X ≤ x)**, and for continuous X, **f(x) = F'(x)** and P(a < X ≤ b) = F(b) − F(a).

Constants are found from the total: for **f(x) = k(8 − x), x = 0, 1, ..., 5**, Σ(8 − x) = 33, so **k = 1/33**. For **f(x) = ke^(−3x), x > 0**, ∫ ke^(−3x) dx = k/3 = 1, so **k = 3**, and P(0.5 ≤ X ≤ 1) = e^(−1.5) − e^(−3) ≈ 0.173.

## Expectation

**E(X) = Σ x f(x)** or **∫ x f(x) dx**, and **E[g(X)] = Σ g(x) f(x)** or **∫ g(x) f(x) dx**. Expectation is linear: **E(aX + b) = aE(X) + b** and **E[g1(X) + g2(X)] = E[g1(X)] + E[g2(X)]**.

An expectation may **not exist**: for **f(x) = (1/2)ˣ, x = 1, 2, ...**, E(2^X) = Σ 2ˣ(1/2)ˣ = Σ 1, which **diverges**.

For **f(x) = 2(1 − x), 0 < x < 1**, E(X^q) = 2∫(x^q − x^(q+1)) dx = **2/((q + 1)(q + 2))**; so E(X) = 1/3 and E(X²) = 1/6.

## Variance and moments

**Var(X) = E(X²) − [E(X)]²** and **Var(aX + b) = a²Var(X)**. The **rth moment about the origin** is **μ'r = E(Xʳ)**, and the **rth moment about the mean** is **μr = E[(X − μ)ʳ]**. The **first moment about the mean is zero** and the **second is the variance**. The third central moment in terms of raw moments is **μ3 = μ'3 − 3μ'2μ + 2μ³**.

## Moment generating functions

The **moment generating function (mgf)** is **M_X(t) = E(e^(tX))**. Its derivatives at 0 give the moments: **E(X) = M'(0)** and **E(X²) = M''(0)**, and the mgf **uniquely determines** the distribution. For a Poisson variable, **M(t) = e^(λ(e^t − 1))**, giving E(X) = Var(X) = λ.

## Chebyshev's inequality

For any random variable with mean μ and variance σ², and k > 0,

**P(|X − μ| < kσ) ≥ 1 − 1/k²**, equivalently P(|X − μ| ≥ kσ) ≤ 1/k².

It needs **no knowledge of the distribution**. If μ = 12 and σ² = 9, then P(6 < X < 18) = P(|X − 12| < 2·3) **≥ 1 − 1/4 = 3/4**.

Source: Amahia, STA 211 Probability II (UI Distance Learning Centre) (Lectures Five and Six); STA 211 Random Variables 2 slides; STA 211 past papers
