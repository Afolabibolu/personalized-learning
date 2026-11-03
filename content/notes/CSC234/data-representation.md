# Data Representation and Number Systems

## Number systems

In the **decimal** system, a number's value is the sum of each digit multiplied by 10 to the power of its position, counting from zero (any number to the power zero is 1). Computers are not as smart as humans: it is easy to build an electronic machine with **two states, on and off, 1 and 0**, so computers use the **binary** system, with the digits 0 and 1.

- Each binary digit is a **bit**; **4 bits form a nibble**, **8 bits a byte**, **two bytes a word** (16 bits), and two words a **double word** (32 bits, rarely used).
- A "b" is added after a binary number: **101b = 5**.
- **Hexadecimal** uses 16 digits, 0 to 9 and A to F. It is compact and easy to read, and every nibble converts to one hexadecimal digit. An "h" is added at the end, and a 0 at the start if the number begins with a letter: **5Fh = 95**, **0E120h**, and **1234h = 4660**.

A byte can represent **256** values, a word **65,536**, and a double word over four billion. The 80x86 works best with groups of 8, 16 or 32 bits.

## Signed and unsigned integers

The 80x86 represents **unsigned integers** in standard binary and **signed integers** in **two's complement**. A byte like **0FFh** can mean either **255** or **−1**: of its 256 combinations, the first 128 (0 to 127) represent positive numbers and the next 128 represent negative numbers. To get −5, subtract 5 from 256 to get 251. Then adding 5 and 251 overflows past 255 and gives zero, as −5 + 5 should. In negative numbers the **high bit is always 1**, so it shows the sign. Words work the same way: of 65,536 combinations, 0 to 32,767 are positive and the rest negative.

The emu8086 environment has a **base converter** and a **multi-base calculator** for these conversions. For example, 0FFFFh × 10h + 0FFFFh, the maximum memory location the 8086 can address, is 1,114,095 unsigned, or −17 if treated as signed.

## Operations on bits

Binary values support normal arithmetic (+, −, ×, ÷) and the **logical operations AND, OR, XOR and NOT**, defined for single bits and extended to n bits by **bitwise** operation, plus **shift left, shift right, rotate left and rotate right**, which work on fixed-length strings of bits.

Source: csc234 assemblylanguage.pdf (CSC 234 course book, I. T. Ayorinde), Study Session 1 (Data Representation)
