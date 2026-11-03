# Operators and Selection Statements

## Operators

**Arithmetic operators** are `+`, `-`, `*`, `/`, `%` (modulus, the remainder), `++` (increment) and `--` (decrement). With two integers, **`/` performs integer division and truncates**: `10 / 3` is **3**, while `10.0 / 3` gives 3.333. `10 % 3` is 1.

**Assignment operators** assign values; **compound** forms combine an operation with assignment: with x = 10, `x += 5` gives 15, `x *= 2` gives 20 and `x %= 3` gives 1.

**Relational operators** compare two values and return a boolean: `==`, `!=`, `>`, `<`, `>=` and `<=`. **Logical operators** combine booleans: `&&` (AND, true only if both are true), `||` (OR, true if at least one is true) and `!` (NOT, reverses the value). With x = 7, `x > 5 && x < 10` is true.

**Operator precedence**, from high to low, is: `()`, then `++`/`--`, then `* / %`, then `+ -`, then relational, then `== !=`, then `&&`, then `||`. So with a = 10, b = 4, c = 3, `a + b * c` is **22**, while `(a + b) * c` is **42**. Use parentheses to make intent explicit.

The **ternary operator** `condition ? valueIfTrue : valueIfFalse` is a compact if-else: `String status = (a >= 50) ? "Pass" : "Fail";`.

## Selection

**Selection (branching)** lets a program **make decisions**, running different code depending on whether a condition is true or false. It is one of the **three fundamental control structures**, with **sequence** and **iteration**.

- **if** runs a block only when the condition is true.
- **if-else** chooses between exactly two paths; **exactly one block always runs**.
- The **else-if ladder** handles more than two outcomes. In the UI grade classifier (A for 70 and above, B for 60, C for 50, D for 45, E for 40, F below), **the order matters**: the highest score is checked first, and the final `else` catches F.
- A **nested if** places an if inside another; more than three levels makes code hard to read.
- **switch** compares a variable against **specific constant values** (case labels), with `default` for no match. Each case needs **break** to prevent **fall-through**; without it, execution continues into the next case.

Use **if-else** for range comparisons, complex conditions and several variables; use **switch** for exact matches against many discrete integer, char or String values.

Source: cos201_weeks3to6.pdf (Week 4: Operators and Expressions; Week 5: Selection); cos 201 L4.pdf (control statements) (control statements)
