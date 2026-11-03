# Extrema, Stationary Points and Optimisation

## Stationary points

A **stationary point** is where **f'(x) = 0**; a **critical point** is where f'(x) = 0 or f' does not exist. They may be a **local maximum**, a **local minimum** or a **point of inflection**.

- **First derivative test**: if f' changes from + to − at c, it is a **local maximum**; from − to +, a **local minimum**; no sign change, neither.
- **Second derivative test**: if f'(c) = 0 and **f''(c) < 0, a local maximum**; **f''(c) > 0, a local minimum**; f''(c) = 0, inconclusive.

For f(x) = x³ − 6x² + 9x, f'(x) = 3(x − 1)(x − 3), so x = 1 and 3. f''(x) = 6x − 12 gives f''(1) = −6 < 0, a **local maximum f(1) = 4**, and f''(3) = 6 > 0, a **local minimum f(3) = 0**.

## Absolute extrema on a closed interval

A continuous function on a closed interval [a, b] **attains an absolute maximum and minimum** (the extreme value theorem). To find them, evaluate f at the **critical points inside (a, b)** and at the **endpoints a and b**, and compare.

## The optimisation method

1. Write the **objective function** to maximise or minimise, using any constraint to reduce it to one variable.
2. Find its derivative, **set it to zero** and solve for critical points.
3. **Classify** with the second derivative (negative for a maximum, positive for a minimum).

## Applied cases

- **Profit**: P = 120x − 2x² − 1500 naira for x bags of rice. P'(x) = 120 − 4x = 0 gives **x = 30 bags**, and P'' = −4 < 0 confirms a maximum of **P(30) = 300 naira**. Profit is positive when x² − 60x + 750 < 0, that is, between the roots 30 ± √150, about **17.75 and 42.25**, so selling **18 to 42 bags** gives a profit.
- **Fencing**: with 200 m of fencing, l + w = 100 and A = w(100 − w). A' = 100 − 2w = 0 gives **w = 50 m and l = 50 m**, a square of **2500 m²**.
- **Cylinder**: for a can of fixed volume V = πr²h, the surface area S = 2πr² + 2πrh = 2πr² + 2V/r is least when S' = 4πr − 2V/r² = 0, which gives **h = 2r**: the height equals the diameter.

Source: MTH201 Study Guide (integration applications, theorems, optimisation) (sections 6 and 9); MTH201 slides 1 (real-valued functions of a real variable) (Extrema of Functions; Finding Absolute Extrema on a Closed Interval); MTH201 slides 2 (integration and optimisation). The study guide factorises x² − 60x + 750 as (x − 15)(x − 50), which is wrong; the correct roots are used here.
