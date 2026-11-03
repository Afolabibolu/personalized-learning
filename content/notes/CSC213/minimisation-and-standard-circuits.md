# Minimisation and Standard Combinational Circuits

## Minimisation

A fundamental SOP is correct but not usually the simplest. **Minimisation** gives the same function with fewer gates.

- **Boolean algebra**, developed from George Boole's "laws of thought", supplies laws that can be applied left to right or right to left, such as the absorption and De Morgan laws and XY + X̄Y = Y.
- A **Karnaugh map (K-map)** rearranges a truth table so that **adjacent cells differ in exactly one input**; rows and columns are numbered 00, 01, 11, 10 (Gray order). Put a 1 in each cell whose minterm gives 1, then find the **largest groups of adjacent 1s** (of 1, 2, 4, 8 cells). A variable that changes inside a group drops out of that group's term. Larger groups mean fewer products and inputs. K-maps suit 2 to 4 inputs.
- The **Quine-McCluskey (QM) method** is a systematic, tabular approach for many variables. It applies XY + X̄Y = Y repeatedly, combining minterms that differ in one bit to find the prime implicants.

## Adders

A **half adder** adds two bits A and B, giving a **Sum** (XOR) and a **Carry** (AND). It has no carry-in, so it cannot add multi-bit numbers. A **full adder** has three inputs, A, B and **Carry-in**, and is two half adders joined; the TTL 74LS83 adds two 4-bit numbers. **n full adders cascaded** form a **ripple carry adder**: each carry-out feeds the next carry-in, so the carry "ripples" from right to left and the result is delayed until it settles.

## Data selectors and code converters

- A **multiplexer (MUX)**, or data selector, works like a fast rotary switch: it lets many inputs share one output, chosen by the select (address) lines. With m select lines it chooses from 2ᵐ inputs. It is like a television channel selector.
- A **demultiplexer (DEMUX)**, or data distributor, does the reverse: it routes one input to one of many outputs, converting serial data to parallel.
- An **encoder** converts one active input out of many into a binary code; an s-bit encoder has 2ˢ inputs. It gives a wrong code if two inputs are active at once, so a **priority encoder** outputs the code of the highest-priority active input (used for microprocessor interrupts).
- A **decoder** is the opposite: an n-bit decoder has 2ⁿ outputs, one active for each input code (2-to-4, 3-to-8, 4-to-16), used as address decoders. A **BCD to 7-segment decoder** drives a display from 4 BCD inputs to 7 segment outputs.

Source: CSC 213 DLC course book.pdf (Digital Logic Design, Nancy C. Woods), Lecture Eight (Switching Function Minimization) and Lecture Nine (Standard Combinational Logic Circuits)
