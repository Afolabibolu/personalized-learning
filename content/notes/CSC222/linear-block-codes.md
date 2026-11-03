# Linear Block Codes and Syndrome Decoding

## Linear codes

**Linear codes** are block codes with an added algebraic structure, the **vector space**, which helps decoding. An **(n, m) D-ary linear code** (1 ≤ m ≤ n) is an **m-dimensional subspace** of the vector space GF(D)ⁿ of n-tuples. So:

- **Every linear code contains the null codeword 0.** {1101, 0110, 1110} is not linear because 0000 is missing.
- {0000, 1101, 0110, 1011} is a **(4, 2) binary linear code**: any linear combination of codewords is a codeword, its dimension is 2 and its length 4.
- An (n, m) D-ary linear code has **Dᵐ codewords**, so codes whose number of codewords is not a power of D cannot be linear.
- Its **transmission rate** is **R = m / n**.

The **weight** of a codeword is its number of non-zero symbols. For a linear code, **the minimum distance equals the minimum weight** (the smallest weight of a non-zero codeword): the (11, 3) code {00000000000, 10011110000, …} has minimum weight 5, so its minimum distance is 5. A code with minimum distance 3 can correct all single errors.

## Encoding

A **generator matrix** G of an (n, m) linear code is an m × n matrix whose m rows are a **basis** of the code. A message u of m symbols is encoded as **z = u · G**; the null message always becomes the null codeword. For the (4, 2) code above with basis 1101 and 0110, u = 10 gives 1101, u = 01 gives 0110, and u = 11 gives 1011. G is in **systematic form** if its left-most m × m block is the identity, so the **first m symbols of each codeword are the message itself** and only the last n − m are redundant; such a code is a **systematic code**.

**Parity-check bit encoding** sends the message followed by its **parity-check bit**, the binary sum of its bits: 01101 gets 1 and 00101 gets 0. It is the (m + 1, m) binary linear code.

## Decoding

A **verification (parity-check) matrix** H satisfies z · Hᵀ = 0 for every codeword z. If an error e occurs and ẑ = z + e is received, then **ẑ · Hᵀ = e · Hᵀ**, which depends only on the error. This value is the **syndrome**. The decoder:

1. **computes the syndrome** s = ẑ · Hᵀ;
2. **looks up the correction** for that syndrome in a table stored in memory, built from the columns of H (the null syndrome means no correction);
3. **adds the correction** to ẑ to recover the codeword, and from it the message.

When the minimum distance is 3, every single-error pattern has its own syndrome, but some syndromes of two errors are not unique.

Source: CSC 222 Digital Communication lecture slides (Dr Adeniji Oluwashola David), Lecture 4 (linear codes) and slides 4 and 5 (Linear Block Codes; Syndrome Decoding)
