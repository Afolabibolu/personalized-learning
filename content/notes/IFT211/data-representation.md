# Digital Signals and Data Representation

## Analogue and digital

Natural signals are **analogue (continuous)**: a human voice, a thermometer, a cassette tape and an analogue clock all vary smoothly. **Digital signals** are **discrete in value and time**: they take a finite set of values, in practice the binary values 0 and 1, and jump from OFF to ON. Digital systems sample analogue signals and express them as sequences of numbers. They are found in calculators, computers, phones, CDs and DVDs.

Notable features of digital systems are that they **use binary code**, are **accurate**, **process data quickly**, are **immune to noise**, are **scalable** (memory and components can be added without redesign) and **store data efficiently**. Digital design is easier because a limited set of values is simpler, more tolerant of drift and noise, cheaper, easier to store and transmit, and uses less power.

## Data and the computer

**Data** is any collection of numbers, characters or symbols coded so that a computer can process it; on its own it has no meaning, and only after processing does it become **information**. A computer performs four basic functions, all around data: **data processing**, **data storage**, **data movement** (input-output with peripherals, or data communication over distance) and **control**.

## Representing numbers

Any combination of bits, called a **code word**, can represent a data item as long as it is unique. Information is either **numeric** (signed or unsigned integers, tied to binary arithmetic) or **non-numeric** (symbols, colours, the alphabet, with no arithmetic).

A signed binary number carries a **sign bit**, the leftmost bit: 0 for positive, 1 for negative. Signed integers have three forms:

- **Sign-magnitude** (rarely used): the sign bit followed by the true binary magnitude. In 8 bits, +25 = 00011001 and −25 = 10011001.
- **1's complement**: positives as in sign-magnitude; a negative is the 1's complement (all bits inverted) of the positive, so −25 = 11100110.
- **2's complement** (mostly used): add 1 to the 1's complement, so −25 = 11100111.

An **unsigned integer** represents zero and positive numbers only, as the magnitude of its bit pattern; with 16 bits, 0001 0000 0000 1000 = 2¹² + 2³ = 4104. Common integer lengths are 8, 16, 32 and 64 bits. In **fixed-point** representation the binary point stays in one position, splitting the bits into an integer part and a fractional part, for example an 8.8 format.

Source: Data Representation and Number System.pdf (IFT 211 lecture 1)
