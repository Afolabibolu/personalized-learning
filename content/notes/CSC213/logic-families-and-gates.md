# Logic Families and Logic Gates

## Integrated circuits and logic families

Integrated circuits are classed by how many transistors or gates they hold: **SSI** (up to 10 transistors, a few gates), **MSI** (10 to 100; adders, decoders, counters), **LSI** (100 to 1,000; I/O chips, memory), **VLSI** (1,000 to 10,000; processors), **SLSI** (10,000 to 100,000) and **ULSI** (over a million; CPUs). A **system-on-chip (SoC)** puts a whole system on one piece of silicon.

A **logic family** is a group of compatible ICs with the same logic levels and supply voltages. **Bipolar** families use diodes and BJTs: TTL, RTL, DTL, ECL and others. **Unipolar** families use MOSFETs (PMOS, NMOS, CMOS) and offer higher speed and lower power.

## Characteristics

- **Noise immunity**: the maximum noise a circuit can withstand without a false change in its output. The **noise margin** measures it: VNH = VOH(min) − VIH(min) and VNL = VIL(max) − VOL(max).
- **Propagation delay**: the time between a change at the input and the resulting change at the output; it limits speed.
- **Fan-in** is the number of inputs a gate can handle; **fan-out** is the maximum number of inputs of the same family that one output can drive reliably.

**TTL** (the 7400 series) uses BJTs and a stabilised 5 V ± 0.25 V supply. An input above 2 V is logic 1 and below 0.8 V is logic 0; in between is the indeterminate region. Its noise margin is 0.4 V and its fan-out 10 to 40, but it uses more power. **CMOS** (the 4000 series) uses FETs, works on 3 V to 15 V, draws microamperes, has very high input impedance and a noise margin of about 1.45 V, and is now more common.

## Logic gates

A digital logic gate makes logical decisions on its inputs and has one output. Each gate is described by its symbol, truth table and Boolean expression:

- **AND** (Q = A·B): output 1 only when all inputs are 1. **OR** (Q = A + B): output 1 when any input is 1.
- **NOT** (inverter): output is the complement of the single input; the bubble shows inversion. The **buffer** passes its input unchanged.
- **NAND** and **NOR** are AND and OR followed by NOT. **XOR** gives 1 when the inputs differ; **XNOR** gives 1 when they are the same.

**NAND** and **NOR** are **universal gates**: any other gate, and so any circuit, can be built from either alone.

Source: CSC 213 DLC course book.pdf (Digital Logic Design, Nancy C. Woods), Lecture Four (Digital Logic Families) and Lecture Five (Digital Logic Gates)
