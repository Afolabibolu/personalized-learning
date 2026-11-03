# Undetermined Coefficients and Variation of Parameters

## The approach

For **a0 y'' + a1 y' + a2 y = f(x)**, first solve the homogeneous part to get the **complementary function (CF)** y_c, then find a **particular integral (PI)** y_p, and write **y = y_c + y_p**. The three methods in the course are **undetermined coefficients**, **variation of parameters** and the **operator D method**.

## Undetermined coefficients

Guess a particular integral of the **same form as f(x)** with unknown coefficients, substitute and compare coefficients.

| f(x) | Trial y_p |
| --- | --- |
| a polynomial of degree n | a general polynomial of degree n |
| e^(ax) | A e^(ax) |
| sin bx or cos bx | A cos bx + B sin bx |
| e^(ax) times a polynomial or sine | the product of the matching forms |

**If a term of the trial form already appears in the CF, multiply the trial form by x** (or x² for a double root). For y'' − 5y' + 6y = 50 sin 4x, the CF is c1 e^(2x) + c2 e^(3x), and the trial y_p = A cos 4x + B sin 4x gives (−10A − 20B) cos 4x + (−10B + 20A) sin 4x = 50 sin 4x, so A = 2, B = −1 and **y_p = 2 cos 4x − sin 4x**.

The method works only when f(x) is built from polynomials, exponentials, sines and cosines.

## Variation of parameters

This method **applies whenever the complementary function is known**, even when f(x) is not of the special forms (for example cosec 2x). If y_c = c1 y1 + c2 y2 for y'' + p y' + q y = f(x), replace the constants by functions: **y_p = u1 y1 + u2 y2**, with

**u1' = −y2 f / W** and **u2' = y1 f / W**,

where **W = y1 y2' − y2 y1'** is the **Wronskian**, which is non-zero for independent solutions. Integrate to find u1 and u2.

For y'' + 4y = cosec 2x: y1 = cos 2x, y2 = sin 2x and W = 2, so u1' = −1/2 and u2' = (1/2) cot 2x. Then u1 = −x/2 and u2 = (1/4) ln(sin 2x), giving **y_p = −(x/2) cos 2x + (1/4) sin 2x ln(sin 2x)**.

## Initial value problems

After writing the general solution, substitute the initial conditions to find the constants. A third-order equation such as y''' − 6y'' + 11y' − 6y = e^x needs three conditions, y(0), y'(0) and y''(0). Because e^x is in its CF, the trial particular integral is **Ax e^x**.

Source: MAT 241 class slides (A. O. Akeju) (Chapter 4: method of undetermined coefficients); MAT 241 Lecture 5 (Variation of Parameters); MAT 241 past papers. The worked examples are solved here from the past papers.
