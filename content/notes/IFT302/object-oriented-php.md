# Object-Oriented Programming in PHP

## The idea

**PHP OOP organises code into classes and objects** that contain **properties** (variables) and **methods** (functions). **Classes provide structure; objects are individual instances** of classes. **Procedural programming** emphasises sequential commands, while OOP emphasises **objects and their interactions**. OOP gives a clear structure, supports **DRY ("Don't Repeat Yourself")**, improves maintenance and debugging, and reduces duplication.

Its core concepts are **classes and objects**, **encapsulation** (controlling access to internal state with visibility modifiers), **inheritance**, **abstraction** and **interfaces**.

## Classes and objects

```php
class Fruit {
    public $name;
    public $color;
    function __construct($name, $color) {
        $this->name = $name;
        $this->color = $color;
    }
    function get_details() {
        echo "Name: " . $this->name . ". Color: " . $this->color;
    }
}
$apple = new Fruit("Apple", "Red");
$apple->get_details();
```

A class is declared with **class**; objects are created with **new**; and **$this** refers to the **current object**. Each object has its own property values. **instanceof** checks whether an object belongs to a class and returns true or false.

**__construct()** is called **automatically when an object is created** and can initialise its properties. **__destruct()** is called automatically **when the object is destroyed or the script ends**. Both begin with **two underscores**.

## Access modifiers

- **public**: accessible **everywhere**; the **default** when no modifier is given.
- **protected**: accessible **within the class and its child classes**.
- **private**: accessible **only within the class** where it is defined; outside access causes an error.

## Inheritance

A child class **inherits public and protected** members of its parent using **extends**, as in `class Strawberry extends Fruit`. **Private members of the parent are not directly accessible** to the child. A child can add members and **override** an inherited method by redefining it with the same name. The **final** keyword stops a **class from being inherited** or a **method from being overridden**.

## Other features

- **Class constants** are declared with **const**, cannot change, are conventionally uppercase, and are accessed with the scope resolution operator **::**, as in `Goodbye::MESSAGE` outside the class and `self::MESSAGE` inside it.
- An **abstract class** **cannot be instantiated** and contains at least one **abstract method**, declared but not implemented. Child classes must implement it with the same name and the same or a less restrictive access modifier.
- An **interface** defines methods that implementing classes **must provide**.
- **Traits** let classes reuse methods; **static** members belong to the class; and **namespaces** group related code to avoid name clashes.

Source: OOP in PHP.pptx; Web Application Development course content.docx (Week 6)
