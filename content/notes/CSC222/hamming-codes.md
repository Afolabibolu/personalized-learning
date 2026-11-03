# Error Correction and the Hamming Code

## History

The problem of finding efficient error-correcting schemes troubled **Richard Wesley Hamming** (1915–1998). In 1946 he went to **Bell Labs** and worked on the Bell Model V computer, a relay machine fed by **punch cards**, which often had read errors. On weekdays, errors made the computer flash lights for operators; at weekends the machine simply terminated the program, so Hamming had to restart his programs from scratch. He worked on error correction for several years and in **1950** published what is now known as the **Hamming code**, still used in some applications.

## The (7,4) Hamming code

The original Hamming code is a **(7,4) binary linear code**: the encoder takes a **message of four bits**, s = (s₁, s₂, s₃, s₄), and encodes it as a **codeword of seven bits**, x = (p₁, p₂, p₃, s₁, s₂, s₃, s₄), adding **three parity bits** with the generating equations (addition modulo 2):

- p₁ = s₁ + s₃ + s₄
- p₂ = s₁ + s₂ + s₃
- p₃ = s₂ + s₃ + s₄

Each also gives a **parity-check equation**, such as p₁ + s₁ + s₃ + s₄ = 0.

## The Venn diagram

The code can be remembered by a **Venn diagram of three overlapping circles**, I, II and III. Each circle holds one generating (and parity-check) equation: the parity bit chosen so that **each circle contains an even number of 1s**. To correct an error, put the received bits into the diagram. Every circle with an odd number of 1s shows a warning. The faulty bit is the one that lies in **exactly the warned circles** and in no others. If the read-out is (0 1 1 1 1 0 0), circles I and II warn and III does not, so s₁ is wrong; correcting it gives (0 1 1 0 1 0 0). If the read-out is (1 1 1 0 1 0 0), only circle I warns, so p₁ is wrong.

## The parity-check matrix

Systematically, multiply the read-out y by the **parity-check matrix H**: the result, the **syndrome**, has one entry per check equation, 1 where the check fails. **The column of H that equals the syndrome gives the position of the error.** For y = (0 1 1 1 1 0 0), the syndrome is (1 1 0)ᵀ, the fourth column of H, so the fourth bit (s₁) is in error. This works because y = x + e, where x is the original codeword and e the error pattern; x·Hᵀ = 0, so the syndrome depends only on e.

Source: CSC 222 Digital Communication lecture slides (Dr Adeniji Oluwashola David), Lecture 4 (Efficient Error-Correcting Schemes) and slides 3 (Errors, Hamming distance)
