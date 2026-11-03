# Joint, Marginal and Conditional Distributions

## Joint distributions

The **joint probability function** of X and Y, f(x, y), satisfies f(x, y) ≥ 0 and **Σ Σ f(x, y) = 1** or **∫∫ f(x, y) dx dy = 1**. Probabilities of regions are double sums or integrals. For **f(x, y) = 2, x > 0, y > 0, x + y < 1**, the density is constant on a triangle of area 1/2.

## Marginal distributions

The **marginal** of X is found by **summing or integrating out y**: **f_X(x) = Σ_y f(x, y)** or **∫ f(x, y) dy**, and similarly for Y. In a table, the marginals are the **row and column totals**.

**Example**: f(x, y) = (2/3)(x + 2y) on 0 < x < 1, 0 < y < 1 gives **f_X(x) = (2/3)(x + 1)** and **f_Y(y) = (1/3)(1 + 4y)**.

**Example**: for f(x, y) = c(x + y) on 0 ≤ y ≤ x² ≤ 1, the constant c comes from integrating over the region 0 ≤ x ≤ 1, 0 ≤ y ≤ x².

## Conditional distributions

The **conditional density of X given Y = y** is **f(x|y) = f(x, y)/f_Y(y)**, and the **conditional expectation** is **E(X|Y = y) = ∫ x f(x|y) dx**. As a function of y, E(Y|X = x) is the **regression curve** of Y on X.

**Example**: for f(x, y) = (1/4)(2x + y) on 0 < x < 1, 0 < y < 2, f_Y(y) = (1/4)(1 + y), so f(x|y) = (2x + y)/(1 + y), and E(X|Y = y) = (2/3 + y/2)/(1 + y).

## Independence

X and Y are **independent** if and only if **f(x, y) = f_X(x)f_Y(y)** for all x and y. Then E(XY) = E(X)E(Y) and Cov(X, Y) = 0, though zero covariance alone does not prove independence.

## Covariance

**Cov(X, Y) = E(XY) − E(X)E(Y)**. Positive covariance means X and Y tend to increase together; negative, that one rises as the other falls. Also **Var(X ± Y) = Var(X) + Var(Y) ± 2Cov(X, Y)**. The correlation ρ = Cov(X, Y)/(σ_X σ_Y) lies between −1 and 1.

**Example**: if two caplets are drawn from 3 aspirin, 2 sedatives and 4 laxatives, with X aspirin and Y laxatives, the joint probabilities are f(x, y) = C(3, x)C(4, y)C(2, 2 − x − y)/C(9, 2). From the table, E(X), E(Y) and E(XY) give the covariance, which is **negative**: more aspirin leaves less room for laxatives.

## Functions of random variables

The distribution of Y = g(X) is found by the **CDF method**, F_Y(y) = P(g(X) ≤ y), or by **transformation**, f_Y(y) = f_X(g⁻¹(y))|d g⁻¹(y)/dy| for a one-to-one g. For f(x) = 2x on (0, 1) and Y = 8X³, F_Y(y) = P(X ≤ (y/8)^(1/3)) = (y/8)^(2/3), so **f_Y(y) = (1/6)y^(−1/3), 0 < y < 8**.

Source: Amahia, STA 211 Probability II (UI Distance Learning Centre) (Lectures Thirteen and Fourteen); STA 211 Random Variables 2 slides; STA 211 past papers (the joint density, caplets and transformation problems)
