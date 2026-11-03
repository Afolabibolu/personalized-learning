# Access and Non-Access Modifiers

## Two groups of modifiers

The `public` in `public class Main` is an **access modifier**: it sets the access level for classes, attributes, methods and constructors. Java divides modifiers into two groups:

- **Access modifiers**, which **control the access level**; and
- **Non-access modifiers**, which **do not control visibility** but add other features.

## Access modifiers

| Modifier | Accessible from |
| --- | --- |
| public | all classes |
| private | only within the declared class |
| default (none written) | only the same package |
| protected | the same package and subclasses |

Think of **public** as a public park that everyone can enter, and **private** as your house key that only you can use. If `Person` has `public String name` and `private int age`, then `p.name` works from another class but `p.age` gives an error: **age has private access in Person**.

## Non-access modifiers

The most commonly used non-access modifiers are **final**, **static** and **abstract**.

- **final**: on an attribute, its value **cannot be changed** after it is set; `myObj.x = 50;` on a `final int x = 10;` gives "cannot assign a value to a final variable". On a method, it **cannot be overridden**. On a **class**, the class **cannot be inherited**.
- **static**: the member **belongs to the class, not to any object**. All objects **share the same static attribute**, and a static method can be **called without creating an object**, either directly or with the class name (`Main.myStaticMethod()`). A static method **cannot use instance variables or instance methods**.
- **abstract**: on a **class**, it **cannot be used to create objects** and must be inherited from. On a **method**, it can only be used in an abstract class and has **no body**, for example `abstract void run();`; the subclass provides the body.

For **classes**, you can use either **final** or **abstract**. For attributes and methods, three more modifiers fine-tune serialisation and concurrency:

- **transient**: the attribute is **skipped when serialising** the object containing it;
- **synchronized**: the method can be accessed by **only one thread at a time**; and
- **volatile**: the value is **not cached thread-locally** and is **always read from main memory**.

In summary, non-access modifiers add behaviour, not visibility control: final locks a value or prevents subclassing, and static ties a member to the class rather than an instance.

Source: COS202_Advanced Java_Programming.pdf (Weeks Three and Four); Inheritance_Interface_Abstraction-2.pdf (Week 6: Non-Access Modifiers)
