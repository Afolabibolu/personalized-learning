# Capacitors and Dielectrics

## Capacitance

A **capacitor** is two conductors separated by an insulator. With charges ±Q and potential difference V, its **capacitance** is **C = Q/V**, measured in **farads** (C/V). Practical values are in μF, nF or pF.

For a **parallel-plate capacitor** of plate area A and separation d:

**C = ε₀A/d** in vacuum, and **C = κε₀A/d** with a **dielectric** of constant κ (εᵣ).

**Example**: A = 0.1 m², d = 1 cm and κ = 2 give C = 2 × 8.85 × 10⁻¹² × 0.1/0.01 = **1.77 × 10⁻¹⁰ F**.

## Dielectrics

A dielectric is an insulator whose molecules **polarise** in the field. This reduces the field between the plates by the factor κ, so for a given charge **the capacitance rises by κ** and the voltage falls. Dielectrics also raise the breakdown voltage and keep the plates apart.

## Combinations

- **Parallel**: **C = C₁ + C₂ + ...**. The same voltage is across each, and the charges add.
- **Series**: **1/C = 1/C₁ + 1/C₂ + ...**. The same charge is on each, and the voltages add. The total is less than the smallest capacitance.

## Energy

The energy stored is **U = ½CV² = ½QV = Q²/2C**. It resides in the field, with energy density ½ε₀E².

**Example**: a 2 μF capacitor at 4 V stores ½ × 2 × 10⁻⁶ × 16 = **16 × 10⁻⁶ J**.

## RC circuits

Charging a capacitor through a resistance R gives **q = Q(1 − e^(−t/RC))**. Discharging gives **q = Q e^(−t/RC)**. The **time constant** τ = RC is the time to reach about 63% of the final charge (charging) or fall to about 37% (discharging).

Source: PHY 104 electricity lectures 1–10 (Oyewande, 2024); PHY 104 past questions; General knowledge of PHY 102 for RC circuits and energy density
