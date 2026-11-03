# Classes, Encapsulation and Methods

## Objects and classes

In the **object-oriented** methodology, a program consists of **objects that interact** by means of actions. The actions an object can take are its **methods**. Objects of the same kind have the same **type**, that is, they belong to the same **class**. A Rectangle object, for example, has attributes **length** and **width**, and needs ways to accept their values, calculate the area and display details. In the class, length and width are **member variables** (data members that store data), and AcceptDetails, GetArea and Display are **member functions**.

## Encapsulation

**Encapsulation** is defined as "the process of enclosing one or more items within a physical or logical package". In object-oriented programming it **prevents access to implementation details**. **Abstraction** and encapsulation are related: abstraction makes relevant information visible, and encapsulation lets the programmer implement the desired level of abstraction.

Encapsulation is implemented with **access specifiers**, which define the scope and visibility of a class member. C# supports:

- **public**: exposes member variables and functions to other functions and objects; any public member can be accessed from outside the class.
- **private**: hides members from other functions and objects; only functions of the same class can access them, and not even an instance of the class can. In the Rectangle example with private length and width, Main cannot touch them, but the public AcceptDetails and Display can.
- **protected**: lets a **child class** access the members of its base class, which helps implement inheritance.
- **internal**: exposes members to other functions and objects in the **current assembly**.
- **protected internal**: hides members from other objects except child classes within the same application.

A class member declared with no access specifier is private by default.

## Methods

A **method** is a group of statements that together perform a task. **Every C# program has at least one class with a method named Main.** To use a method you define it and then call it. The syntax:

`<Access Specifier> <Return Type> <Method Name>(Parameter List) { Method Body }`

The elements are the **access specifier** (visibility), the **return type** (void if nothing is returned), the **method name** (a unique, case-sensitive identifier), the **parameter list** (the type, order and number of parameters; it may be empty) and the **method body** (the statements). A method is called by its name with arguments, for example r.GetArea() on a Rectangle object r.

Source: Introduction to C# Programming Language, weeks 5-10 slides, Object-Oriented Programming; Introduction to C# Programming Language, weeks 10-12 slides, Encapsulation and Methods
