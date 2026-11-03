# Sequential Circuits, Counters and Registers

## Sequential circuits

In a combinational circuit the output depends only on the current input. **Sequential logic circuits remember past inputs and past circuit state**: they contain **storage elements (memory)** and use **feedback**, with results fed back as inputs, so outputs = f(present inputs, past inputs, past outputs). A thermostat is an example: the output of the temperature-changing function affects the input of the temperature-checking function. A counter is a typical sequential design.

**Bistables** have two stable states (logic 1 or logic 0) and stay **latched** until a trigger changes them; they are the basis of counters, shift registers and memories. A plain latch shows any change at its inputs immediately at its outputs, which causes **synchronisation problems**. The solution is to use latches to build **flip-flops** that update only at specific times. Flip-flops come in two main types: **level-sensitive** (usually called a latch, the simplest type) and **edge-triggered** (for example master-slave and D-type).

- The **SR flip-flop** is set by a 1 on S and reset by a 1 on R.
- The **JK flip-flop** was invented to **eradicate the invalid state of the SR flip-flop**. It acts as a D-type when J and K differ and as a **T-type when J = K = 1**.
- The **T flip-flop** toggles (changes state) with every clock pulse while T is at logic 1.
- In a **D latch** with inputs D (data) and E (enable), Q follows D while E is 1.

The operation of **asynchronous circuits** is not controlled by any external timing mechanism, whereas **synchronous circuits** have a clock that regulates the feedback.

## Registers and counters

A **register** is a collection of binary storage elements that stores a vector of binary values and is used for simple data storage, movement and processing. Shift registers include serial-in serial-out, parallel-in serial-out and parallel-in parallel-out types.

**Counters** are formed by connecting flip-flops together. In **asynchronous (ripple) counters** the flip-flops do not share a clock, so they change at slightly different times; the cumulative delay is a drawback. The **modulus** of a counter is the number of states it goes through before returning to zero. **n flip-flops give a MOD-2ⁿ counter**, counting 0 to 2ⁿ − 1: 3 bits give MOD-8, 4 bits MOD-16 and 8 bits MOD-256. The output of the last flip-flop divides the clock frequency by the MOD number, so **a counter is also a frequency divider**. A decade (BCD) counter counts 0 to 9.

Source: SequentialCircuits.ppt (IFT 211 lecture 8); counters_and_registers.ppt (IFT 211 lecture 9)
