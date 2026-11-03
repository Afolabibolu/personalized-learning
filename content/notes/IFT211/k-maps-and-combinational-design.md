# Karnaugh Maps and Combinational Design

## Karnaugh maps

**Karnaugh maps (K-maps)** are graphical representations of Boolean functions. One map cell corresponds to one row of the truth table, that is to one minterm or maxterm; multiple-cell areas correspond to standard terms. The order of variables matters: for f(x1, x2), x1 labels the columns and x2 the rows. **Any two adjacent cells differ in only one variable**, which is complemented in one cell and uncomplemented in the other. So m0 (x1′x2′) is adjacent to m1 and m2 but not to m3. Enter a 1 for each minterm in the function, then group (OR) the 1s: f = m0 + m1 + m2 simplifies to x1′ + x2′.

## Designing combinational circuits

A simple logic design process: describe the problem, derive the logical expression, simplify it, then draw the circuit. A logical function can be expressed by a **truth table**, a **Boolean expression** (an output expression for each input combination that gives 1) or a **logic diagram**. Two circuits are logically equivalent if their expressions give the same output for every input combination, which a truth table can check. Classic exercises are a room alarm watching a door sensor, a glass-break sensor and a motion sensor (extended to an armed or disarmed system), and sharing three types of biscuit under two rules.

## Arithmetic circuits

A **half adder** combines an XOR gate (Sum) with an AND gate (Carry-out). Adders are used in ALUs and counter circuits. **Overflow** occurs when an n-bit adder's sum is greater than or equal to 2ⁿ: 14 + 13 = 27 = 11011 needs 5 bits, so a 4-bit adder outputs 1011 (11). The ripple carry adder is slow, and the **carry look-ahead adder** is the solution.

A computer computes X = A − B as **A + (−B)**: take the **2's complement of B** by inverting its 4 bits and setting the **carry-in to HIGH** instead of LOW, then add. In binary subtraction, 0 − 1 produces a difference bit and a **borrow bit** for the next higher bit.

**Comparators** check whether A > B, A = B or A < B. An **identity comparator** has only one output, for A = B. A **magnitude comparator** has three outputs: A = B, A > B and A < B. Cascading n 1-bit comparators gives an n-bit comparator, for example comparing two 4-bit words.

Source: Minimisation Aids.pptx (IFT 211 lecture 4); Combinational Logic Design.pptx (IFT 211 lecture 5); full adder and co.ppt (IFT 211 lecture 7)
