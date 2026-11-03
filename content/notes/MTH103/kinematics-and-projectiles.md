# Kinematics and Projectiles

## Rates of change

For motion in a straight line with displacement x at time t:

- **v = dx/dt** and **a = dv/dt = d²x/dt²**;
- velocity is the gradient of the (t, x) graph and acceleration the gradient of the (t, v) graph;
- going the other way, **v = ∫a dt** and **x = ∫v dt**, with the constants fixed by the initial values.

**Example**: x = 2t³ − 6t gives v = 6t² − 6 and a = 12t. At t = 1, v = 0.

**Example**: a = 6 − t, starting at the origin with v = −2. Then v = 6t − ½t² − 2 and x = 3t² − t³/6 − 2t, so at t = 6, **v = 16 m/s** and **x = 60 m**.

**Example**: a = 8 − 2t², starting from rest at the origin. Then v = 8t − ⅔t³ and x = 4t² − t⁴/6, so the distance in 2 s is 16 − 8/3 = **13⅓ m**.

## Distance and displacement

**Displacement** is ∫v dt between the times. **Distance travelled** is **∫|v| dt**: split the integral where v changes sign.

For v = 2t − t² on [0, 4], the displacement is **−16/3 m**. The distance is ∫₀² (2t − t²) dt + ∫₂⁴ (t² − 2t) dt = 4/3 + 20/3 = **8 m**.

The area under a v–t graph gives the distance: a car with v = t(40 − t)/20 travels **533.3 m** between two stops.

## Constant acceleration

**v = u + at, s = ut + ½at², v² = u² + 2as.** A coin dropped from 12 m with g = 10 lands after √2.4 ≈ **1.55 s**.

## Projectiles

A projectile is a particle, unpowered, with air resistance ignored. It has **no horizontal acceleration** and acceleration **g downward**. Launched at speed u and angle α:

- **x = (u cos α)t** and **y = (u sin α)t − ½gt²**;
- the vertical velocity is zero at the top, giving **greatest height H = u²sin²α/(2g)**;
- **time of flight T = 2u sin α/g**;
- **range R = u² sin 2α/g**, the greatest at α = 45°.

(The formulas for H, T and R are general knowledge; the slides work them out numerically.)

For u = 20 m/s at 60° with g = 10: H = 15 m, T = 3.46 s and R = 34.6 m. The time to the top is half the flight time.

For motion in space, differentiate the position vector: v = dr/dt and a = d²r/dt².

Source: MAT 141 lecture note (University of Ibadan, 2016): vectors and motion, in Combined slides.pdf; MAT 141 / MTH 103 past papers; General knowledge of MTH 103 for the general projectile formulas
