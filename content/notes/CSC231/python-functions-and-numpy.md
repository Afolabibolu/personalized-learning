# Python Functions and NumPy

## Functions

A **function** is a named block of code defined with `def`:

```
def is_even(n):
    return n % 2 == 0
```

**Parameters** receive values when the function is **called** (`is_even(7)`), and `return` sends a result back; a function without return gives None. Variables created inside a function are **local** to it. Functions make programs shorter, reusable and easier to test.

A function can contain a whole simulation. For example, an `atm_simulator()` function can store the correct PIN, loop with a counter while the user has attempts left, read each attempt with `input()`, print "Access Granted" and stop on a correct PIN, and print "Access denied" after three wrong attempts. Here a `while` loop with an attempts counter, or a `for` loop over `range(3)` with `break`, controls the number of tries.

## NumPy

**NumPy** (`import numpy as np`) is Python's main library for numerical computing. Its **ndarray** holds numbers of one type in a grid and is much faster than a list for arithmetic.

- `np.array([[70, 80, 90, 60], [85, 75, 95, 70]])` makes a **2 × 4 matrix**: one row per student, one column per subject. `.shape` gives (2, 4).
- Arithmetic is **element-wise**: `a * 2` doubles every element and `a + b` adds matching elements. **Broadcasting** stretches a smaller array, such as a single number, to match.
- Indexing uses zero-based positions: `a[0, 2]` is row 0, column 2 (90), and `a[:, 1]` is the whole second column.
- **Aggregations along an axis**: `a.mean(axis=1)` averages **across each row** (each student's average: 75.0 and 81.25), and `a.mean(axis=0)` averages **down each column** (each subject's average: 77.5, 77.5, 92.5, 65.0). `sum`, `max` and `min` work the same way.
- `np.linspace`, `np.arange`, `np.zeros` and `np.dot` mirror their MATLAB counterparts.

Source: Written from general knowledge of CSC 231; no course file covered this topic.
