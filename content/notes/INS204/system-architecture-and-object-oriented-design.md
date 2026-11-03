# System Architecture and Object-Oriented Design

## System architecture

**System architecture** is the **high-level structure of a system**: its major components, responsibilities, connections, data flows and deployment environment. It decides **where the user interface, business processing, data, security and infrastructure reside and how they communicate**. Architecture matters for **performance, scalability, security, availability, maintainability and cost**.

## Architectures

- **Client-server**: a **client** (browser, mobile or desktop app) **requests** a resource and a **server** (web, application or database server) **processes it and responds**, over a network.
- **Two-tier**: the client holds the **UI and application logic** and connects to a **database server**. It is simple and suits small departmental applications, but clients may connect directly to the database.
- **Three-tier**: (1) the **presentation layer** (browser or mobile UI), (2) the **application or business layer** (authentication, validation, business rules) and (3) the **data layer** (database and files). Its benefits are **separation of concerns**, **security** (clients do not access the database directly), maintainability, independent **scalability**, **reusability** across web and mobile clients and testability.
- **Web architecture**: the browser sends HTTP/HTTPS requests to a **web server**, which passes processing to an **application server** backed by a **database**.
- **Cloud architecture**: users reach services over the Internet through a **load balancer** to scalable servers and a cloud database, with **resource pooling** and **elasticity**.

**Centralised** systems keep processing and data on a central server that all users access: easier to control but a single point of failure. **Distributed** systems spread components across several machines and locations: more scalable and resilient but more complex. Hardware and software choices (servers, storage, networks, operating systems, DBMS) must fit the requirements.

## Object-oriented analysis and design

**OOAD** analyses and designs a system in terms of **objects, their properties, behaviours and relationships**. **Object-oriented analysis** asks **what** the system must do (actors, requirements, objects); **object-oriented design** asks **how**, through classes, methods and relationships.

- An **object** has **identity, state** (its data) and **behaviour** (its operations): a Student object has studentID and level, and registerCourse() and payFees().
- A **class** is a **blueprint** for objects; **attributes** describe what an object has and **methods** what it can do.

The four principles are:

1. **Encapsulation**: bundling data with its methods and controlling access, as a BankAccount keeps its balance private.
2. **Inheritance**: a subclass acquires features of a superclass, an **IS-A** relationship (Student and Lecturer inherit from Person).
3. **Polymorphism**: "many forms", as makeSound() barks for a Dog and meows for a Cat.
4. **Abstraction**: showing essential features and hiding details, as an ATM's withdraw().

**UML (Unified Modelling Language)** models OO systems. A **use case diagram** shows **actors** and the **use cases** they perform; a **class diagram** shows classes, attributes, methods and relationships; an **activity diagram** shows workflow; and a **sequence diagram** shows objects exchanging messages over time. **Structured design** centres on **processes and data flows** (DFDs); **object-oriented design** centres on **objects that combine data and behaviour**.

Source: System Architectural Design lecture slides; OOAD 200L Comprehensive Lecture Note
