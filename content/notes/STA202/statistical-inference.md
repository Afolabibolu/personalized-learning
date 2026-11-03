# Sampling Distributions, Estimation and Hypothesis Testing

## Sampling distributions

A sample taken from a population **represents** it. The distribution of a statistic over repeated samples is its **sampling distribution**. The **standard error of the mean** is **σ/√n**: with σ = 35 and n = 9, it is 35/3 = **11.67**. For the difference of two independent means, the standard error is √(σ1²/n1 + σ2²/n2).

## Estimation

An estimator is **unbiased** if the **mean of its sampling distribution equals the population parameter**; x̄ is an unbiased estimator of μ. A **point estimate** is a single value; a **confidence interval estimate** is a **range of values likely to contain the parameter at a stated confidence level**, such as x̄ ± 1.96σ/√n for 95% confidence.

## Hypothesis testing

A test compares a **null hypothesis H0** (no effect or no difference, such as H0: μ = 1500) with an **alternative H1**. A **one-sided (lower-tailed)** test uses H1: μ < 1500; a **two-sided** test uses H1: μ ≠ 1500. The **p-value** is the probability of results at least as extreme as those observed if H0 is true; if it is below the **significance level α** (often 0.05), reject H0.

- A **Type I error** is **rejecting H0 when it is true**; its probability is α.
- A **Type II error** is **failing to reject H0 when it is false**; its probability is β.

## Choosing a test

- **z-test**: for a mean when the **population standard deviation is known** (or n is large).
- **t-test**: when σ is unknown and estimated by s, for one sample, two independent samples or paired data.
- **F-test**: for comparing variances, and in **ANOVA** for comparing several means.
- **Chi-square (χ²) test**: for categorical data, testing **association** or goodness of fit, and for a specified population variance. With χ² = 5.8 on 1 degree of freedom (critical value 3.84 at α = 0.05 and 6.63 at α = 0.01), **H0 is rejected at the 5% level** but not at 1%.
- **Non-parametric tests** make fewer assumptions about the distribution.

## Correlation and regression

The **correlation coefficient r**, between −1 and +1, measures the strength of a **linear** relationship; **r close to 1** means a **strong positive linear relationship**. **Simple linear regression** fits Y = α + βX + ε, with **β̂ = Σ(X − X̄)(Y − Ȳ)/Σ(X − X̄)² = cov(X, Y)/Var(X)** and α̂ = Ȳ − β̂X̄. Correlation does not prove causation.

**Association** measures the relationship between **attributes** (qualitative characteristics). For attributes A and B in N items, if (AB) < (A)(B)/N, the association is **negative**; if greater, positive.

Source: STA 204 Lecture 6 (Follow-up class: summary statistics, tests, regression) (hypothesis testing, t-tests, confidence intervals, correlation and regression, choosing the right test); STA 201/202/204 quiz (2024/2025 session) (inference items). Critical values and the regression formulas are from general knowledge of STA 202.
