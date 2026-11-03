# Arrays, Methods and Recursion

## Arrays

An **array** is a collection of elements of the **same data type** stored in **contiguous memory locations** and accessed by an **index** starting at **0**. Arrays hold primitive types (int, char, boolean) or objects (String, Integer): **primitive arrays store values** contiguously, while **non-primitive arrays store references**. Once created, an array's **size is fixed**; use **ArrayList** or Vector for growable collections.

- **Declaration** only creates a reference: `int[] arr;` (preferred) or `int arr[];`.
- **Initialisation** allocates memory on the **heap** with `new`: `int[] arr = new int[5];`.
- Elements **auto-initialise** to **0** (numeric), **false** (boolean) or **null** (reference types).
- An **array literal** needs no `new`: `int[] arr = {1, 2, 3};` and its length is inferred.

You access elements by index (`arr[3]`), update them with assignment, and **traverse** with a loop from 0 to `length - 1`.

A **multi-dimensional array** is an **array of arrays** storing data in tabular form; the **2D array** is the most common. Its total size is the **product of the dimension sizes**: `new int[3][5][7]` stores **105** elements. A 2D array `new int[x][y]` is a table of x rows and y columns, accessed as `arr[row][col]`.

## Methods

A **method** is a **block of code that only runs when it is called**; methods are also called functions. A method must be declared **within a class**, is defined once and can be used many times. `static` means it belongs to the class, not an object, and `void` means it returns no value.

**Parameters** act as variables inside the method; the values passed in a call are **arguments**. In `myMethod(String fname)` called as `myMethod("Babatunde")`, `fname` is the parameter and "Babatunde" the argument. A method that returns a value uses a data type instead of void and the **return** keyword. **Method overloading** lets methods share a name with **different parameter lists**, and it is **resolved at compile time**.

## Recursion

**Recursion** is a function **calling itself** to break a complicated problem into simpler sub-problems. Every recursive method needs a **base case** to stop the calls. For example:

```java
public static int sum(int k) {
    if (k > 0) return k + sum(k - 1);
    else return 0;   // base case
}
```

`sum(10)` unwinds as 10 + sum(9), then 10 + 9 + sum(8), down to `sum(0)`, giving **55**. Each call is suspended until the deeper call returns, and the results combine on the way back up.

Source: COS202_Advanced Java_Programming.pdf (Weeks One and Two)
