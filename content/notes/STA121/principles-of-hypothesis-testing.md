# Principles of Hypothesis Testing

## Hypotheses

A **statistical hypothesis** is a claim about a population parameter, which may or may not be true. Testing it means judging whether the difference between a sample statistic and the claimed value is too large to be chance. The theory comes from Neyman and Pearson.

- The **null hypothesis H₀** states a specific value, such as µ = µ₀ ("machines A and B are equally efficient").
- The **alternative H₁** is its opposite: µ ≠ µ₀, µ < µ₀ or µ > µ₀.
- A **simple** hypothesis fully specifies the distribution. A **composite** one does not.

## The steps

1. State H₀ and H₁.
2. Choose the **level of significance α** (0.10, 0.05 or 0.01) **before** seeing the data.
3. Set the **critical (rejection) region** and the **acceptance region**. They are separated by the **critical value**.
4. Compute the **test statistic** = (sample statistic − hypothesised value)/standard error.
5. Conclude. **Reject H₀** if the statistic falls in the critical region (|calculated| ≥ critical value); otherwise do not reject it.

## One and two tails

- **Two-tailed**: H₁: µ ≠ 20. Half of α goes in each tail.
- **Left-tailed**: H₁: µ < 20.
- **Right-tailed**: H₁: µ > 20.

In a one-tailed test, all of α sits in one tail.

## Errors and power

| Decision | H₀ true | H₀ false |
| --- | --- | --- |
| Reject H₀ | **Type I error** (probability α) | correct |
| Accept H₀ | correct | **Type II error** (probability β) |

- 1 − α is the confidence coefficient.
- **1 − β is the power**, the probability of rejecting a false H₀.
- For a fixed α, a **larger n lowers β** and raises the power.
- For a fixed n, a smaller α raises β. To reduce both, increase n.

(One slide writes β as P(reject H₀ | H₁ true). It is P(accept H₀ | H₁ true).)

Courts give a picture, with H₀ = "innocent":

- jailing an innocent woman is a **Type I** error;
- freeing guilty men is a **Type II** error.

## The p-value

The **p-value** is the probability of a result at least as extreme as the one observed, if H₀ is true:

- P(Z > z*) for a right-tailed test;
- P(Z < z*) for a left-tailed test;
- 2P(Z > |z*|) for a two-tailed test.

**Reject H₀ if p ≤ α.** The smaller the p-value, the stronger the evidence against H₀. Below 0.01 is strong, and below 0.001 very strong.

Source: STA 121 Lecture 5: Testing of Hypothesis (Olubusoye), the 2018 Lecture 5: Hypothesis Testing (Dr O.I. Shittu) and Principle of Hypothesis Testing (Dr A.U. Chukwu)
