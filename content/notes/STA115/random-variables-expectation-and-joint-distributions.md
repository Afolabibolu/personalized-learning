# Random Variables, Expectation and Joint Distributions

## Random variables

A **variable** is a characteristic with at least two possible values. It can be qualitative (sex, ability) or quantitative (age, yield). A **random variable** is a **real-valued function defined on a sample space**. For three coin tosses, X = the number of heads takes the values 0 to 3. An experiment such as "tossing a coin twice" is not itself a variable.

- A **discrete** random variable takes a finite or countable set of values.
- A **continuous** one takes any value in an interval, with **P(X = a) = 0** for every single value.

## Discrete distributions

A probability mass function f(x) = P(X = x) must satisfy **f(x) ≥ 0** and **Σ f(x) = 1**. The **distribution function** is F(x) = P(X ≤ x). For f(x) = x/6, x = 1, 2, 3: P(X ≥ 2) = 5/6 and E(X) = 14/6 = 7/3.

The **expected value** is **E[X] = Σ x f(x)**. For example, a wheel pays 1, 5 or 30 with probabilities 0.50, 0.45 and 0.05: E = 0.5 + 2.25 + 1.5 = **4.25**. With a $5 stake, the game is **not fair**: the house gains 75 cents per play on average.

**Rules**:

- E[a + bX] = a + bE[X];
- **Var(X) = E[(X − µ)²] = E[X²] − µ²**;
- Var(b) = 0;
- **Var(aX + b) = a²Var(X)**.

The rth moment about the mean is E[(X − µ)ʳ], and the coefficient of variation is σ/µ.

## Continuous distributions

A pdf satisfies f(x) ≥ 0, ∫f(x)dx = 1, and P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx. The cdf is F(x) = ∫ f(t)dt from −∞ to x.

**Example**: for f(x) = k(1 − x²) on −1 < x ≤ 1, k × 4/3 = 1 gives **k = 3/4**, and P(−0.5 ≤ X ≤ 1) = F(1) − F(−0.5) = 1 − 5/32 = **27/32**.

## Joint and marginal distributions

A **joint pmf** f(x, y) = P(X = x, Y = y) is non-negative and sums to 1. The **marginal** of X is found by summing (or integrating) over y. X and Y are **independent** if f(x, y) = f_X(x) f_Y(y) for all x, y.

**Example**: roll two dice, with A = the maximum and B = the sum.

- f_A(a) = **(2a − 1)/36**.
- f_B(b) = (6 − |b − 7|)/36.
- P(A = 3, B = 7) = 0, but P(A = 3)P(B = 7) ≠ 0, so A and B are **not independent**.

**Continuous example**: f(x, y) = (2/3)(x + 2y) on the unit square has marginals f_X(x) = (2/3)(x + 1) and f_Y(y) = (1/3)(1 + 4y).

Source: STA 115 Lecture 4: Random Variables (Shittu) and Lecture 7: Joint and Marginal Probability Distribution (Shittu, 2021); STA 115 tests (2016/17 to 2023) and STA 112 Probability I papers
