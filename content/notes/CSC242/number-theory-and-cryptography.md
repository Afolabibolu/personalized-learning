# Number Theory and Cryptography

## Divisibility and primes

For integers a and b, **a divides b** (written a | b) if there is an integer c with b = ac; then a is a **factor** of b. A positive integer p greater than 1 is **prime** if its only positive factors are 1 and p; otherwise it is **composite**. The **fundamental theorem of arithmetic** states that every positive integer greater than 1 can be written uniquely as a **product of primes**, the prime factors in non-decreasing order. A composite n has a prime divisor no greater than √n.

The **greatest common divisor** gcd(a, b) is the largest integer that divides both. The common divisors of 48 and 72 are 1, 2, 3, 4, 6, 8, 12 and 24, so gcd(48, 72) = 24. From prime factorisations, gcd takes the smaller exponent of each prime. Integers are **relatively prime** if their gcd is 1, and a set is **pairwise relatively prime** if every pair is: 15, 17 and 27 are not, because gcd(15, 27) = 3. Also **a · b = gcd(a, b) · lcm(a, b)**.

The **Euclidean algorithm** finds the gcd by repeated division: gcd(287, 91) = gcd(91, 14) = gcd(14, 7) = 7, because 287 = 3 · 91 + 14 and 7 | 14. Recursively, gcd(a, b) = b if a = 0, else gcd(b mod a, a).

**a is congruent to b modulo m**, a ≡ b (mod m), if m divides a − b, that is, a and b leave the same remainder on division by m.

## Cryptography

Number theory plays a key role in **cryptography**, the subject of transforming information so that it cannot easily be recovered without special knowledge. The classical ciphers are **private key ciphers**. **Julius Caesar** made messages secret by **shifting each letter three letters forward** in the alphabet. Mathematically, each letter is replaced by an element of Z₂₆, one less than its position: A = 0, K = 10, Z = 25. Encryption is then f(p) = (p + 3) mod 26. A **shift cipher** uses any key k, f(p) = (p + k) mod 26, decrypted by (p − k) mod 26; an **affine cipher** uses f(p) = (ap + b) mod 26.

**Cryptanalysis** breaks a cipher without the key. A shift cipher has only 25 possible keys, so all can be tried. **Frequency analysis** compares letter counts in the ciphertext with ordinary English, where E, T and A are the most common letters. **Transposition ciphers** rearrange letters, for example by writing them in columns under a keyword.

Source: CSC 242.pdf (Discrete Structures lecture slides), the number theory section; cryptograpy.pdf (the cryptanalysis and transposition paragraph is written from general knowledge, because the cryptography file stops after numbering the letters)
