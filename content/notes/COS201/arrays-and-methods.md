# Arrays and Methods

## Arrays

An **array** is a **fixed-size, ordered collection of elements of the same data type** stored in contiguous memory. Its length is set at creation and **cannot change**; it is **zero-indexed**, so the first element is at index 0 and the last at **length - 1**.

Arrays are declared and initialised in three common ways: `int[] marks = new int[5];` (five slots, default value 0), `double[] prices = new double[4];` (default 0.0), or with an initialiser list, `int[] nums = {3, 6, 9, 12, 15};`. You access an element by index (`nums[4]` is 15), change it (`nums[2] = 99;`) and read the length with the **`.length` property**.

Arrays are traversed with a **standard for loop** when the index is needed (`for (int i = 0; i < scores.length; i++)`), an **enhanced for-each** loop when you only read values, or a while loop.

A **2D array** is an **array of arrays**, useful for matrices and tables, and accessed as `matrix[row][col]`: in `{{1,2,3},{4,5,6},{7,8,9}}`, `matrix[1][2]` is **6**. It is traversed with nested loops.

The **java.util.Arrays** class offers `sort()` (ascending), `toString()`, `binarySearch()` (the array **must be sorted first**), `copyOf()`, `equals()` and `fill()`.

## Modularity and methods

**Modularity** has three ideas: **separation** (dividing a program into independent, self-contained pieces), **encapsulation** (hiding internal details and exposing only what callers need) and **reusability** (write once, use many times).

A **method** groups statements under a name so they can be called repeatedly:

```java
public static int add(int a, int b) {
    return a + b;
}
int result = add(3, 7);   // 10
```

It has an access modifier, a **return type**, typed **parameters** and a `return` statement. Use **void** when a method performs an action and a return type when it computes a result. **Primitive parameters are passed by value**, so changes inside the method do not affect the caller.

**Method overloading** lets several methods share a name if their **parameter count or types differ**; the **return type alone does not overload**.

A **recursive method** calls itself on a smaller version of the problem, such as `factorial(n) = n * factorial(n - 1)` with `factorial(0) = 1`, so `factorial(4)` is 24. **Every recursive method needs a base case**, or it runs until a **StackOverflowError**. Java 9 added the **module system (JPMS)**, where `module-info.java` declares what a module exports and requires.

Source: COS201_Java_Programming.pptx (Arrays, Modularity and Methods)
