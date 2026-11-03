# Inheritance and Polymorphism

## Inheritance

**Inheritance** is a core OOP concept that allows a class to **acquire the properties and behaviours of another class**, promoting **code reusability** and better organisation. A **subclass** reuses the fields and methods of its **superclass** without rewriting them, and can add or modify its own. The keyword is **extends**, and inheritance represents an **"is-a" relationship**.

## Types of inheritance

- **Single**: a subclass is derived from **only one superclass**.
- **Multilevel**: a derived class inherits a base class and itself acts as the base class for another, forming a **chain**.
- **Hierarchical**: **more than one subclass** is derived from a single base class; cars and buses are both vehicles.
- **Multiple**: **Java does not support multiple inheritance with classes**; it is achieved only through **interfaces**.
- **Hybrid**: a mix of two or more types, achieved through interfaces when multiple inheritance is involved. `Bus extends Vehicle implements Fare` is an example.

## The IS-A relationship

**IS-A** means "this object is a type of that object". If SolarSystem is the superclass of Earth and Mars, and Moon is a subclass of Earth, then Moon is also (transitively) a SolarSystem.

## What a subclass can do

A subclass can use inherited fields and methods directly, **declare new fields and methods**, **override** an inherited instance method with the same signature, **hide** an inherited static method, and write a constructor that invokes the superclass constructor, implicitly or with **super**.

Advantages of inheritance are code reusability, abstraction, class hierarchies and polymorphism. Its limitations are **complexity** (deep hierarchies are hard to follow) and **tight coupling** (superclass changes can break subclasses), so keep hierarchies simple or prefer composition and interfaces.

## Polymorphism

**Polymorphism** means "**many forms**": the same method or object shows **different behaviour depending on context**. For example, `speak()` produces Bark, Meow or Moo depending on whether the object is a Dog, Cat or Cow.

- **Compile-time polymorphism** is **method overloading**: the same name with different parameters, resolved at compile time.
- **Runtime polymorphism** is **method overriding**: a subclass redefines a superclass method, and at runtime Java calls the version that matches the object's **actual type**. Storing several shapes in a `Shape[]` array and printing each area is runtime polymorphism.

Source: Inheritance_Interface_Abstraction-2.pdf (Week 7: Inheritance); COS202_Advanced Java_Programming.pdf (Week Five: inheritance and polymorphism)
