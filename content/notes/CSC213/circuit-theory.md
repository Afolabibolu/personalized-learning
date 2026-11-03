# Basic Circuit Theory

## Circuits and units

A closed loop through which current can flow is an **electric circuit**. Every circuit has four basic parts: a **voltage (energy) source**, AC or DC; a **conductor**, usually wire forming a closed loop; an electrical **load**, such as a bulb that turns electrical energy into light and heat; and at least one **controller** (switch). A closed switch lets current flow; an open switch stops it. An ammeter measures current and a voltmeter measures voltage. The SI units are the **volt** (V), the **ampere** (A) and the **ohm** (Ω), linked by Ohm's law V = I × R. Prefixes scale them, for example 1 mA = 10⁻³ A and 1 kΩ = 10³ Ω.

## Kirchhoff's laws

Ohm's law alone cannot solve complex circuits, so Gustav Kirchhoff's two laws (1845) are used. The terms: a **node** is a junction where two or more elements meet, a **branch** is a component or group between two nodes, and a **loop** is a closed path that meets no node twice.

- **Kirchhoff's current law (KCL)**: the algebraic sum of currents meeting at a node is zero; the current flowing into a node equals the current flowing out. This is the **conservation of charge**.
- **Kirchhoff's voltage law (KVL)**: around any closed loop, the algebraic sum of all voltages is zero; the source voltage equals the sum of the voltage drops. This is the **conservation of energy**.

To use them, label each branch current, write KCL equations for the nodes and KVL equations for the independent loops, then solve the simultaneous equations. A negative answer only means the assumed direction was wrong.

## Thevenin's theorem

Any linear circuit containing several voltages and resistances can be replaced by **a single voltage source in series with a single resistor** connected to the load. Steps: (1) remove the load; (2) find Rs by shorting voltage sources and opening current sources, looking back into the terminals; (3) find Vs, the open-circuit voltage across the terminals; (4) redraw with the load. For example, 24 V across 12 Ω and 4 Ω in series gives Rs = 12 × 4 / 16 = 3 Ω and Vs = 1.5 A × 12 Ω = 18 V; a 15 Ω load then carries 18 / (3 + 15) = 1 A.

## Norton's theorem

Any linear network can be replaced by **a single constant current source Is in parallel with a resistance Rs**. Is is the current that flows when the output terminals are shorted together, and Rs is found exactly as for Thevenin. In the course example, Rs = 8 + (10 ∥ 8) = 12.44 Ω and Is = 0.9 A.

Source: CSC 213 DLC course book.pdf (Digital Logic Design, Nancy C. Woods), Lecture One (Basic Circuit Theory)
