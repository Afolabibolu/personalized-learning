# Interfaces

## What an interface is

An **interface** defines a **contract that specifies the behaviour a class should provide**. A class **implements** an interface with the **implements** keyword and supplies implementations for its abstract methods. Key facts:

- A class **can implement multiple interfaces**, separated by commas, which gives Java **multiple inheritance of type**.
- **All variables in an interface are public, static and final** by default.
- Interfaces can also contain **default** and **static** methods with implementations.

If the interface `Shape` declares `calculateArea()`, then Circle and Rectangle implement it with their own calculations. References of the interface type can hold either object, and Java decides which method to call **at runtime**: this is **dynamic method dispatch**.

## Class or interface?

Use a **class** when you need to represent a real-world entity with attributes and behaviours, or objects that hold state and perform actions. Use an **interface** when you need a **contract for behaviour that several classes can implement**, or want abstraction and multiple inheritance. A class can extend another class, and an interface can **extend** another interface, but **only a class can implement an interface**; an interface cannot implement a class.

## JDK 8 and JDK 9 features

| Feature | Behaviour |
| --- | --- |
| Default methods (Java 8) | Provide a body; inherited by implementing classes; can be overridden |
| Static methods (Java 8) | Called through the interface name; **not inherited** |
| Functional interfaces (Java 8) | **Exactly one abstract method**; usable with **lambda expressions** |
| Private methods (Java 9) | Internal helpers for default or static methods; not inherited or overridable |
| extends between interfaces | The child interface inherits all the parent's abstract methods |

**Default methods** are useful for **adding new methods to an interface without breaking existing implementing classes**. The **@FunctionalInterface** annotation is optional but recommended. A class implementing a child interface must implement **all methods in the inheritance chain**.

## Bringing OOP together

The course's key concepts fit together: **classes and objects** (blueprint and instance, attributes, new), **non-access modifiers** (final, static, abstract, transient, synchronized, volatile), **inheritance** (single, multilevel, hierarchical, multiple through interfaces, hybrid; IS-A), **abstraction** (abstract classes and methods) and **interfaces** (contracts, multiple implementation, default, static and private methods, functional interfaces). Interfaces enable flexible, decoupled designs.

Source: Inheritance_Interface_Abstraction-2.pdf (Week 9: Interfaces; Week 10: Advanced Interface Features and Review)
