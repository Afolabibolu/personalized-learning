# Current, Resistance and D.C. Circuits

## Current

**Current I = Q/t** is the net charge flowing per second, measured in **amperes** (C/s). Conventional current flows from + to −. With n carriers per unit volume, charge q and drift velocity v_d (about 10⁻⁴ m/s), **I = nqAv_d** and the current density is **J = I/A = nqv_d**.

## Resistance

**Ohm's law**: at a given temperature, **V = IR**; equivalently E = ρJ. Not all materials obey it.

- The resistance of a wire is **R = ρL/A**, where ρ is the **resistivity** (Ω m).
- For metals, ρ and R rise with temperature: **R(T) = R₀[1 + α(T − T₀)]**. A copper wire of 1.05 Ω at 20 °C becomes 1.38 Ω at 100 °C.

## E.m.f. and internal resistance

A source's **e.m.f. E** is the energy it gives per unit charge (J/C = V). A real cell has **internal resistance r**, so the terminal voltage is **V = E − Ir** and **E = I(R + r)**.

## Combinations and power

- **Series**: **R = R₁ + R₂ + ...**. The same current flows, and the voltages add.
- **Parallel**: **1/R = 1/R₁ + 1/R₂ + ...**. Four 3 Ω resistors in parallel give **0.75 Ω**.

**Power** is **P = IV = I²R = V²/R**. For identical lamps in series, the one with the largest R (or I²R) glows brightest.

**Worked circuit** (2021/22 test): 3.8 Ω + 6 Ω in series with (8 Ω ∥ 12 Ω) + 5 Ω, on 30 V.

- Total R = 9.8 + 4.8 + 5 = **19.6 Ω**, so I = **1.53 A**.
- The drop across 6 Ω is **9.18 V**.
- The 8 Ω carries 1.53 × 12/20 = **0.92 A**.

## Kirchhoff's laws and bridges

1. **Junction rule**: the currents into a junction equal the currents out (charge is conserved).
2. **Loop rule**: around any closed loop, the sum of e.m.f.s equals the sum of the IR drops (energy is conserved).

A **Wheatstone bridge** is balanced (zero galvanometer current) when **P/Q = R/S**, which measures an unknown resistance. A **potentiometer** compares e.m.f.s by balance lengths: E₁/E₂ = l₁/l₂.

Source: PHY 104 Lecture 10: Current Electricity and DC Circuits (Oyewande); PHY 104 past questions; General knowledge of PHY 102 for the potentiometer ratio
