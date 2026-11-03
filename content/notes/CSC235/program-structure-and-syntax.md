# C# Program Structure and Basic Syntax

## Parts of a C# program

A C# program consists of: a **namespace declaration**, a **class**, class **methods**, class **attributes**, a **Main method**, **statements and expressions**, and **comments**. The minimal Hello World program shows each part:

- `using System;` The **using** keyword includes the System namespace; a program can have several using statements.
- `namespace HelloWorldApplication` A **namespace** is a collection of classes; this one contains the class HelloWorld.
- `class HelloWorld` The **class** declaration; a class contains the data and method definitions the program uses.
- `static void Main(string[] args)` The **Main method** is the **entry point** of every C# program; it states what the class does when executed.
- `/* my first program in C# */` A comment, ignored by the compiler.
- `Console.WriteLine("Hello World");` **WriteLine** is a method of the **Console** class in the System namespace; it displays the message.
- `Console.ReadKey();` makes the program wait for a key press, so the screen does not close at once in Visual Studio.

Points to note:

- **C# is case sensitive.**
- **All statements and expressions must end with a semicolon (;).**
- **Program execution starts at the Main method.**
- Unlike Java, the **file name can differ from the class name**.

## Comments

**Multi-line comments** start with `/*` and end with `*/`; **single-line comments** start with `//`. Compilers ignore comments, which explain the code.

## Identifiers

An **identifier** is a name for a class, variable, function or other user-defined item. The rules:

1. It must begin with a **letter**, followed by letters, digits (0 to 9) or underscores; the first character **cannot be a digit**.
2. It must not contain embedded **spaces** or symbols such as ? - + ! @ # % ^ & * ( ) [ ] { } . ; : " ' / \, though an underscore ( _ ) is allowed.
3. It must **not be a C# keyword** such as abstract, bool or break.

Common naming styles are **camel case** (firstName), **Pascal case** (FirstName) and **Hungarian notation** (strFirstName).

In the Rectangle example, the class has **member variables** length and width (attributes that store data) and **member functions** AcceptDetails, GetArea and Display (statements that perform specific tasks).

Source: Introduction to C# Programming Language, weeks 5-10 slides, Program Structure, Basic Syntax and Identifiers
