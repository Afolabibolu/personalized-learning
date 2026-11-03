# Number Systems and Data Representation

## Analog and digital

**Analog** data is continuous, like a mercury thermometer; **digital** data is discrete. Computers **digitise** data into pieces and use binary, because a digital signal has only two states. **n bits represent 2ⁿ things**: one bit gives two, eight bits 256. A **bit** is a binary digit, a **nibble** 4 bits, a **byte** 8 bits and a **word** one or more bytes.

## Number systems

In a positional system each digit's place value is a power of the base: 954 = 9 × 10² + 5 × 10 + 4. A base B uses digits 0 to B − 1:

- binary: 0 and 1;
- octal: 0 to 7;
- hexadecimal: 0 to 9 and **A to F**.

Examples:

- octal 642 = 6 × 64 + 4 × 8 + 2 = **418**;
- hexadecimal DEF = 13 × 256 + 14 × 16 + 15 = **3567**;
- binary 10110 = **22**;

To convert between binary and octal or hexadecimal, group the bits in **threes** or **fours** from the binary point: 10101011 = 10 101 011 = **253₈**. Decimal to another base is repeated division by the base; fractions are converted by repeated multiplication. For fractions, 0.110011₂ = 51/64 = 0.796875 and 1100.1011₂ = 12.6875. Binary arithmetic follows decimal rules: 1 + 1 = 0 carry 1, and subtraction borrows a power of the base.

## Negative and real numbers

**Sign-magnitude** has both +0 and −0. **Two's complement** keeps one zero and lets subtraction be done as A + (−B). In 8 bits, adding 127 and 3 gives **overflow**. Real numbers use **floating point**, sign × mantissa × 2^exp. **Scientific notation** keeps the point after the first digit: 12001.32708 = 1.200132708E+4.

## Text, sound and images

- **ASCII** used **7 bits (128 characters)**; extended ASCII uses 8 bits (256). '!' is 33.
- **Unicode** uses **16 bits**; it is a superset of ASCII.
- **Compression** saves space. **Keyword encoding** replaces common words. **Run-length encoding** writes a run as a flag, the character and a count (*b8). **Huffman codes** give frequent letters shorter codes, and no code is a prefix of another.
- Compression is **lossless** if nothing is lost and **lossy** if some is lost.
- **Sound** is digitised by **sampling**, about 40,000 times a second.
- **Colour** is an **RGB** value: (255, 255, 0) is yellow and (255, 255, 255) white.

## Logic gates

**Boolean algebra** compares bits:

- **AND** is 1 only if all inputs are 1;
- **OR** is 1 if any input is 1;
- **NOT** inverts its input;
- **NAND** and **NOR** invert AND and OR;
- **XOR** is 1 when the inputs **differ**.

Source: Week 4b Data_representation.pdf (CSC 101 slides); Week 5 Number Systems.ppt (CSC 101 slides); CSC 101 compiled by SISTER IZA.pdf (the CSC 101 slides compiled by a student) (Boolean algebra slides); COS 101 / CSC 101 past questions
