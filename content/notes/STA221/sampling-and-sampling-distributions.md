# Sampling and Sampling Distributions

## Why sample

A **population** is every unit of interest; a **sample** is the part observed. Sampling is preferred to **complete enumeration** because it is cheaper and faster, the population may be infinite or hard to reach, testing may destroy the unit, and a well-run sample can be more accurate than a hurried census.

## Sampling methods

**Probability (random) methods**: **simple random** sampling (every sample of size n equally likely), **stratified** (random samples within groups), **cluster** (whole groups chosen at random), **systematic** (every kth unit after a random start) and **multistage**. **Non-probability methods**: **quota**, **convenience**, **purposive** and **snowball** (subjects refer the researcher to others).

**Sampling error** is the chance difference between a statistic and its parameter; **non-sampling error** comes from bias, wrong measurement, non-response and recording mistakes. The theory of sampling rests on **statistical regularity** and the **inertia of large numbers**.

## The sampling distribution of the mean

A **sampling distribution** is the distribution of a **statistic** over all possible samples. For the mean, **E(x̄) = μ**, and its standard deviation, the **standard error**, is **σ/√n** when sampling with replacement (or from an infinite population). Without replacement from a population of N it is **(σ/√n)√((N − n)/(N − 1))**, the finite population correction.

If the population is normal, x̄ is exactly normal. If not, the **central limit theorem** makes x̄ approximately normal for large n (n ≥ 30). With σ unknown and a normal population, (x̄ − μ)/(s/√n) follows the t-distribution with **n − 1** degrees of freedom.

**Example** (2012/13): ages 3, 5 and 7, so μ = 5 and σ² = 8/3. With replacement there are 3² = 9 samples of size two, and σx̄ = √(4/3) = 1.155. Without replacement the samples are (3, 5), (3, 7), (5, 7), with means 4, 5, 6, so μx̄ = 5 and σx̄ = √(2/3) = **0.816**, matching (8/3 ÷ 2)(1/2).

**Example**: bulbs with μ = 1500 and σ = 100 in boxes of 25 give x̄ with mean 1500 and standard error **20**; with μ = 36, σ = 15 and n = 49, P(x̄ < 33) = P(Z < −1.4) = **0.0808**.

## Proportions and differences

The sample proportion p̂ has mean p and standard error **√(pq/n)**; it is approximately normal when **np ≥ 5 and nq ≥ 5**. With p = 0.5 and a standard error of 0.01, n = 0.25/0.0001 = **2500**. For two independent samples, x̄1 − x̄2 has mean μ1 − μ2 and variance **σ1²/n1 + σ2²/n2**.

Source: STA 221 course outline (STA 221_merged.pdf); STA 221 past papers; STA 221 Lecture 1 (Estimation) (the sampling distribution example); General knowledge of STA 221 for the methods, as no slides on sampling are in the folder
