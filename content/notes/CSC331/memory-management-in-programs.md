# Memory Management in Programs

## Three memory areas

**Memory management** binds values to memory, considering both their static and their dynamic characteristics. While a program runs, its address space is divided into three parts:

- **Static area:** values whose size is known before run time and stays constant, such as global and static variables.
- **Run-time stack:** the centre of control for active methods, holding their local variables and parameter-argument links. It is a contiguous region that grows and shrinks at one end.
- **Heap:** all other values allocated dynamically at run time. Its active blocks are scattered unpredictably and reached through **pointers**.

The stack and heap must not meet; if they do, a **stack overflow** occurs.

## Stack frames

Each time a method is called, including main, a **stack frame** is pushed onto the run-time stack. It holds:

- the argument values and the method's local variables;
- a **static link** to the static area;
- a **dynamic link** to the frame of the calling method.

The frame is popped when the method returns. At any moment the stack holds one frame for every active call, with the most recent on top.

## Garbage collection and memory leaks

The heap becomes **fragmented** as blocks are allocated and freed, so languages use **garbage collection** to reclaim blocks that are no longer referenced.

- In **C++** an object created on the heap stays there until the programmer frees it. Forgetting to free it causes a **memory leak**, which **destructors** help prevent.
- **Java** creates all objects on the heap, and its JVM collects garbage automatically, so programmers need no destructors.

## Parameter passing

- **Pass by value:** the argument's value is copied into the parameter at the call, so changes inside the method do not affect the caller. Used widely in C, C++, ADA and Java.
- **Pass by reference:** the argument's **address** is given to the parameter, so assignments inside the method change the caller's variable. It suits arrays, structures and objects, or cases where the argument must change. Its disadvantage is side effects on the original. In C++, & marks a reference parameter.

In Java, elementary types are passed by value, while arrays and objects are passed as a copy of their reference.

## Pointers, arrays and structures

- A **pointer** holds a memory address, giving a level of indirection; C marks it with *. Pointers build structures such as linked lists, but complicate memory management.
- An **array** is an ordered finite sequence of values of the **same type**, 0-indexed in C, C++ and Java. Java pre-initialises array elements (numbers to zero, booleans to false).
- A **structure (record)** groups elements of **different types**, such as C's struct or a Java class.

Source: CSC 331 Programming Principles and Paradigms.pdf (course book), Study Session 13 (memory management, run-time memory structure, stack frames, argument-parameter linkage, pointers, arrays, structures) and Study Session 3 (3.6, C++ memory leaks and Java garbage collection)
