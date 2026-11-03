# Measures of Variability and the Normal Rules

## Spread

- **Range** = largest − smallest. It is simple, but it uses only two values.
- **Variance**: for a sample, **s² = Σ(x − x̄)²/(n − 1) = (Σx² − (Σx)²/n)/(n − 1)**. The population variance divides by N.
- **Standard deviation** s = √(variance), in the same units as the data.
- The **coefficient of variation** **CV = (s/x̄) × 100%** compares spreads on different scales.

**Example**: for 2, 5, 3, 1, 6 (mean 3.4), Σ(x − x̄)² = 17.2, so s² = 4.3, s = 2.074 and **CV ≈ 61%**.

## The empirical rule

For **bell-shaped (normal)** data:

- about **68%** of values lie within x̄ ± s;
- about **95%** within x̄ ± 2s;
- about **99.7%** within x̄ ± 3s.

**Examples**:

- Heights with mean 65 in and s = 3 in: 59 to 71 is ±2s, so **95%**.
- Scores with mean 75 and s = 5: 70 to 80 covers **68%**, 65 to 85 covers **95%**, and 65 to 75 covers half of 95% = **47.5%**.
- IQ with mean 40 and s = 10: 95% lies between **20 and 60**.
- For x̄ = 70.92 and s = 1.70, the 68% interval is (69.22, 72.62) and the 95% interval (67.52, 74.32).

The empirical rule applies **only to bell-shaped data**.

## Chebyshev's theorem

For **any** data set and any k > 1, at least **1 − 1/k²** of the values lie within k standard deviations of the mean:

- k = 2: at least **3/4**;
- k = 3: at least **8/9**.

**Example**: with x̄ = 15, s = 2 and the interval (9, 21), k = 3, so at least **8/9** of the observations lie in it.

## The normal distribution

The normal curve is symmetric about μ, with mean = median = mode. **z = (x − μ)/σ** converts any normal value to the standard normal, whose probabilities come from z-tables. For example, P(Z < 1.96) = 0.975.

Source: STA 114 Lecture 4: Measures of Variability (Adepoju); STA 111 2025 test; General knowledge of STA 111 for normal z-tables
