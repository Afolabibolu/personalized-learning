# The Relational Model and Relational Algebra

## Relations

A **relational database** is a set of **relations**. A relation has:

- a **schema**: the relation's name and the name and type of each column, as in Students(sid: string, name: string, login: string, age: integer, gpa: real);
- an **instance**: a table of rows and columns. The number of rows is the **cardinality**, the number of fields the **degree** (arity), and all rows are distinct.

## Integrity constraints

An **integrity constraint (IC)** is a condition that must hold for every instance, such as a domain constraint. ICs are specified with the schema and checked whenever relations change; a **legal instance** satisfies them all. They come from the meaning of the real-world enterprise: an instance can show that an IC is violated but never prove it holds.

- A set of fields is a **key** if no two distinct tuples agree on all of them and no subset has this property. A set containing a key is a **superkey**, such as {sid, gpa}.
- A relation may have several **candidate keys** (declared UNIQUE in SQL); one is chosen as the **primary key**.
- A **foreign key** is a set of fields that refers to a tuple in another relation, like a logical pointer, and must match that relation's primary key. If all foreign keys are enforced, there are no dangling references: **referential integrity**.

When a referenced tuple is deleted, SQL offers four options: **NO ACTION** (the default; the delete is rejected), **CASCADE** (delete the referring tuples too), **SET NULL** and **SET DEFAULT**. Inserting a tuple whose foreign key refers to a non-existent tuple is rejected.

## Views

A **view** is a virtual relation defined by a query (CREATE VIEW v AS query). Views present needed information while hiding details, for security, and simplify other queries.

## Relational algebra

The basic operations are:

- **Selection (σ):** selects the rows that satisfy a condition.
- **Projection (π):** keeps only the listed columns, eliminating duplicates.
- **Cross-product (×):** combines every tuple of two relations.
- **Set difference (−):** tuples in the first relation but not the second.
- **Union (∪):** tuples in either relation.

Union, intersection and difference need **union-compatible** relations. Useful additional operations are **intersection**, **join**, **division** and **renaming**:

- A **condition (theta) join** is a cross-product followed by a selection.
- An **equi-join** has only equalities in its condition.
- A **natural join** is an equi-join on all common fields.

The result of each operation is a relation, so operations can be composed.

## Relational calculus

**Relational calculus** comes in two forms, **tuple (TRC)** and **domain (DRC)**, and uses variables, constants, comparison operators, logical connectives and quantifiers. Its expressions are **formulas**. Every query expressible in relational algebra can be expressed in safe relational calculus, and a query language that can express all of them, such as SQL, is **relationally complete**.

Source: DBMS Lecture Notes.pdf, Units I and II (CSC 472)
