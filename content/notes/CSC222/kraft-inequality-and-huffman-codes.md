# Kraft Inequality, Expected Length and Huffman Codes

## The Kraft inequality

When can a prefix-free code exist? The **Kraft inequality** is a **necessary and sufficient condition**: there exists a D-ary prefix-free code of N codewords with lengths l₁, l₂, …, l_N **if and only if**

Σᵢ D^(−lᵢ) ≤ 1.

For binary codes (D = 2) with lengths 3, 4, 4, 4, 4, the sum is 1/8 + 4/16 = 3/8 ≤ 1, so such a code exists; with lengths 1, 2, 3, 3, 4 the sum is 1/2 + 1/4 + 1/8 + 1/8 + 1/16 > 1, so no prefix-free code with those lengths exists. A complete binary prefix-free code has a sum of exactly 1. The **classical pitfall** is to forget that the theorem only says **when a prefix-free code may exist**: it does not say that a given code satisfying the inequality is prefix-free.

## Expected code length

If symbol uᵢ has probability pᵢ and codeword length lᵢ, the **expected code length** is

E[L] = Σᵢ pᵢ lᵢ.

We look for prefix-free codes with E[L] as small as possible, so **shorter codewords should go to the most probable symbols**: if pᵢ > pⱼ and l ≥ l′, then pᵢl + pⱼl′ ≥ pᵢl′ + pⱼl, so swapping helps. In a rooted tree with probabilities, the **average depth of the leaves equals the sum of the probabilities of all the nodes**, including the root.

## Optimal codes: Huffman

With the symbols ordered so that p₁ ≥ p₂ ≥ … ≥ p_r, a code is optimal only if l₁ ≤ l₂ ≤ … ≤ l_r. Binary Huffman coding rests on **two basic observations**:

1. In the tree of an optimal binary prefix-free code, **there is no unused leaf**.
2. There is an optimal binary prefix-free code in which **the two least likely codewords differ only in the last digit**: they are siblings.

**Huffman's algorithm** for an optimal binary code follows from these:

1. Create a leaf for each symbol, labelled with its probability.
2. Repeatedly **combine the two least probable nodes** into a new node whose probability is their sum, labelling the two branches 0 and 1.
3. Stop when one node (the root, probability 1) remains; each codeword is read along its path from the root.

For probabilities 0.4, 0.2, 0.2, 0.1 and 0.1, Huffman's algorithm gives codeword lengths such as 1, 2, 3, 4, 4 (or an equally good set), with E[L] = 2.2 bits.

Source: CSC 222 Digital Communication lecture slides (Dr Adeniji Oluwashola David), Lectures 2 and 3 (Kraft inequality, expected code length, optimal codes: Huffman code)
