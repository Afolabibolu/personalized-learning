# The CPU, ALU, Instruction Formats and Addressing Modes

## The CPU

The **CPU** has a **processor unit** (ALU, registers and internal buses) and a **control unit**.

To compute R3 ← R1 + R2, the control word sets:

1. SELA to place R1 on bus A;
2. SELB to place R2 on bus B;
3. OPR to select A + B in the ALU;
4. SELD to load the output into R3.

## The control unit

The control unit is the **heart of the CPU**: it holds the program counter, instruction register, and timing and control logic. Its inputs are the **clock**, the **instruction register**, **flags** and **control signals from the control bus**. Its outputs are **control signals within the processor** and **control signals to the control bus**.

- **Hardwired** control builds the logic from gates and decoders; it is fast but hard to change.
- **Microprogrammed** control stores the control words in a control memory; it is flexible but slower.

## The ALU

The **ALU** is a combinational circuit that performs arithmetic and logic. Its core is a **parallel adder** built from full adders in cascade, with multiplexers selecting the operation. Data come from registers, results go to registers, and the ALU sets flags. A 2-bit or 4-bit ALU for addition, AND, OR and XOR is built from an adder and logic gates, with select lines choosing the output.

## Instruction formats

An instruction has an **operation code** field, an **address** field and a **mode** field. CPU organizations are **single-accumulator**, **general-register** or **stack**. To evaluate X = (A + B) × (C + D):

- **Three-address:** ADD R1, A, B; ADD R2, C, D; MUL X, R1, R2. Programs are short.
- **Two-address:** MOV R1, A; ADD R1, B; MOV R2, C; ADD R2, D; MUL R1, R2; MOV X, R1.
- **One-address** (with an accumulator and temporary T): LOAD A; ADD B; STORE T; LOAD C; ADD D; MUL T; STORE X.
- **Zero-address** (stack): PUSH A; PUSH B; ADD; PUSH C; PUSH D; ADD; MUL; POP X.

## Addressing modes

The **effective address (EA)** is where the operand really is.

- **Implied:** operand implied by the instruction.
- **Immediate:** the operand is in the instruction, used to initialise registers.
- **Register direct** and **register indirect:** the operand is in a register, or a register holds its address.
- **Auto-increment/auto-decrement:** register indirect, with the register stepped after or before use.
- **Direct:** the address field is the operand's address.
- **Indirect:** the address field holds the address of the address.
- **Relative** (PC + offset), **indexed** (index register + address), **base register** (for relocation) and **stack** addressing.

Source: CSC 313-Computer Organization and Architecture.pdf (course material, T. Oguntunde), Unit 6 (CPU, processor unit, control unit, registers organization), Unit 7 (ALU, ALU design, instruction formats, addressing modes) and the 2020/21 paper (Question 3b)
