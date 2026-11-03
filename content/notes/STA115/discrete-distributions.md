# Discrete Distributions: Bernoulli, Binomial and Poisson

## Bernoulli

A **Bernoulli trial** has exactly two outcomes, success with probability p and failure with q = 1 − p, and trials are independent.

- p(x) = pˣ(1 − p)¹⁻ˣ for x = 0, 1.
- **E(X) = p** and **Var(X) = pq**.

For a 3 on one die: E = 1/6 and Var = 5/36.

## Binomial

A **binomial experiment** has:

- n identical, independent trials;
- two outcomes per trial;
- a constant p.

X counts the successes:

**P(X = x) = nCx pˣ qⁿ⁻ˣ, x = 0, 1, ..., n**, with **mean np** and **variance npq**.

**Examples**:

- Guessing 100 four-option questions: mean 25 right, SD √(100 × 1/4 × 3/4) = **4.33**.
- Five fair coin tosses: P(exactly 3 heads) = 10/32 = **0.3125**, and P(at least 3) = 1/2.
- Bolts with 20% bad, 4 chosen: P(at most 2) = 1 − P(3) − P(4) = 1 − 0.0256 − 0.0016 = **0.9728**.
- 500 families of 5 children: about 500 × 10/32 ≈ **156** have exactly 2 boys.

## Poisson

The **Poisson** distribution counts independent random events in a fixed interval of time or space:

**P(X = k) = e^(−λ) λᵏ/k!, k = 0, 1, 2, ...**, with **mean = variance = λ**.

**Examples**:

- Lightning kills on average 3 people a year in the UK, so P(exactly 1) = 3e⁻³ ≈ **0.15**.
- Messages arrive at 1.2 per second, so in 2 seconds λ = 2.4 and P(5) ≈ 0.060.

Events must be independent. Floods affecting many homes at once, or planes landing on a fixed schedule, are not Poisson.

**Approximation**: for large n and small p, the binomial is close to the Poisson with **λ = np** (say n > 30 and np < 5). For 100,000 babies with p = 0.00002, λ = 2.

## Without replacement and waiting times

- The **hypergeometric** distribution is used when selections are **not replaced**: from N items with K successes, P(X = x) = (KCx)((N − K)C(n − x))/(NCn), with mean nK/N.
- The **geometric** distribution gives the number of trials up to the first success: P(X = k) = qᵏ⁻¹p. Drawing from items that are 40% defective, P(first defective on the 3rd draw) = 0.6² × 0.4 = 0.144.

Source: STA 115 Lecture 5: Discrete Univariate Distributions: Bernoulli, Binomial and Poisson (Shittu, 2023; Dr A.U. Chukwu, 2018); STA 115 tests (2016/17 to 2023) and STA 112 Probability I papers; General knowledge of STA 115 for the hypergeometric and geometric distributions
