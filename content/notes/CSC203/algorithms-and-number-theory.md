# Algorithms, Big-O and Number Theory

## Algorithms

An **algorithm** is a **finite set of precise instructions** for performing a computation or solving a problem. Its properties are **input** and **output** from specified sets, **definiteness** of every step, **correctness** for every input, **finiteness** of the number of steps, **effectiveness** of each step and **generality** for a class of problems. Examples are finding the maximum element in a finite sequence, **linear search** (compare the target with each term in turn) and **binary search**, which works on an **ordered** list by repeatedly halving the part that can contain the target. Binary search is much faster on long lists.

## Growth and big-O

What matters about an algorithm's time or space complexity is how it **grows** with the input size, not its value for small inputs. **Big-O notation** describes growth: f(x) is **O(g(x))** if there are constants C and k with |f(x)| ≤ C|g(x)| whenever x > k. Linear search uses O(n) comparisons and binary search O(log n); a polynomial of degree d is O(xᵈ).

## Applications of number theory

For integers a ≠ 0 and b, **a divides b** (a | b) if b = ac for some integer c. A **prime** is an integer greater than 1 whose only positive divisors are 1 and itself. By the **fundamental theorem of arithmetic**, every integer greater than 1 is a product of primes in exactly one way, apart from order.

The **greatest common divisor** gcd(a, b) is the largest integer dividing both, so gcd(48, 72) = 24; a and b are **relatively prime** if gcd(a, b) = 1, and a · b = gcd(a, b) · lcm(a, b). The **Euclidean algorithm** replaces (a, b) by (b, a mod b) until the remainder is 0: gcd(287, 91) = gcd(91, 14) = gcd(14, 7) = 7.

**a ≡ b (mod m)** when m divides a − b. Congruences give **classical ciphers**: number the letters A = 0 to Z = 25, then **Caesar's cipher** shifts each letter three places, f(p) = (p + 3) mod 26. A **shift cipher** with key k uses (p + k) mod 26 and decrypts with (p − k) mod 26; an **affine cipher** uses (ap + b) mod 26.

Source: CSC 203.pdf (CSC 203 topics and logic note) (topics 3 and 4); CSC 242.pdf (Discrete Structures slides, filed in the CSC 203 folder), the algorithms and number theory sections
