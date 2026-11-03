# Tests on Means, Proportions and Variances

## One mean

With σ known (or n large), **z = (x̄ − μ0)/(σ/√n)**; with σ unknown and a small normal sample, **t = (x̄ − μ0)/(s/√n)** with n − 1 degrees of freedom. Reject H0 when |z| > z(1−α/2) for a two-tailed test, or in the one tail named by H1.

**Example** (2011/12): 49 individuals average 130 heartbeats with σ² = 100: z = (130 − 125)/(10/7) = **3.5 > 1.96**, so the mean differs from 125.

## Two means

With known variances, **z = ((x̄ − ȳ) − (μx − μy))/√(σx²/nx + σy²/ny)**. If σ1 and σ2 are unknown and the samples are large, use s1 and s2 instead.

**Example** (Lecture 8, set in 2012/13): sickness absence averages 2.03 and 1.28 days, with 65 workers in each part and variance estimates 3.0125 and 2.1482. SE = √((3.0125 + 2.1482)/65) = 0.282, so **z = 0.75/0.282 = 2.66 > 1.96**: the means differ.

For small samples with equal variances, use the **pooled t test**: **t = (x̄1 − x̄2)/(sp√(1/n1 + 1/n2))** with **n1 + n2 − 2** degrees of freedom. **Example** (visual acuity, set in several years): n = 11 and 14, means 26 and 21, s = 5 and 6. sp² = (10 × 25 + 13 × 36)/23 = 31.2, so t = 5/(5.587 × 0.403) = **2.22 > t(23) = 2.069**: reject equal means at 0.05.

## Proportions

One proportion: **z = (p̂ − p0)/√(p0q0/n)**. **Example** (2020/21): 100 of 250 had check-ups, so z = (0.4 − 0.5)/0.0316 = **−3.16** and p = 0.5 is rejected.

Two proportions: pool **p̄ = (x1 + x2)/(n1 + n2)** and use **z = (p̂1 − p̂2)/√(p̄q̄(1/n1 + 1/n2))**. **Example**: insurance in 129 of 150 and 144 of 160 patients gives p̄ = 0.881 and z ≈ **−1.09**, so p1 = p2 is not rejected at 0.05.

## Variances

One variance: **χ² = (n − 1)s²/σ0²** with n − 1 degrees of freedom. **Example** (2011/12): nine patients with s = 2 testing σ² < 5 gives χ² = 8(4)/5 = 6.4. That is above the lower 5% point 2.733, so H0 is not rejected.

Equality of two variances: **F = s1²/s2²** with (n1 − 1, n2 − 1) degrees of freedom, usually with the larger variance on top for a two-tailed test.

All these tests assume random, independent samples, and the t, chi-square and F tests assume normal populations.

Source: STA 221 Lecture 8 (Hypothesis Testing II, file Lecture 7_1.pdf); STA 221 past papers; General knowledge of STA 221 for the one-sample and chi-square variance tests and the table values
