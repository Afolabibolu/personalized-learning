# Intervals for Variances and Differences, and Sample Size

## A variance

For a normal population the pivot **(n − 1)S²/σ² ~ χ²(n − 1)**, so

**CI(σ²) = [(n − 1)s²/χ²(1−α/2), (n − 1)s²/χ²(α/2)]**,

using the upper and lower chi-square points. Taking square roots gives an interval for σ. The pivot is **not robust** to non-normality, so the sample should be checked for normality first; otherwise non-parametric methods are more appropriate.

**Example** (2013/14): ten times with s = 4.5 seconds: (n − 1)s² = 182.25, and χ²(9) has points 19.023 and 2.700, so σ² lies in [9.58, 67.5] and **σ in about [3.10, 8.22]** with 95% confidence.

## A ratio of variances

For two independent normal samples, **(S1²/σ1²)/(S2²/σ2²) ~ F(n1 − 1, n2 − 1)**, which gives an interval for σ1²/σ2².

## Differences

- **Two means, σ known**: **(x̄1 − x̄2) ± z √(σ1²/n1 + σ2²/n2)**. Heights of 10 girls and 10 boys (59.8 and 58.5, σ = 2 and 3) give 1.3 ± 1.96(1.140), so the 95% interval is about **[−0.94, 3.54]**.
- **Two means, σ unknown but equal**: pool **sp² = ((n1 − 1)s1² + (n2 − 1)s2²)/(n1 + n2 − 2)** and use t with n1 + n2 − 2 degrees of freedom.
- **Unequal variances** (2018/19 asks for this): use s1²/n1 + s2²/n2 with approximate degrees of freedom.
- **Two proportions**: **(p̂1 − p̂2) ± z √(p̂1q̂1/n1 + p̂2q̂2/n2)**.

## Sample size

The **bound on the error** (margin of error) is **B = z(1−α/2) σ/√n**, so

**n = (z σ / B)²**, rounded **up**.

**Example**: to be 95% confident that [x̄ − 1, x̄ + 1] contains μ when σ = 5, n = (1.96 × 5)² = 96.04, so **n = 97**.

For a proportion, **n = z² p(1 − p)/B²**, using p = 0.5 when nothing is known. **Example** (2010/11 CA): with p = 0.08 and B = 0.06 at 95%, n = 3.8416(0.0736)/0.0036 = 78.5, so **79**.

When σ is unknown, the range R of preliminary data gives **σ ≈ R/4** (2009/10).

Source: STA 221 Lecture 3 (Interval Estimation II); STA 221 Lecture 4 (Sample Size Determination); STA 221 past papers; General knowledge of STA 221 for the unequal-variance interval and the chi-square table values
