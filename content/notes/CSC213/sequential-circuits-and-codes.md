# Sequential Circuits, Counters, Codes and Error Detection

## Sequential circuits and flip-flops

**Sequential circuits** consist of combinational logic plus memory elements, so their outputs depend on **both current and previous inputs**; they are combinational circuits with **feedback**, and at any time they occupy a **state**. **Bistables (flip-flops)** have two stable states and stay latched until a trigger changes them. They are the building blocks of counters, shift registers and memories.

The **SR flip-flop**, a one-bit memory, can be made from two cross-coupled NAND gates with Set and Reset inputs and outputs Q and Q̄. Activating Set and Reset together is **invalid (meta-stable)**. The **JK flip-flop** was developed to remove this problem: it adds clock input circuitry and feedback, so J = K = 1 makes the output **toggle**.

## Registers and counters

A **register** is a group of flip-flops with a common clock. **Shift registers** move data one stage per clock pulse in four modes: **SISO**, **SIPO**, **PISO** and **PIPO** (serial or parallel in, serial or parallel out). They store data temporarily or act as delays, and shifting left multiplies by 2.

**Counters** are flip-flops (often T-type) connected to toggle as pulses arrive. In an **asynchronous (ripple) counter**, only the first flip-flop gets the clock and the effect ripples through, which is slower. In a **synchronous counter**, all flip-flops are clocked together, which is faster but more complex. The **modulus** is the number of states: n flip-flops give MOD-2ⁿ, counting 0 to 2ⁿ − 1 (3 flip-flops: MOD-8, 0 to 7).

## Computer codes

**Weighted codes** obey positional weights: binary and **BCD (8-4-2-1)**, in which each decimal digit takes 4 bits (0000 to 1001), so 10 = 0001 0000. **Non-weighted codes** include **Excess-3** (BCD plus 3; self-complementing) and **Gray code** (reflective; one bit changes between successive values, so it suits analogue-to-digital converters but not arithmetic). Alphanumeric codes such as **ASCII** and **EBCDIC** represent symbols.

## Error detection and correction

No medium is error-free. A **parity bit** makes the number of 1s even or odd: 1001110 with even parity is sent as 01001110. Parity detects a single-bit error but misses two errors and cannot locate the error. **Hamming codes** add several parity (check) bits so errors can be detected and corrected; the number of bit positions in which two code words differ is their **Hamming distance**.

Source: CSC 213 DLC course book.pdf (Digital Logic Design, Nancy C. Woods), Lectures Ten to Thirteen (Sequential Logic Circuits, Registers and Counters, Computer Codes, Error Detection and Correction)
