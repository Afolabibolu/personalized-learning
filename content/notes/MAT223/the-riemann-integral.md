# The Riemann Integral

## Partitions and sums

A **partition** P of [a, b] is a finite set of points a = x0 < x1 < ... < xn = b. A **refinement** Q of P is a partition containing all the points of P (and possibly more).

For a bounded function f on [a, b], let M_k and m_k be the supremum and infimum of f on [x_(k−1), x_k]. The **upper sum** is **U(f, P) = Σ M_k Δx_k** and the **lower sum** is **L(f, P) = Σ m_k Δx_k**, where Δx_k = x_k − x_(k−1). Always **L(f, P) ≤ U(f, P)**.

**Refining a partition can only increase the lower sum and decrease the upper sum**: if Q is a refinement of P, then **L(f, P) ≤ L(f, Q) ≤ U(f, Q) ≤ U(f, P)**.

## Integrability

The **upper integral** is the infimum of all upper sums and the **lower integral** the supremum of all lower sums. f is **Riemann integrable** on [a, b] (written f in R_a^b) if they are **equal**; the common value is **∫ from a to b of f(x) dx**.

- **Darboux integrability criterion**: f is integrable **if and only if for every ε > 0 there is a partition P with U(f, P) − L(f, P) < ε**.
- **Limit test criterion**: if there are partitions P_n with **lim U(f, P_n) = lim L(f, P_n)**, then f is integrable and the integral is that common limit.

**Example**: for f(x) = x² on [1, 4] with the regular partition P_n into n equal parts, U(f, P_n) and L(f, P_n) both tend to **(4³ − 1³)/3 = 21**, so ∫ from 1 to 4 of x² dx = 21.

The function f(x) = 0 for rational x and 1 for irrational x is **not Riemann integrable** on any interval: every subinterval contains both kinds of number, so every lower sum is 0 and every upper sum is b − a.

## Properties

- **Continuous functions** and **monotone functions** on [a, b] are Riemann integrable, and an integrable function must be **bounded**.
- If f ≥ g on [a, b], then ∫ f ≥ ∫ g; in particular **if f ≥ 0 then ∫ f ≥ 0** (the **inequality rule**). For example, since 1 ≤ e^(x²) ≤ e on [0, 1], **1 ≤ ∫ from 0 to 1 of e^(x²) dx ≤ (e + 1)/2**.
- **Triangle inequality**: |∫ f| ≤ ∫ |f|.
- The **integral function** F(x) = ∫ from a to x of f is **uniformly continuous** (indeed Lipschitz) on [a, b].

Source: MAT 223 past papers (the integration sections and the 2015/16 CA papers); MAT 223 lecture notes (scanned, Notes 1 to 9). The scanned notes do not include the integration lectures, so this note is written from general knowledge of MAT 223 following the papers' questions.
