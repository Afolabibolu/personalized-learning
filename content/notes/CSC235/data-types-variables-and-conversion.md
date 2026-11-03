# Data Types, Variables and Type Conversion

## Value types

**Value type** variables can be assigned a value directly. They derive from **System.ValueType** and **directly contain data**; when you declare an int, the system allocates memory to store the value. Examples of primitive value types:

- **bool**: Boolean value, True or False, default False.
- **byte**: 8-bit unsigned integer.
- **char**: 16-bit Unicode character, U+0000 to U+ffff.
- **int** and **long**: integers; **float** and **double** (64-bit double precision): floating point numbers.
- **decimal**: 128-bit precise decimal values with 28 to 29 significant digits, default 0.0M.

## Reference types

**Reference types** (non-primitive types) **do not contain the actual data** but a **reference** to a memory location. Several variables can refer to the same location, so if one of them changes the data, the others reflect the change. The built-in reference types are **object**, **dynamic** and **string**.

- **object** is the ultimate base class for all data types in the C# **Common Type System**; it is an alias for System.Object and can hold values of any type. Converting a value type to object is **boxing**; converting it back is **unboxing** (`obj = 100;` boxes 100).
- **dynamic** variables can store any type; their type checking happens at **run time**, whereas for object variables it happens at **compile time**.
- **string** is an alias for System.String, derived from object. Literals are **quoted** ("Tutorials Point") or **@quoted** (@"Tutorials Point").

**Pointer types** store the memory address of another type, with the same capabilities as pointers in C or C++.

## Type conversion

**Type conversion** (type casting) converts data from one type to another, in two forms:

- **Implicit** conversion is performed by C# in a **type-safe** way, such as from smaller to larger integral types (a long can hold any int) or from a derived class to its base class. No special syntax is needed.
- **Explicit** conversion is done by the user with a **cast operator** when information might be lost. To cast, put the target type in parentheses: `double d = 5673.74; int i = (int)d;` gives 5673.

## Variables

A variable is declared as `<data_type> <variable_list>;`, for example `int i, j, k;`, and can be initialised at declaration with an equals sign and a constant expression: `int d = 3, f = 5;` or `double pi = 3.14159;`. **A variable is not usable until it is declared.**

Source: Introduction to C# Programming Language, weeks 5-10 slides, Data Types, Type Conversion and Variables
