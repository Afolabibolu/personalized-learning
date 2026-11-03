# Electromagnetic Induction and A.C. Circuits

## Induction

**Magnetic flux** through an area A is **Φ = BA cos θ**, measured in **webers** (T m²).

- **Faraday's law**: the induced e.m.f. equals the rate of change of flux linkage: **E = −N dΦ/dt**.
- **Lenz's law**: the induced current flows so as to **oppose the change** that produces it. This is the minus sign, and it expresses energy conservation.

A rod of length L moving at v across a field B has a **motional e.m.f. E = BLv**.

**Inductance**: a changing current in a coil induces an e.m.f. in itself, **E = −L dI/dt**, where L is the self-inductance in **henries**. It can also induce one in a neighbour (mutual inductance M). An inductor stores energy **½LI²**.

## Alternating current

A coil of N turns and area A rotating at ω in a field B gives **E = NABω sin ωt**: this is the **a.c. generator**. For sinusoidal a.c., the **r.m.s.** value is the peak divided by √2: **I_rms = I₀/√2**. Mains 230 V is the r.m.s. value, with a peak of about 325 V.

## RLC circuits

- A **resistor**: V and I are in phase.
- An **inductor**: **reactance X_L = ωL**, and V leads I by 90°.
- A **capacitor**: **reactance X_C = 1/(ωC)**, and I leads V by 90°.

In series, the **impedance** is **Z = √(R² + (X_L − X_C)²)** and I = V/Z. The phase angle satisfies tan φ = (X_L − X_C)/R.

At **resonance**, X_L = X_C, so **ω₀ = 1/√(LC)**: Z = R is a minimum and the current is a maximum. The average power is **P = V_rms I_rms cos φ**, where cos φ = R/Z is the **power factor**.

## Transformers

Two coils on an iron core, linked by mutual induction. For an ideal transformer, **Vₛ/Vₚ = Nₛ/Nₚ = Iₚ/Iₛ**, and the power in equals the power out. A step-up transformer raises the voltage and lowers the current. Losses come from eddy currents (reduced by laminating the core), hysteresis, resistance and flux leakage.

Source: PHY 104 Part 2: Magnetism (P. O. Adesina) (outline: induction, RLC, transformer); General knowledge of PHY 102 for the formulas, as the induction and a.c. slides are scanned and not fully legible
