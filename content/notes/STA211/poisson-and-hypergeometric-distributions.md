# The Poisson and Hypergeometric Distributions

## The Poisson distribution

The **Poisson distribution** models the number of occurrences of a **rare event** in a fixed interval of time or space, such as calls per minute or defects per metre:

**f(x) = λˣ e^(−λ)/x!**, x = 0, 1, 2, ..., λ > 0.

The probabilities sum to 1 because Σ λˣ/x! = e^λ. Its **mean and variance are both λ**: E(X) = V(X) = λ. Using the **mgf M(t) = e^(λ(e^t − 1))**, M'(t) = λe^t M(t) gives **M'(0) = λ**, and M''(0) = λ² + λ, so Var(X) = λ² + λ − λ² = **λ**. (Papers write the parameter as λ or θ.)

**Example**: if accidents occur at an average rate of 2 a week, P(no accident in a week) = e^(−2) ≈ 0.135, and P(at most one) = e^(−2)(1 + 2) ≈ 0.406.

## Approximation and sums

When **n is large and p is small**, Bin(n, p) is approximately **Poisson with λ = np**. For example, with n = 200 and p = 0.01, P(X = 0) ≈ e^(−2). If X and Y are **independent** Poisson variables with means λ1 and λ2, then **X + Y is Poisson with mean λ1 + λ2**, as the product of their mgfs shows.

## The hypergeometric distribution

A population of **N** items contains **M "successes"** (for example, defectives) and N − M failures. A sample of **n** is drawn **without replacement**. The number of successes X has

**P(X = x) = C(M, x) C(N − M, n − x) / C(N, n).**

Its **mean is nM/N**, and its variance is n(M/N)(1 − M/N)(N − n)/(N − 1); the factor **(N − n)/(N − 1)** is the **finite population correction**.

**Example**: 3 sets are chosen at random from 12 electronic sets of which 2 are defective (white cords). P(no defective sent) = C(10, 3)/C(12, 3) = 120/220 = **6/11**.

**Example**: if 5 of 12 senators are from the north and 3 are chosen, P(exactly one northerner) = C(5, 1)C(7, 2)/C(12, 3) = 105/220 = **21/44**.

## Hypergeometric or binomial?

Use the **hypergeometric** when sampling **without replacement** from a small population, since the trials are then **dependent**. When N is large relative to n, the hypergeometric is close to the **binomial** with p = M/N.

Source: Amahia, STA 211 Probability II (UI Distance Learning Centre) (Lectures Nine and Ten); STA 211 past papers (Poisson mean and variance, electronic sets and senators problems)
