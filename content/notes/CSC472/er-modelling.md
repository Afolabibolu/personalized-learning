# Entity-Relationship Modelling

## Requirement gathering

Conceptual design starts by gathering requirements from stakeholders, with a focus on data, using the fact-finding techniques of systems analysis: **examining documentation**, **interviewing**, **observing** the enterprise in operation, **research** and **questionnaires**. Requirement gathering also records the initial database size, growth rate, types and number of record searches, networking and shared access, performance, security, backup and recovery, and legal issues.

## Entities

An **entity** is an object that exists and is distinguishable from other objects, such as a customer or an account. An **entity set** is a set of entities of the same type that share the same properties (attributes), and each entity set has a key.

- A **strong entity** can be identified by its own attributes, for example Employee.
- A **weak entity** cannot be identified uniquely without the primary key of its **owner** (identifying) entity, for example Dependants of an employee, or a payment of a loan. It must relate to the owner through a **one-to-many** relationship with **total participation**. Its **discriminator** (partial key) distinguishes its entities, and its primary key is the owner's primary key plus the discriminator. Weak entity sets are drawn as **double rectangles**, with the discriminator underlined by a dashed line.

## Attributes

- **Simple** versus **composite (complex):** FirstName versus Address.
- **Single-valued** versus **multivalued:** Gender versus Phone_no.
- **Derived:** computed from other attributes, such as Years_in_service or age.

## Relationships

A **relationship** associates entities, and a **relationship set** relates entity sets; the same entity set can take part in several relationship sets. The **degree** is the number of entity sets that participate:

- **Unary** (recursive), **binary** (degree two, the most common), **ternary** and **n-ary**.

A **recursive relationship** relates an entity set to itself, as when a main branch manages other branches.

## Keys

- **Candidate key:** cannot be null and must be unique; there may be several, such as a matric number.
- **Primary key:** the candidate key chosen to identify the entity.
- **Composite key:** a candidate key of two or more attributes, where only the combination is unique.

## Design choices

- **Entity or attribute?** If an employee has several addresses, or we want the structure of an address (city, street), address must be an entity, because attribute values are atomic.
- **Entity or relationship?** A relationship can be treated as an abstract entity when it needs attributes or relationships of its own.

From the requirements, the designer identifies the entities, their attributes and the relationships, and draws the **ER diagram (ERD)**.

Source: DB Lecture Note 2.pptx (K. T. Ladoja); DBMS Lecture Notes.pdf, Unit I
