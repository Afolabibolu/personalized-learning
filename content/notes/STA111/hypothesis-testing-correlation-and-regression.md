# Hypothesis Testing, Correlation and Regression

## Hypothesis testing

1. State the **null hypothesis H₀** and the **alternative H₁**.
2. Choose the **level of significance α**, such as 5%.
3. Compute the **test statistic**: z for large samples, t for small samples with unknown σ.
4. Compare it with the **critical value**: accept H₀ if |calculated| ≤ critical, and reject it if larger.
5. Conclude in words.

**Errors**:

- a **Type I error** (probability α) rejects a **true** H₀;
- a **Type II error** (probability β) accepts a **false** H₀.

For fixed α, **a larger sample reduces β**.

**Example**: at 5%, two-sided, the critical z is 1.96. A calculated z of 1.99 exceeds it, so **reject H₀**: there is little evidence to support H₀.

Tests for one mean use z = (x̄ − μ₀)/(σ/√n). Two means use z = (x̄₁ − x̄₂)/√(s₁²/n₁ + s₂²/n₂), or the pooled t for small samples.

## Correlation

A **scatter diagram** shows how two variables vary together: a linear, non-linear or no relationship. **Pearson's correlation coefficient** is

**r = (nΣxy − ΣxΣy)/√[(nΣx² − (Σx)²)(nΣy² − (Σy)²)]**, with −1 ≤ r ≤ 1.

r near +1 means a strong positive relationship, near −1 strong negative, and near 0 weak or none. **Spearman's rank correlation** is **rₛ = 1 − 6Σd²/(n(n² − 1))**, using differences in ranks d; tied ranks are averaged.

**Correlation does not imply causation.** Correlation treats the two variables alike, while in **regression** one variable (**dependent**, y) depends on another (**independent**, x).

## Regression

The **least-squares line** is ŷ = a + bx, with **b = (nΣxy − ΣxΣy)/(nΣx² − (Σx)²)** and **a = ȳ − b x̄**. b is the change in y per unit change in x. Use the line to predict y within the range of the data.

Source: STA 114 Lectures 9 and 10: Hypothesis Testing; Correlation and Regression; STA 111 2025 test
