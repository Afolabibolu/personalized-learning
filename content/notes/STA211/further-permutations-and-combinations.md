# Further Permutations and Combinations

## Counting

If one step can be done in n1 ways and a second in n2 ways, together they can be done in **n1·n2** ways. **n! = n(n − 1)...1** and **0! = 1**.

## Permutations

The number of **ordered arrangements of r objects from n distinct objects** is **nPr = n!/(n − r)!**. Three-digit numbers from the digits 1 to 8 number **8P3 = 336** without repetition and **8³ = 512** with repetition. If nP4 = 20·nP2, then (n − 2)(n − 3) = 20, so **n = 7**.

**Permutations of alike objects**: n objects with n1 of one kind, n2 of another and so on, can be arranged in **n!/(n1! n2! ... nk!)** ways. **Circular** arrangements of n distinct objects number **(n − 1)!**.

## Combinations

The number of **unordered selections of r from n** is **nCr = C(n, r) = n!/(r!(n − r)!)**, and **nPr = r!·nCr**.

Restricted selections are counted by fixing the restriction first. A team of 11 from 14 players can be chosen in C(14, 11) = **364** ways; teams **including the captain** number C(13, 10) = **286**, and teams **excluding the captain** C(13, 11) = **78** (286 + 78 = 364).

## Identities

These appear in nearly every paper:

- **Symmetry**: **C(n, r) = C(n, n − r)**. So if C(10, r) = C(10, r − 2), then r + (r − 2) = 10 and r = 6; and if nC12 = nC8, then n = 20, so 20C17 = 1140 and 22Cn = 22C20 = 231.
- **Pascal's rule**: **C(n, r) + C(n, r − 1) = C(n + 1, r)**, equivalently C(n, r) = C(n − 1, r) + C(n − 1, r − 1). Proof: choosing r from n + 1 either includes a particular object (C(n, r − 1) ways) or excludes it (C(n, r) ways).
- **Vandermonde's identity**: **Σ from r = 0 to k of C(m, r)C(n, k − r) = C(m + n, k)**: choose k from m men and n women by choosing r men and k − r women.
- **C(n, r) = (n/(n − r))·C(n − 1, r)**, from the factorial definitions.

## The binomial expansion

**(a + b)ⁿ = Σ C(n, r) aʳ bⁿ⁻ʳ**, which is why C(n, r) is called a **binomial coefficient**. Setting a = b = 1 gives **Σ C(n, r) = 2ⁿ**, the number of subsets of a set of n elements.

Source: Amahia, STA 211 Probability II (UI Distance Learning Centre) (Lectures One and Two); STA 211 Permutation and Combination slides; STA 211 past papers
