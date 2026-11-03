# Uniform, Normal, Exponential, Gamma and Chi-square Distributions

## The uniform distribution

X ~ U(a, b) has **f(x) = 1/(b − a), a ≤ x ≤ b**. Its **mean is (a + b)/2**, **variance (b − a)²/12**, and mgf **(e^(bt) − e^(at))/(t(b − a))**. Probabilities are proportional to lengths.

**Example**: a measurement error is uniform on (−0.015, 0.015), so f(x) = 1/0.03. P(0.01 < X < 0.02) = (0.015 − 0.01)/0.03 = **1/6**, since the error cannot exceed 0.015; and P(|X| > 0.005) = 0.02/0.03 = **2/3**.

## The normal distribution

X ~ N(μ, σ²) has the bell-shaped density **f(x) = (1/(σ√(2π))) e^(−(x−μ)²/(2σ²))**, symmetric about μ. It is standardised by **Z = (X − μ)/σ ~ N(0, 1)**, and probabilities come from **standard normal tables**. Its mgf is **e^(μt + σ²t²/2)**.

**Example**: if X ~ N(μ, 100) and P(X > 16.34) = 0.1212, then (16.34 − μ)/10 = 1.17 (since P(Z > 1.17) = 0.1210), so **μ ≈ 4.64**.

## The exponential distribution

**f(x) = θe^(−θx), x > 0**, models **waiting times** between Poisson events. Its **mean is 1/θ** and **variance 1/θ²**, and it is **memoryless**. With θ = 3, f(x) = 3e^(−3x), F(x) = 1 − e^(−3x) and E(X) = 1/3. If X1, X2, X3 are independent with densities e^(−x1), 2e^(−2x2) and 3e^(−3x3), their **joint density** is the product, **6e^(−x1 − 2x2 − 3x3)** for positive x1, x2, x3.

## The gamma distribution

X ~ Gamma(α, β) has

**f(x) = x^(α−1) e^(−x/β) / (β^α Γ(α))**, x > 0,

where **Γ(α) = ∫ from 0 to ∞ of x^(α−1) e^(−x) dx**, with Γ(n) = (n − 1)! for whole numbers. Its **mgf is (1 − βt)^(−α)**, so M'(0) = αβ gives the **mean αβ** and the **variance is αβ²**. The exponential is the case α = 1 (with β = 1/θ).

## The chi-square distribution

The **chi-square distribution with ν degrees of freedom** is the gamma with **α = ν/2 and β = 2**, so its **mean is ν** and **variance 2ν**. If Z ~ N(0, 1), then **Z² is chi-square with 1 degree of freedom**, and sums of independent chi-squares add their degrees of freedom. If X ~ U(0, 1), then **Y = −2 ln X** is chi-square with 2 degrees of freedom (an exponential with mean 2).

Source: Amahia, STA 211 Probability II (UI Distance Learning Centre) (Lectures Eleven, Twelve and Fifteen); STA 211 past papers (uniform error, normal mean, gamma mgf and joint density problems)
