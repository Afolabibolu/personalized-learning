# Constructors, Inheritance and Polymorphism

## Constructors and destructors

A **constructor** is a special member function executed whenever a new object of its class is created. It has **exactly the same name as the class** and **no return type**. A **default constructor** has no parameters; a **parameterised constructor** takes parameters, so initial values can be set when the object is created, for example `public Line(double len)`.

A **destructor** runs whenever an object of its class **goes out of scope**. It has the class name prefixed with a **tilde (~)**, returns no value and takes no parameters. It is useful for releasing memory resources before the program exits, and destructors **cannot be inherited or overloaded**.

## Inheritance

**Inheritance**, one of the most important concepts in object-oriented programming, lets us **define a class in terms of another class**, making applications easier to create and maintain and allowing code reuse. Instead of writing completely new members, the new class (the **derived** class) inherits the members of an existing one (the **base** class). Inheritance implements the **IS-A relationship**: a dog IS-A mammal, a mammal IS-A animal, so a dog IS-A animal. The derived class inherits the base class's member variables and methods, so the base (super) class object is created before the subclass; superclass initialisation can be given in the member initialisation list, as in `public Tabletop(double l, double w) : base(l, w)`. **C# does not support multiple inheritance** of classes, but **interfaces** can be used to implement it.

## Polymorphism

**Polymorphism** means having many forms; in object-oriented programming it is often expressed as **"one interface, multiple functions"**.

- **Static polymorphism**: the response to a function is decided at **compile time**. Linking a function to an object at compile time is **early (static) binding**. C# provides **function overloading** (several definitions of one function name, differing in the type or number of parameters) and **operator overloading**.
- **Dynamic polymorphism**: the response is decided at **run time**, through **abstract classes** and **virtual functions**. A virtual function is defined in a class and implemented differently in each inherited class, which **overrides** it.

An **abstract class** provides a partial implementation that derived classes complete. You **cannot create an instance** of an abstract class, abstract methods can only be declared inside one, and an abstract class cannot be **sealed**; a sealed class cannot be inherited.

An **interface** is a **syntactical contract** that every class inheriting it must follow: the interface defines the **"what"** and the deriving classes define the **"how"**. It contains only declarations of its members (properties, methods and events) and is declared with the **interface** keyword.

Source: QuickGuideCsharp.pdf (C# Quick Guide, filed with the course), Classes (constructors and destructors), Inheritance, Polymorphism and Interfaces
