# Object Modelling and the UML

## Objects and classes

**Object-oriented analysis** combines data and the processes that act on it into **objects**.

- An **object** represents a real person, place, event or transaction, such as a student or an instructor.
- Objects have **attributes** (properties) and **methods** (tasks that change the object's properties).
- An object is a member of a **class**, which defines the attributes and methods its objects share.
- A **message** from one object asks another for specific behaviour or information.
- **Inheritance** lets a child class take on the traits of its parent, and **encapsulation** hides an object's internal details.

**Advantages over traditional (structured) modelling:**

- objects model the real world closely, so the model is easier for users to understand;
- objects and classes can be **reused**, saving time and cost;
- encapsulation makes systems easier to maintain and change;
- the same model carries from analysis through design and coding.

## The Unified Modeling Language

The **UML** is a standard set of diagrams for object modelling.

**Use case diagrams** show the **actors** (users or other systems, drawn as stick figures) and the **use cases** (things the system does for them, drawn as ovals) inside a system boundary. In a library, a borrower borrows and returns books and a librarian adds books and issues fines. Two relationships link use cases:

- **include:** one use case always uses another, such as "Borrow book" including "Check membership";
- **extend:** one use case optionally adds behaviour to another under certain conditions, such as "Pay fine" extending "Return book".

**Class diagrams** show classes with their attributes and methods, and the relationships between them, with cardinality:

- **generalization:** an "is a" relationship from a subclass to a superclass, such as Student is a Person;
- **aggregation:** a "has a" or whole-part relationship, such as a Department has Lecturers.

**Sequence diagrams** show objects interacting over time, as messages passed along vertical lifelines.

**State transition diagrams** show how an object changes **state** in response to **events**, drawn as rounded boxes joined by labelled arrows from an initial state to a final state. For example, a borrowed book moves from Available to Reserved, then On Loan, then Overdue or Returned. For a course registration, the states run from logged in through selecting and previewing courses to registered and locked.

**Activity diagrams** show the sequence of activities in a process, like a flowchart, with decisions and parallel paths.

## Organising object models

Object models are refined by grouping related classes into **packages** and identifying the classes, use cases and relationships that the scenarios reveal. Models are checked with users, much as DFDs are reviewed.

Source: general knowledge, following the CSC 302 past papers (2021/22 Question 1(vi), the 2020/21 test Question 2, and the 2020/21 and 2024/25 papers on use case and state transition diagrams); the lecture slides introduce object-oriented analysis and the UML in Chapters 1 and 4
