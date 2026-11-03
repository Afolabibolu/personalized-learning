# Semiconductors, Diodes and Transistors

## Semiconductors

**Semiconductors** are materials whose conductivity lies between that of a conductor and an insulator. Group IV elements such as silicon and germanium have four valence electrons tied up in covalent bonds, so a pure (**intrinsic**) semiconductor is a poor conductor. Heat may free an electron, leaving a positive **hole**; when the electron falls back into a hole, that is **recombination**. In an intrinsic semiconductor the numbers of electrons and holes are equal.

**Doping** adds tiny amounts of an impurity to raise conductivity, giving an **extrinsic** semiconductor:

- **N-type**: doped with a pentavalent (donor) atom such as phosphorus or arsenic. The extra electron is free to move, so **electrons are the majority carriers**.
- **P-type**: doped with a trivalent (acceptor) atom such as boron or aluminium, leaving a hole, so **holes are the majority carriers**.

## The P-N junction and diodes

Where P-type and N-type meet, electrons diffuse across and fill holes, leaving a **depletion region** with no carriers and a **potential barrier** (about 0.6 V for silicon, 0.2 V for germanium). **Forward bias** (negative terminal to N) pushes carriers toward the junction, narrows the depletion region and lets current flow once the barrier is overcome. **Reverse bias** pulls carriers away, widens the depletion region, and almost no current flows. A **diode** is a unidirectional device: conventional current flows from the anode (P side) to the cathode (N side). Types include the Zener (conducts in reverse above its breakdown voltage), Schottky (low voltage drop), varactor (variable capacitance), LED (emits light) and photodiode (conducts when exposed to light).

## Transistors

A transistor is a three-terminal device. The **bipolar junction transistor (BJT)**, NPN or PNP, has an emitter, a thin base and a collector. It is **current-operated**: a small base current IB controls a large collector current IC. The DC current gain is β = IC / IB; α = IC / IE is close to 1. With β = 100, switching a 4 mA load needs IB = 40 µA. As a switch, a transistor with no base current is **cut off** (off); with enough base current it is **saturated** (on).

The **field effect transistor (FET)** is **voltage-operated**: the gate voltage's electric field controls the drain current, and no current flows into the gate. It is unipolar and has very high input impedance. The **JFET** narrows its channel with a reverse-biased gate until it is pinched off. The **MOSFET** has a gate insulated by silicon dioxide and comes in enhancement and depletion types.

Source: CSC 213 DLC course book.pdf (Digital Logic Design, Nancy C. Woods), Lecture Two (Semiconductors I) and Lecture Three (Semiconductors II)
