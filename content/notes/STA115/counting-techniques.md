# Counting Techniques

## The basic principle of counting

If one experiment has n₁ outcomes, a second has n₂ for each of those, and so on, then together they have **n₁ × n₂ × ... × nₖ** outcomes. A store with 3 laptop brands, 2 carrying cases and 4 RAM options offers 3 × 2 × 4 = **24** combinations.

## Sampling with and without replacement

**With replacement**, each object is put back before the next is chosen, so there are **nᵏ** ordered samples of size k. Four-digit licence plates allow repeated digits, giving 10⁴ = **10,000** plates.

**Without replacement**, the number of ordered samples, called **permutations**, is

**nPk = n(n − 1)...(n − k + 1) = n!/(n − k)!**

The first three places in a race of four runners can be decided in 4P3 = 4 × 3 × 2 = **24** ways.

When some objects are **identical**, with n₁ alike, n₂ alike and so on, the count falls to **n!/(n₁! n₂! ... nₖ!)**. DATA has 4!/2! = **12** arrangements.

## Combinations

When order does not matter, as with a committee, the count is the **combination**

**nCk = n!/(k!(n − k)!)**

Three people chosen from eight can form 8C3 = **56** committees. Note that nCk = nPk/k! and nCk = nC(n − k).

**Example**: sequences of three letters from A, B, C and D:

- no repetition, order matters: 4 × 3 × 2 = 24;
- repetition allowed: 4³ = 64;
- order ignored: 4C3 = 4. (The slide repeats the committee answer of 56 here. The correct count is 4.)

**Partitions**: assigning nine people to committees of sizes 2, 3 and 4 gives 9C2 × 7C3 × 4C4 = 9!/(2! 3! 4!) = **1260** ways.

## Circular arrangements and restrictions

n distinct objects in a **circle** can be arranged in **(n − 1)!** ways, because rotations are the same arrangement. A necklace, which can also be turned over, has (n − 1)!/2. For restrictions such as "couples stand together", treat each block as one object and then arrange within the blocks. For example, 4 couples can stand in 4! × 2⁴ = 384 ways.

The **binomial theorem**, (a + b)ⁿ = Σ nCr aⁿ⁻ʳ bʳ, uses the same coefficients and appears in STA 112 papers.

Source: STA 115 Lecture 1: Counting Techniques (Prof. O.I. Shittu, 2023); STA 115 tests (2016/17 to 2023) and STA 112 Probability I papers; General knowledge of STA 115 for circular arrangements and the binomial theorem
