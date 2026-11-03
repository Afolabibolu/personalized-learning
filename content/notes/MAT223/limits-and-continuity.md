# Limits and Continuity of Functions

## Functions

A variable y = f(x) is a **function** of x on a domain D if to each x in D there corresponds a definite value y; x is the **independent** and y the **dependent** variable. 

## Open balls and intervals

For a fixed x0 in R and r > 0, the **open ball** centred at x0 with radius r is **B_r(x0) = {x in R : |x − x0| < r} = (x0 − r, x0 + r)**. For example, B_(1/3)(−3) = (−10/3, −8/3).

## Limits

f has **limit L as x → x0** if for every ε > 0 there is δ > 0 such that |f(x) − L| < ε whenever 0 < |x − x0| < δ. One-sided limits handle jumps: for h(x) = |x − 6|/(x − 6), the right limit at 6 is 1 and the left limit is −1, so the limit does not exist.

## Continuity

f is **continuous at x0** if **for every ε > 0 there is δ > 0 such that |f(x) − f(x0)| < ε whenever |x − x0| < δ**. Equivalently, f is continuous at x0 if lim f(x) = f(x0).

To prove f(x) = 3x² − 2x + 1 is continuous at x0 = 5: |f(x) − f(5)| = |3x² − 2x − 65| = |x − 5| · |3x + 13|. If |x − 5| < 1, then |3x + 13| < 31, so taking **δ = min(1, ε/31)** gives |f(x) − f(5)| < ε.

**Sequential criterion**: f is continuous at x0 **if and only if f(x_n) → f(x0) for every sequence x_n → x0**. To show the **signum-type function** f(x) = 1 for x > 0, 0 at x = 0 and −1 for x < 0 is **discontinuous at 0**, take x_n = 1/n → 0; then f(x_n) = 1, which does not tend to f(0) = 0.

## Algebra of continuous functions

If f and g are continuous at x0, then **αf, f + g, f − g and fg are continuous at x0**, and f/g is too if g(x0) ≠ 0. The **composite** of continuous functions is continuous.

## Uniform continuity

f is **uniformly continuous** on an interval if **one δ works for every point**: |f(x) − f(y)| < ε whenever |x − y| < δ. f(x) = x² is uniformly continuous on (0, 1), but f(x) = 1/x is **not** uniformly continuous on (0, 1). **A function continuous on a closed bounded interval [a, b] is uniformly continuous there.**

Source: MAT 223 lecture notes (scanned, Notes 1 to 9) (Functions of a Real Variable; Continuous Functions; Some Theorems on Continuity); MAT 223 past papers. The worked ε-δ proof at x0 = 5 and the uniform continuity results are from general knowledge of MAT 223.
