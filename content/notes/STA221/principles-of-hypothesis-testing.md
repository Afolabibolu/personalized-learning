# Principles of Hypothesis Testing

## The set-up

A **statistical hypothesis** is a statement about a population parameter. The **null hypothesis H0** (for example μ = μ0) is tested against the **alternative H1** (μ > μ0, μ < μ0 or μ ≠ μ0). A **simple** hypothesis fixes the parameter at one value; a **composite** one allows a range. A **test statistic** is computed from the sample, and the **critical (rejection) region** is the set of its values that leads to rejecting H0. H1 with > or < gives a **one-tailed** test; ≠ gives a **two-tailed** test.

General steps: state H0 and H1; choose α; choose the test statistic; find the critical region; compute the statistic; decide and conclude in words.

## Errors

| Decision | H0 true | H0 false |
| --- | --- | --- |
| Reject H0 | **Type I error** (α) | Correct (power) |
| Do not reject H0 | Correct (1 − α) | **Type II error** (β) |

The **significance level α** is the probability of a Type I error; 1 − α is the **confidence coefficient**. In a trial, convicting an innocent defendant is a Type I error and acquitting a guilty one a Type II error.

**Example** (2010/11 CA): to test θ = 0.6 against θ = 0.5 with five births, rejecting when X < 3, α = P(X ≤ 2 | θ = 0.6) = 0.0102 + 0.0768 + 0.2304 = **0.317**, β = P(X ≥ 3 | θ = 0.5) = 16/32 = **0.5**, and power = 0.5.

## Calculating β

For a right-tailed z test, **x̄crit = μ0 + zcrit σ/√n**, and β is the area to the left of x̄crit under the normal curve centred at the true mean μa. (Left-tailed: μ0 − zcrit σ/√n; two-tailed: both.)

**Example** (Lecture 7): testing μ = 11 against μ > 11 for debit card use, with α = 0.01, n = 36 and σ = 3, x̄crit = 11 + 2.33(0.5) = 12.165. If μa = 13, **β = P(Z < (12.165 − 13)/0.5) = P(Z < −1.67) = 0.0475**.

**Example**: with σ = 6, testing μ = 40 and rejecting when x̄ < 36 or x̄ > 44 for n = 9, α = P(Z < −2) + P(Z > 2) = **0.0455**.

## Power

The **power** is the probability of rejecting H0 when it is false: **power = 1 − β**, a function of the true θ. At θ0, power equals α. Power increases when **α is increased**, when **n is increased**, or when the **difference between θ1 and θ0 is larger**. For fixed α, a larger n decreases β.

Source: STA 221 Lecture 7 (Hypothesis Testing II, file Lecture 6.pdf); STA 221 past papers
