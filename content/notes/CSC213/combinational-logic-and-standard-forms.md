# Combinational Logic and Standard Forms

## Combinational logic circuits

**Combinational logic circuits (CLCs)** are made by connecting basic logic gates. Their outputs depend **only on the present combination of inputs**, because they have no feedback; when an input changes, the output changes at once. Any CLC can be built from NAND or NOR gates alone. There are three main ways to specify a CLC:

1. **Truth table**: every possible input combination with its output. An n-input circuit has **2ⁿ combinations**, so 3 inputs give 8 rows and 4 inputs give 16.
2. **Boolean expression**: for example, an alarm that rings when the front (F) or back (B) sensor fires and the noise sensor (N) also fires is Alarm = (F + B) · N. Brackets matter: without them, F + B · N means something else, because AND takes precedence over OR. A NOT bar over a single variable takes precedence; a bar over an expression acts like brackets.
3. **Logic circuit diagram**: the gates and their wiring. A dot shows that crossing lines are connected.

You can move between the three: write the expression at each gate's output to get the function from a diagram, then build the truth table column by column. To **evaluate** an output, substitute the input values into the expression.

## Standard forms

Two standard forms pass every signal through just two layers of gates (apart from inverters), giving predictable speed:

- A **product term** ANDs inputs, each true or complemented. A **sum of products (SOP)** ORs product terms, such as Y = ĀB + B̄C. One bar may not cover more than one input in a term, and there are no brackets.
- In the **fundamental (canonical) SOP**, every product term contains all the input variables. These terms are **minterms**: each gives a 1 in exactly one row of the truth table and is numbered by that row, so ĀBC̄ ≡ 010 = m2. A function can then be written Y = Σm(…). Any truth table converts directly to a fundamental SOP by ORing the minterms of the rows whose output is 1.
- A **sum term** ORs inputs; a **product of sums (POS)** ANDs sum terms. In the fundamental POS, each sum term contains every variable and is a **maxterm (M)**; each maxterm puts a 0 in one row.

To expand an SOP to fundamental form, multiply each term missing a variable X by (X + X̄).

Source: CSC 213 DLC course book.pdf (Digital Logic Design, Nancy C. Woods), Lecture Six (Combinational Logic Design) and Lecture Seven (Standard Forms of Expression)
