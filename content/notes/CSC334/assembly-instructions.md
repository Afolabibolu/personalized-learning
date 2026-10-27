# Assembly Instructions, Procedures and Macros

## Addressing modes

With two operands, the first is usually the **destination** and the second the **source**. The three basic modes are:

- **Register addressing:** the operand is in a register (`MOV EAX, EBX`). It is the fastest, since no memory is involved.
- **Immediate addressing:** the operand is a constant (`MOV AX, 45H`).
- **Memory addressing:** the operand is in memory. It may be direct (`MOV BX, WORD_VALUE`), direct-offset (`BYTE_TABLE[2]`) or indirect through a base or index register (`MOV [EBX], 110`).

**MOV** copies data; both operands must be the same size, and the source is unchanged. Type specifiers (BYTE, WORD, DWORD) remove ambiguity.

## Directives

- **Define (initialised data):** DB 1 byte, DW 2, DD 4, DQ 8, DT 10. Characters are stored as ASCII, negative numbers in two's complement, and the processor is little-endian.
- **Reserve (uninitialised):** RESB, RESW, RESD, RESQ, REST.
- **TIMES** repeats an initialisation: `marks TIMES 9 DW 0`.
- **Constants:** EQU defines a constant; %assign defines a numeric constant that can be redefined; %define defines numeric or string constants, like #define in C.

## Arithmetic and logic

- **INC/DEC** add or subtract one.
- **ADD/SUB** work on bytes, words or doublewords, but not memory to memory.
- **MUL** (unsigned) and **IMUL** (signed) multiply into the accumulator.
- **DIV** and **IDIV** divide, giving a **quotient and a remainder**.
- **AND** clears bits (`AND BL, 0FH`) and tests odd or even. **OR** sets bits. **XOR** with itself clears a register. **TEST** is AND without changing the operand. **NOT** reverses the bits.

## Conditions and loops

**CMP** compares two operands by subtraction, setting flags. **JMP** jumps unconditionally, and conditional jumps (JE, JNE, JG, JL, JLE and others) jump when flags match. The **LOOP** instruction repeats a block using **ECX** as the counter.

## Procedures, stack and macros

- A **procedure** is called with `CALL name` and returns with `RET`.
- The **stack** stores data and return addresses with PUSH and POP, through SS:SP.
- **Recursion** is a procedure calling itself, directly or indirectly.
- A **macro** is a named block of text substituted wherever it is used: `%macro name number_of_params ... %endmacro`. Unlike a procedure, it is expanded in place rather than called.

Source: CSC 334- Systems Programming - new1.docx (course book), Unit 5 (addressing modes, MOV, variables, constants, INC, DEC, ADD, SUB), Unit 6 (MUL, DIV, logical instructions, conditions), Unit 7 (loops, numbers, strings, arrays, procedures, stack) and Unit 8 (recursion and macros)
