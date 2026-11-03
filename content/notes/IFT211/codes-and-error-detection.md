# Binary Codes and Error Detection

## Codes for decimal digits

Computers work in binary, so decimal digits must be coded in 1s and 0s. Arranging four bits into ten distinct combinations gives **binary-coded decimal (BCD)**. A number with k decimal digits needs **4k bits**: 396 is 0011 1001 0110 in BCD. A BCD number above 9 looks different from its binary equivalent; (185)₁₀ = (0001 1000 0101)BCD = (10111001)₂. The combinations 1010 to 1111 are not used in BCD, and BCD is **not self-complementing**.

- **Weighted codes** obey positional weights. In 8421 BCD, the bits of 1001 have weights 8, 4, 2 and 1. 8421 BCD, 2421 BCD and 5211 BCD are all weighted.
- **Non-weighted codes** do not assign a weight to each position; Excess-3 and Gray code are examples.

## Alphanumeric codes

Alphanumeric (character) codes represent digits, letters, mathematical symbols and punctuation, and let keyboards, monitors and mice be interfaced. The most common are ASCII, EBCDIC and Unicode.

- **ASCII** (American Standard Code for Information Interchange) uses **seven bits to code 128 characters**: 94 printable graphic characters and 34 non-printing control characters. The letter A is 1000001. Computers handle bytes, so ASCII characters are usually stored one per byte, leaving an extra bit for other uses.
- **EBCDIC** (Extended Binary Coded Decimal Interchange Code) was invented by **IBM** to extend BCD. It is an **8-bit code** with room for **256 characters**, used on IBM computers.

## Errors and error coding

Interference and defects in the medium cause random bit errors. A **single-bit error** changes only one bit of a data unit; a **burst error** changes two or more bits. Error detection relies on **redundancy**: extra bits are added.

- **Simple parity check**: a parity bit makes each 7-bit ASCII character 8 bits. With even parity, any single-bit change makes the parity odd, so the receiver detects it, but it cannot correct it because it does not know which bit is wrong. Parity also detects some multiple-bit errors.
- A **two-dimensional parity check** adds parity across rows and columns of a block.
- The **Hamming code** is a set of error-correction codes that detect and correct bit errors when data is moved or stored.

Source: Data Representation and Number System.pdf (IFT 211 lecture 1), sections on binary codes and error detection
