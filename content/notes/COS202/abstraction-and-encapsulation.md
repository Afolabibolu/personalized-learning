# Abstraction and Encapsulation

## Abstraction

**Abstraction** is the process of **hiding internal implementation details and showing only essential functionality** to the user. It focuses on **what an object does rather than how**. An **ATM**, a coffee machine or a **TV remote** is an example: users press a button without knowing how it works inside. Abstraction hides complexity, improves maintainability (internal changes do not affect code that depends only on the abstraction) and enhances flexibility through loose coupling.

It is achieved in two ways:

- **Abstract classes**, which give **partial abstraction**; and
- **Interfaces**, which give **abstraction for behaviour** (described in the slides as up to 100% abstraction).

## Abstract classes and methods

An **abstract class** is declared with the **abstract** keyword and **cannot be instantiated directly**: `Animal myObj = new Animal();` gives a compile error if Animal is abstract. To use it, another class must **inherit** from it. It may contain **both abstract methods (no body) and concrete methods (with a body)**, and can have **constructors, instance variables and static members**.

An **abstract method** can only be declared in an abstract class and **has no body**; the **subclass supplies the body**:

```java
abstract class Shape {
    abstract double area();
}
class Circle extends Shape {
    double r;
    double area() { return Math.PI * r * r; }
}
```

Here Shape defines common properties, and Circle and Rectangle each supply their own `area()`.

**Advantages** of abstraction: complex systems are easier to understand, parts are kept separate, code is maintained more efficiently, and **security** increases by exposing only necessary detail. **Limitations**: unnecessary abstraction adds complexity, debugging can be harder because implementation is hidden, extra classes increase code volume, too many layers hurt comprehension, good design needs careful planning, and it **adds little benefit in small programs**.

## Encapsulation

**Encapsulation** **wraps data and methods into a single unit (a class)** and **restricts direct access** to the data. Data members are hidden with the **private** modifier, and access is provided through **public getter and setter methods**. This improves **data security**, maintainability and **controlled access**: a setter can reject an invalid value before it is stored.

In short, **abstraction hides "how"**, while **encapsulation protects "what"** (the data).

Source: Inheritance_Interface_Abstraction-2.pdf (Week 8: Abstraction); COS202_Advanced Java_Programming.pdf (Week Five: abstraction and encapsulation)
