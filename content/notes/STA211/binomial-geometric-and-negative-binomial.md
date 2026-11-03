# Bernoulli, Binomial, Geometric and Negative Binomial Distributions

## Bernoulli trials

A **Bernoulli trial** has two outcomes, **success** with probability p and **failure** with probability q = 1 − p. A Bernoulli variable has mean p and variance pq.

## The binomial distribution

X ~ Bin(n, p) counts the successes in **n independent Bernoulli trials with the same p**:

**P(X = x) = C(n, x) pˣ qⁿ⁻ˣ**, x = 0, 1, ..., n.

**Properties**: (1) a fixed number n of trials; (2) each trial has two outcomes; (3) the trials are **independent**; (4) p is **constant** from trial to trial. Its **mean is np**, its **variance is npq** (so the standard deviation depends on n, p and q), and its **mgf is (q + pe^t)ⁿ**. The probabilities sum to 1 because Σ C(n, x)pˣqⁿ⁻ˣ = (p + q)ⁿ = 1.

**Example**: a fair die thrown four times, with "six" as success (p = 1/6): P(no six) = (5/6)⁴ ≈ 0.482, P(four sixes) = (1/6)⁴ ≈ 0.00077, and **P(at least one six) = 1 − (5/6)⁴ ≈ 0.518**.

**Combining**: if X ~ Bin(10, 0.4) and Y ~ Bin(20, 0.5), then Var(X) = 2.4 and Var(Y) = 5. If X and Y are **independent**, Var(X + Y) = 7.4; if they are dependent with Cov(X, Y) = 2.5, **Var(X − Y) = Var(X) + Var(Y) − 2Cov(X, Y) = 2.4**.

## The geometric distribution

X counts the trials up to and including the **first success**:

**f(x) = pqˣ⁻¹**, x = 1, 2, 3, ...,

with **mean 1/p**, **variance q/p²** and mgf **pe^t/(1 − qe^t)** for qe^t < 1. It is **memoryless**: P(X > m + n | X > m) = P(X > n).

## The negative binomial distribution

X counts the trials up to the **kth success**:

**P(X = x) = C(x − 1, k − 1) pᵏ qˣ⁻ᵏ**, x = k, k + 1, ...,

because the last trial must be a success and k − 1 successes must occur in the first x − 1 trials. Its **mean is k/p** and **variance kq/p²**. The geometric distribution is the case **k = 1**.

Source: Amahia, STA 211 Probability II (UI Distance Learning Centre) (Lectures Seven and Eight); STA 211 past papers (binomial properties, die and Var(X − Y) items). The memoryless property is from general knowledge of STA 211.
