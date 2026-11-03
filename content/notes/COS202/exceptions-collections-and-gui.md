# Exceptions, Collections and GUI Programming

## Exceptions

An **exception** is an **event that disrupts the normal flow** of a program, such as dividing an integer by zero (**ArithmeticException**), using a null reference (**NullPointerException**), indexing past the end of an array (**ArrayIndexOutOfBoundsException**) or parsing text that is not a number (**NumberFormatException**). **Checked exceptions** (such as IOException) must be caught or declared with **throws**; **unchecked exceptions** (subclasses of RuntimeException) need not be.

Exceptions are handled with:

```java
try {
    int n = Integer.parseInt(text);
} catch (NumberFormatException e) {
    System.out.println("Please enter a number");
} finally {
    // always runs, for example to close a resource
}
```

The **try** block holds code that may fail, a **catch** block handles a specific exception type, and **finally** runs whether or not an exception occurred. A program can raise an exception itself with **throw**. An exception not caught where it occurs **propagates** up the call stack to the caller. Robust programs validate input and catch exceptions so that bad input gives a helpful message instead of a crash.

## The API and collections

The **Java API** is the library of ready-made classes. Its **collections** grow and shrink as needed, unlike arrays:

- **ArrayList** is a resizable list with `add()`, `get()`, `remove()` and `size()`. The GUI assignment requires courses to be stored in an `ArrayList<Course>`, **not a fixed-size array**.
- A **Stack** is **last in, first out (LIFO)**, with `push()`, `pop()` and `peek()`.
- A **Queue** is **first in, first out (FIFO)**, with `offer()` and `poll()`.
- An **Iterator** visits each element in turn with `hasNext()` and `next()`.

## Event-driven GUI programming

In **event-driven programming**, the program **waits for events**, such as a button click or key press, and responds to each by running a handler. Java's **Swing** library provides components including **JFrame** (the window), **JLabel**, **JTextField**, **JComboBox**, **JButton**, **JTextArea** and **JOptionPane** (pop-up dialogs). A component reports events to an **event listener**, such as an **ActionListener** whose `actionPerformed()` method runs when a button is clicked.

The course's practical assignment combines these ideas: a Student Course Registration and CGPA Calculator with Person and Student classes (inheritance and encapsulation), an ArrayList of courses, Swing forms and listeners, and validation, such as refusing to calculate the CGPA until at least five courses are registered.

Source: Written from general knowledge of COS 202, following the course outline (exceptions, API, List, Stack, Queue, iterators, event-driven and GUI programming); no lecture in the course folder covered this topic. The assignment details are from GUI_Exception_Handler.pdf (Java GUI practical assignment).
