# Registers and Number Representation

## Registers

**Registers** quickly accept, store and transfer the data and instructions the CPU is using immediately. They perform **fetch** (take instructions from memory), **decode** (interpret them) and **execute** (carry them out and store the results).

- **Memory address register (MAR):** holds the address of data or instructions to access in memory.
- **Program counter (PC):** the address of the next instruction (the instruction pointer in x86; a 16-bit register in the 8085).
- **Accumulator (AC):** stores results produced by the CPU.
- **Memory data register (MDR):** holds data being written to or read from memory, acting as a buffer. To read cell 123, load 123 into the MAR and fetch; the copy appears in the MDR.
- **Index register:** holds a number added to an address to form the effective address.
- **Memory buffer register (MBR):** holds data or instructions read from or written to memory.
- **Data register (DR):** temporarily stores data going to or from a peripheral.

## Number systems

Computers use **binary** (base 2), with **octal** (base 8) and **hexadecimal** (base 16, digits 0–9 and A–F) as compact forms. A number in base b is Σ dᵢ × bⁱ.

- **Decimal to binary:** divide repeatedly by 2 and read the remainders backwards; 22₁₀ = 10110₂.
- **Binary to hexadecimal:** group bits in fours from the right; 10110₂ = 16₁₆.
- **Binary to octal:** group bits in threes; 25₁₀ = 11001₂ = 31₈.

In binary addition, 1 + 1 = 10 (0, carry 1).

## Signed integers

- **Unsigned:** n bits give 0 to 2ⁿ − 1 (4 bits: 0 to 15).
- **Sign-magnitude:** the most significant bit is the sign (0 positive, 1 negative); range −(2ⁿ⁻¹ − 1) to 2ⁿ⁻¹ − 1. It has **two zeros** (0000 and 1000), which complicates hardware.
- **One's complement:** negate by inverting every bit (+1 = 00001, −1 = 11110). It also has two zeros (00000 and 11111) and is historically important (early CDC machines used it).
- **Two's complement:** invert every bit and add 1. It has **a single zero** and simpler, faster hardware, so virtually all modern computers use it. With 3 bits the values run from −4 to 3.
- **Biased (excess)** representation is rarely used for integers.

## Fixed and floating point

**Fixed-point** numbers keep the binary point in a fixed position. **Floating-point** numbers store a **sign, exponent and mantissa**, as in the IEEE 754 standard, giving a much wider range of real values.

Source: CSC 313-Computer Organization and Architecture.pdf (course material, T. Oguntunde), Unit 4 (registers, their operations and types, number systems, conversions, sign representation) and Unit 5 (one's complement, two's complement, fixed and floating point)
