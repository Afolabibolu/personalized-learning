# First-Order Differential Equations

## Separable equations

If dy/dx = g(x)h(y), separate and integrate: ∫ dy/h(y) = ∫ g(x) dx. For dy/dx = ky, ln y = kt + c, so y = Ce^(kt).

## Homogeneous equations

dy/dx = f(x, y) is **homogeneous** if f(tx, ty) = f(x, y), that is, f can be written as a function of y/x. M(x, y) is **homogeneous of degree n** if M(tx, ty) = tⁿM(x, y). Solve with the substitution **y = vx**, so dy/dx = v + x dv/dx, which makes the equation separable in v and x. For example, (x² + xy) dy/dx = xy − y² is homogeneous of degree 2.

## Exact equations

M(x, y) dx + N(x, y) dy = 0 is **exact** if it is the total differential dF of some F(x, y). **Theorem**: if M and N have continuous first partial derivatives, the equation is **exact if and only if ∂M/∂y = ∂N/∂x**. Then find F by integrating M with respect to x (adding a function of y), choose that function so that ∂F/∂y = N, and the solution is **F(x, y) = C**.

For 3x(xy − 2) dx + (x³ + 2y) dy = 0: M = 3x²y − 6x and N = x³ + 2y, so ∂M/∂y = 3x² = ∂N/∂x, and the equation is **exact**. F = x³y − 3x² + y², so the solution is **x³y − 3x² + y² = C**.

## Integrating factors

A non-exact equation can be multiplied by an **integrating factor** μ to make it exact. If (∂M/∂y − ∂N/∂x)/N depends on x alone, μ(x) = e^(∫ that dx); if (∂N/∂x − ∂M/∂y)/M depends on y alone, μ(y) = e^(∫ that dy).

## Linear first-order equations

The equation **dy/dx + P(x)y = Q(x)** has integrating factor **μ = e^(∫P dx)**. Multiplying gives d(μy)/dx = μQ, so **y = (1/μ)(∫ μQ dx + C)**. For dy/dx + y cot x = cos x, μ = e^(∫cot x dx) = sin x, so d(y sin x)/dx = sin x cos x, and **y sin x = (1/2)sin²x + C**. An equation can also be linear in x, as dx/dy + p(y)x = q(y), which is how y² dx + (3xy − 1) dy = 0 is solved.

## Bernoulli equations

**dy/dx + P(x)y = Q(x)yⁿ** (n ≠ 0, 1) is a **Bernoulli equation**. Dividing by yⁿ and substituting **v = y^(1−n)** turns it into a **linear** equation in v: dv/dx + (1 − n)Pv = (1 − n)Q.

Source: MAT 241 class slides (A. O. Akeju) (Chapter 3: homogeneous, exact, non-exact and Bernoulli types); MAT 241 past papers. The worked exact and linear examples are calculated here from the past papers.
