# Confidence Intervals for Means and Proportions

## Why intervals

Even the best unbiased estimator rarely equals the parameter, and a point estimate says nothing about its precision. A **(1 − α) confidence interval** has limits L(X) and U(X) chosen so that **P[L(X) ≤ θ ≤ U(X)] = 1 − α**. Typical levels are 90%, 95% and 99%, with **z = 1.645, 1.96 and 2.576**.

## The mean, σ known

From x̄ ~ N(μ, σ/√n), the pivot (x̄ − μ)/(σ/√n) ~ N(0, 1) gives

**CI(μ) = x̄ ± z(1−α/2) σ/√n**,

where **z σ/√n is the margin of error**. **Example**: n = 30, σ = 2.5 and Σx = 77 give x̄ = 2.5667 and a 95% interval **[1.67, 3.46]**. **Example** (2020/21): heights with σ = 2, n = 16 and x̄ = 6.2 give a 90% interval 6.2 ± 1.645(0.5) = **5.378 to 7.022 feet**.

**Example** (2012/13): 64 peptic ulcer patients with mean stay 8.25 days and σ = 3: the standard error is 0.375, so the 95% interval is 8.25 ± 0.735 = **[7.515, 8.985]** and the 90% interval is 8.25 ± 0.617.

## The mean, σ unknown

If **n ≥ 30**, replace σ by s and keep z. If **n < 30** and the population is normal, use the **t-distribution with n − 1 degrees of freedom**:

**x̄ ± t(α/2, n−1) s/√n**.

The t-distribution is needed when the sample is small *and* σ is unknown. With n = 25 the two-sided 95% value is t(0.025, 24) = 2.064.

## A proportion

With x successes in n, **p̄ = x/n** and, for large n,

**p̄ ± z(α/2) √(p̄(1 − p̄)/n)**.

**Example**: 10 defectives in 800 calculators give p̄ = 0.0125 and a 99% interval 0.0125 ± 2.575(0.003928) = **[0.0025, 0.0226]**. **Example** (2020/21): 201 of 300 believed the accused guilty, so 99 did not; p̄ = 0.33 and the 95% interval for "not guilty" is **0.277 to 0.383**.

## Width

The interval is **narrower for larger n** and **wider for higher confidence**. Lowering confidence from 98% to 90% narrows the interval but does **not** change the standard error σ/√n. For a fixed level, the margin of error falls as 1/√n.

Source: STA 221 Lecture 2 (Interval Estimation); STA 221 past papers; General knowledge of STA 221 for the t value with 24 degrees of freedom
