# Source Coding and Prefix-Free Codes

## Why code?

There are basically **three purposes of coding**:

1. **Compressing data**: reducing, on average, the length of messages by **removing redundancy**.
2. **Ensuring quality of transmission in noisy conditions**: **adding redundancy** so that messages can be corrected despite noise.
3. **Secrecy**: making the message impossible, or hard, to read for unauthorised readers.

For compression, if some symbols are more probable than others, we can assign **shorter codewords to more frequent symbols**. Such codes have codewords of **varying length**, which raises the problem of recognising where one codeword ends and the next begins.

## Sources and codes

An **information source** is a message generator: a generator of sequences of **symbols**, elements of a set called an **alphabet**. When the alphabet is finite the source is **discrete**, and the size of its alphabet is its **arity**; a newspaper is a discrete source whose symbols are letters. The source is **memoryless** if the probability of emitting a symbol does not depend on the symbols emitted before. An **encoder** turns messages into sequences of **codewords**, each a non-empty sequence of symbols from the coding alphabet.

- A code is **non-singular** when different source symbols map to different codewords.
- A code is **non-ambiguous** if every finite sequence of codewords can be decoded in only one way. For symbols a, b, c, the code a → 1, b → 00, c → 11 is **ambiguous**, since "aaaa" and "cc" both give 1111; a → 1, b → 00, c → 10 is non-ambiguous (10000 decodes as abb).
- A code is **prefix-free** when **no codeword is the prefix of another**.
- A code is **instantaneously decodable** if each codeword can be decoded as soon as its end is reached. **A code is instantaneously decodable if and only if it is prefix-free**, and every prefix-free code is non-ambiguous.

For example, with z₁ = 0, z₂ = 10, z₃ = 110 and z₄ = 111, the message 1423312 encodes as 011110110110010, and 1001101010 decodes as 21322.

## Coding trees

A code over an alphabet of size n is an **n-ary code**. Any binary code can be drawn as a **binary tree**: each bit is a decision to go up (0) or down (1), so each codeword is a path from the root to a leaf. An **n-ary tree** has exactly n children at every interior node, and a **full** n-ary tree has all leaves at the same depth. When there is **no unused leaf** in the coding tree, the code is **complete**.

Source: CSC 222 Digital Communication lecture slides (Dr Adeniji Oluwashola David), Lecture 2 (Information Compression and Error Correction: source coding)
