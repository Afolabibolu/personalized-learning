# Python Basics and Control Flow

## The language

**Python** is a high-level, interpreted, general-purpose language known for readable code. It is **dynamically typed**: a variable's type is decided when the program runs, from the value it holds, and can change, so `x = 5` and later `x = "five"` are both allowed. In a **statically typed** language such as C or Java, each variable's type is declared and checked before the program runs. Blocks of code are marked by **indentation**, not braces, and comments start with `#`.

## Data and input-output

Basic types are **int** (5), **float** (5.0), **str** ("Ade") and **bool** (True, False); collections include **lists** [70, 80, 90], **tuples** and **dictionaries** {"name": "Ade"}. `print()` displays values and `input()` reads text from the user. Because `input()` always returns a string, convert it before arithmetic: `bill = float(input("Total bill: "))`.

Operators: arithmetic `+ - * / // % **` (`//` is integer division, `%` the remainder, `**` the power); comparison `== != < > <= >=`; logical `and`, `or`, `not`. A number is even when `n % 2 == 0`.

## Decisions

```
if bill >= 5000:
    discount = 0.15 * bill
elif bill >= 2000:
    discount = 0.10 * bill
else:
    discount = 0
```

Python tests the conditions in order and runs the first block whose condition is true. This pattern solves tiered problems such as the course test's cafeteria discount.

## Loops

- A **for loop** repeats for each item of a sequence: `for score in scores:` or `for i in range(1, 11):`, which counts 1 to 10 (range stops before its end value).
- A **while loop** repeats while a condition is true, so it suits loops whose number of passes is not known in advance, such as giving a user up to three attempts at a PIN.
- `break` leaves a loop early; `continue` skips to the next pass.

Source: Written from general knowledge of CSC 231; no course file covered this topic.
