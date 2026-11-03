# Introduction to Number Theory

## Integers and primes

Under + and ·, the integers are associative, commutative and distributive, with identities 0 and 1 and additive inverses −a. (Z, ≤) is ordered: for any a and b exactly one of a < b, a = b, a > b holds. If a = nb, a is a **multiple** of b and b a **factor** of a. An integer P > 1 whose only factors are ±1 and ±P is **prime**. By the **Fundamental Theorem of Arithmetic**, every integer n ≥ 2 can be written uniquely as a product of primes.

## The division algorithm and the gcd

**Euclidean (division) algorithm**: for any integer a and positive integer b there are unique integers q and r with **a = bq + r and 0 ≤ r < b**. A **common divisor** d of a and b divides both; if every common divisor divides d, d is the **greatest common divisor**, gcd(a, b). The **lowest common multiple** [a₁, …, aₙ] is a common multiple that divides every other one. a and b are **relatively prime (coprime)** if gcd(a, b) = 1. Divisibility rules include: m | n implies m | kn, and m | n and m | s imply m | (n + s).

Since gcd(a, b) = gcd(b, r), repeated division finds the gcd, and reversing the steps writes it as **d = au + bv**. For example, gcd(540, 168) = 12 = 540(5) + 168(−16); gcd(2598, 1124) = 2 = 2598(167) + 1124(−386); and gcd(−28, 45) = 1 = −28(8) + 45(5).

## Modular arithmetic

**a ≡ r (mod m)** reads "a is congruent to r modulo m": a = mq + r with 0 ≤ r < m. Congruence partitions Z into the classes [0], [1], …, [m − 1]; for m = 3, [0] = {…, −3, 0, 3, 6, …}. The set **Zₘ = {0, 1, …, m − 1}** is the **residue class of integers modulo m**, with addition and multiplication done modulo m and shown in Cayley tables. The number of elements of Zₘ relatively prime to m is **Euler's phi function (the totient) φ(m)**: φ(10) = |{1, 3, 7, 9}| = 4.

## Congruence equations

For **ax ≡ 1 (mod m)**: if gcd(a, m) = 1 there is one solution; if gcd(a, m) > 1 there is none. So 7x ≡ 1 (mod 9) has x = 4, while 11x ≡ 1 (mod 33) has no solution. For large m, use d = ax + my: 1 = 81(−79) + 256(25) solves 81x ≡ 1 (mod 256). For **ax ≡ b (mod m)**, if d = gcd(a, m) divides b, divide through by d: 6x ≡ 3 (mod 9) reduces to 2x ≡ 1 (mod 3).

Source: MAT 213 Full.pdf (Algebra I lecture notes, B. O. Onasanya), Chapter 4 (Introduction to Number Theory)
