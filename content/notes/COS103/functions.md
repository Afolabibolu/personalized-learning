# Functions

## Functions

A **function** is a block of reusable code that performs a specific task. Functions increase **reusability**, improve **readability** and reduce **redundancy**. **Built-in** functions include print(), len() and type(); **user-defined** functions are written with **def**:

```python
def add(a, b):
    return a + b

print(add(3, 5))   # 8
```

A function has a name, zero or more parameters, an optional docstring, a body and a return value. **Defining a function does not run it; it must be called** with its name and round brackets: print_hello().

## Parameters

- **Positional** parameters must be passed in order: add(3, 5).
- **Default** parameters are used when no argument is given: def add(a=1, b=2), so add() gives 3, add(2) gives 4, and with def add(a, b=5), add(3) gives **8**.
- **Keyword** arguments name the parameter, in any order: add(b=6, a=7).

## Return values

A function can return **nothing** (it returns **None** by default), **one value** or **several values as a tuple**: def math_operations(a, b): return a + b, a - b, a * b, so sum_, diff, product = math_operations(10, 5) gives 15, 5, 50. return can end a function early; it is **not** mandatory. **print** only displays a value, while **return** hands it back to the caller.

Functions can call other functions. def sum_of_squares(a, b): return square(a) + square(b) gives 25 for (3, 4). In a **chained call** such as double(add(x, y)), the **inner call runs first**. Functions can be nested: an inner function can use the outer function's variable x = 10 and return x + 5 = 15.

## Scope

- A **local variable** is created inside a function and exists only during the call; using it outside raises an error.
- A **global variable** is defined outside all functions and is accessible throughout the program.
- To **change** a global inside a function, declare it with **global z**. Otherwise Python treats the assignment as a new local variable.

## Recursion and lambdas

A **recursive function** calls itself. It needs a **base case** that stops the recursion and a **recursive case** with a modified argument:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

The results come back in reverse order of the calls.

A **lambda** is a small anonymous function: **lambda arguments: expression**. It is a single expression, with the return implied. square = lambda x: x ** 2 is equivalent to def square(x): return x ** 2. Use lambdas only for very simple functions.

Source: CSC 103 Lecture 3 (2024): functions and lists; CSC 103 2023/24 examination
