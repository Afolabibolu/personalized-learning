# Classes, Objects and Constructors

## Object-oriented programming

**Object-oriented programming (OOP)** is a paradigm based on **objects that bundle data (fields) and behaviour (methods)**, closely modelling real-world entities. It **improves code reusability**, **enhances maintainability and scalability**, and makes programs easier to understand and manage.

## Classes and objects

A **class** is a **blueprint for creating objects**: it encapsulates the **fields (state)** and **methods (behaviour)** common to all objects of that type. For example, **Car** is a class, and BMW, Mercedes and Audi are **objects (instances)** of it; **Dog** is a class and Tommy an object.

An **object** is an **instance of a class** that represents a real-world entity. It has:

- **State**: its current data or attributes;
- **Behaviour**: the actions it can perform; and
- **Identity**: a unique identity in memory that distinguishes it from other objects, **even if they contain the same data**.

Objects are created with the **new** keyword: `Main myObj = new Main();`. Variables declared inside a class are **attributes** (also called **fields**). They are accessed and modified with **dot syntax**, as in `myObj.x = 40;`, and each object holds **its own state**.

## Constructors

A **constructor** is a **special member of a class that is automatically invoked when an object is created**. It initialises the object's data members and sets up its initial state. Its rules:

- The constructor name **must be the same as the class name**.
- It has **no return type, not even void**.
- It is called automatically when an object is created with **new**.

```java
public class Main {
    int x;
    public Main(int y) { x = y; }
    public static void main(String[] args) {
        Main myObj = new Main(5);
        System.out.println(myObj.x);   // 5
    }
}
```

**All classes have constructors by default**: if you do not write one, Java creates one for you, but then you cannot set initial values for attributes. Constructors can take several parameters, such as a model year and model name for a car.

## Types of constructor

- **Default constructor**: has **no parameters** and initialises with default values.
- **Parameterised constructor**: accepts parameters to set specific values.
- **Copy constructor**: creates a new object by **copying another object's data**.
- **Private constructor**: has private access and **prevents creating objects from outside the class**.

Source: COS202_Advanced Java_Programming.pdf (Week Three); Inheritance_Interface_Abstraction-2.pdf (Week 5: Classes, Objects and Attributes)
