# Logic Gates and Their Properties

## Logic gates

Only two voltage levels, logic 1 and logic 0 (true and false), are allowed. Hardware consists of a few simple building blocks: **logic gates, built from transistors**. A NOT gate can be made from a single transistor, while an AND gate needs three. Every gate can be described in three ways: by its **truth table** (the output for each possible input combination), its **logic symbol** and its **Boolean expression**.

The 2-input gates are AND, NAND, OR, NOR, XOR and XNOR, plus the single-input NOT. **XOR** (exclusive-OR) needs its two inputs to be **different** to give an output; with more inputs, an **odd** number of 1s gives 1. **XNOR** (exclusive-NOR) needs its two inputs to be the **same**; an **even** number of 1s gives 1.

## Complete sets and universal gates

A set of gate types is **complete** if any logical function can be implemented using only gates from the set, using as many as you like. {AND, OR, NOT} is complete but not a **minimal complete set**, because it has redundant elements; a minimal complete set has none. **NAND** and **NOR** are each a complete set on their own, so they are classified as **universal gates**: they can produce any other gate function.

## Properties of logic gates

- **Noise** is unwanted voltage induced in electrical circuits that can threaten their proper operation. It is caused by **stray electric and magnetic fields**, and its effect is to make an input voltage drop below VIH(min) or rise above VIL(max).
- **Noise immunity** is the maximum noise a circuit can withstand without affecting its output: its ability to tolerate noise without a false change in output voltage.
- The **noise margin** is a quantitative measure of noise immunity, given as a pair of parameters, the DC HIGH and LOW noise margins.
- **Fan-in** is the number of inputs a logic gate can handle.
- **Fan-out**, the more important characteristic, is the **maximum number of logic inputs of the same family that an output can drive reliably**; it sets how many circuits a gate can drive.

Source: Digital Logic Gates.pptx (IFT 211 lecture 2); Properties of Logic gate.ppt (IFT 211 lecture 6)
