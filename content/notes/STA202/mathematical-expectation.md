# Mathematical Expectation

## Expected value

The **mean (expected value)** of a random variable X is

**μ = E(X) = Σ x f(x)** (discrete) or **∫ x f(x) dx** (continuous).

**Example**: a shipment of 8 microcomputers contains 3 defective ones, and a school buys 2 at random. With X the number of defective computers bought, f(0) = 10/28, f(1) = 15/28 and f(2) = 3/28, so **E(X) = 0(10/28) + 1(15/28) + 2(3/28) = 21/28 = 0.75**.

**Example**: if a device's life X (hours) has pdf f(x) = 20,000/x³ for x > 100, then E(X) = ∫ from 100 to ∞ of 20,000/x² dx = **200 hours**.

## Expectation of a function

For a function g(X), **E[g(X)] = Σ g(x) f(x)** or **∫ g(x) f(x) dx**.

## Rules of expectation

- **E(c) = c** for a constant c.
- **E(aX + b) = aE(X) + b**: expectation is **linear**.
- **E(X + Y) = E(X) + E(Y)** for any X and Y.
- **E(XY) = E(X)E(Y)** if X and Y are **independent**.

If E(X + 4) = 10, then E(X) = **6**.

## Variance

The **variance** is **σ² = Var(X) = E[(X − μ)²] = E(X²) − [E(X)]²**, and the **standard deviation** σ is its square root. Rules:

- **Var(c) = 0**;
- **Var(aX + b) = a²Var(X)**: adding a constant does not change the spread; and
- **Var(X + Y) = Var(X) + Var(Y)** if X and Y are independent.

If E(X) = 6 and E[(X + 4)²] = 116, then E(X²) + 8E(X) + 16 = 116 gives E(X²) = 52, so Var(X) = 52 − 36 = **16**, and **Var(2X + 4) = 4 × 16 = 64**.

## Moments

The **rth moment about the origin** is **μ'r = E(Xʳ)**; the **rth moment about the mean** is **μr = E[(X − μ)ʳ]**. The **first moment about the mean is zero** and the **second moment about the mean is the variance**. Higher moments describe shape: the third measures **skewness** and the fourth **kurtosis**. They are related by **μ3 = μ'3 − 3μ'2μ + 2μ³**. A **moment generating function** M(t) = E(e^(tX)) produces moments by differentiation: E(X) = M'(0) and E(X²) = M''(0).

Source: STA 204 Lecture 5 (Mathematical Expectation); STA 201/202/204 quiz (2024/2025 session). The moment relations and the worked variance example follow the STA 211 papers filed in this folder.
