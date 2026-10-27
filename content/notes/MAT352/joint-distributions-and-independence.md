# Joint Distributions, Independence and Transformations

## Joint distributions

Two random variables X and Y have a **joint pmf** p(x, y) = P(X = x, Y = y), or a **joint pdf** f(x, y) ≥ 0 with ∬ f(x, y) dx dy = 1, so that

P((X, Y) ∈ A) = ∬_A f(x, y) dx dy.

**Example:** f(x, y) = C x y² for 0 ≤ y ≤ x ≤ 1 is valid when C ∫₀¹ ∫₀ˣ x y² dy dx = C ∫₀¹ x⁴/3 dx = C/15 = 1, so **C = 15**.

## Marginal and conditional distributions

The **marginal** densities come from integrating out the other variable:

**f_X(x) = ∫ f(x, y) dy**, and f_Y(y) = ∫ f(x, y) dx.

The **conditional density** of X given Y = y is

**f_(X|Y)(x | y) = f(x, y) ÷ f_Y(y)**,

and the **conditional expectation** is E(X | Y = y) = ∫ x f_(X|Y)(x | y) dx.

## Stochastic independence

X and Y are **independent** if and only if **f(x, y) = f_X(x) f_Y(y)** for all x and y, with the joint density factorising over a product region. For the triangle 0 ≤ y ≤ x ≤ 1 above, the support is not a rectangle, so X and Y are **not** independent.

**Covariance** is Cov(X, Y) = E(XY) − E(X)E(Y), and the **correlation** is ρ = Cov(X, Y) ÷ (σ_X σ_Y), between −1 and 1. Independent variables have zero covariance, but **zero correlation does not imply independence**.

**Example:** if Y is uniform on [0, 2π], A = sin Y and B = cos Y are **uncorrelated** (E(AB) = E(A) = E(B) = 0) but **not independent**, since A² + B² = 1.

## Sums of independent random variables

If X and Y are independent:

- E(X + Y) = E(X) + E(Y);
- Var(X + Y) = Var(X) + Var(Y);
- M_(X + Y)(t) = Mₓ(t) M_Y(t).

The density of Z = X + Y is the **convolution** f_Z(z) = ∫ f_X(x) f_Y(z − x) dx. Examples:

- Poisson(λ₁) + Poisson(λ₂) is Poisson(λ₁ + λ₂);
- the sum of n independent Exponential(λ) is Gamma(n, λ);
- sums of independent normals are normal.

## The change-of-variable technique

If Y = g(X), with g one-to-one and differentiable, then

**f_Y(y) = f_X(g⁻¹(y)) · |d g⁻¹(y) / dy|**.

**Example:** if X is uniform on (0, 1), Y = −ln X has density e^(−y) for y > 0, which is Exponential(1).

For two variables, the joint density of the new pair is found with the **Jacobian** of the inverse transformation.

Source: general knowledge, following the MAT 352 course outline and past papers (2020/21 Questions 2b, 3a and 3b, 2021/22 Questions 5a and 6b); the student's notes do not reach joint distributions
