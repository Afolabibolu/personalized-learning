# SQL

## Background

SQL began as IBM's **Sequel**, part of the System R project, was renamed Structured Query Language, and is an ANSI and ISO standard. It is **relationally complete**.

## Defining data (DDL)

A relation is defined with **CREATE TABLE**, giving each attribute a domain type:

- **char(n)** fixed-length and **varchar(n)** variable-length strings
- **int** and **smallint** integers
- **numeric(p, d)** fixed-point numbers, and **real**, **double precision** and **float(n)** floating-point numbers

Integrity constraints include **NOT NULL**, **PRIMARY KEY**, **UNIQUE** and **FOREIGN KEY ... REFERENCES**, with actions such as ON DELETE CASCADE or SET NULL.

- **DROP TABLE** removes a relation and all information about it.
- **ALTER TABLE r ADD A D** adds an attribute, with null in every existing tuple; ALTER TABLE can also drop attributes.

## Changing data (DML)

- **INSERT INTO account VALUES ('A-9732', 'Perryridge', 1200)** adds a tuple; it fails if any constraint is violated.
- **DELETE FROM r WHERE ...** removes tuples.
- **UPDATE r SET ... WHERE ...** changes them, for example giving every employee a 10% raise.

## Basic queries

A typical query is SELECT A1, ..., An FROM r1, ..., rm WHERE P, equivalent to a projection of a selection of a cross-product.

- **SELECT** lists the attributes wanted; * means all attributes, and arithmetic expressions are allowed. SQL keeps duplicates unless **DISTINCT** is used (ALL keeps them explicitly).
- **FROM** lists the relations; several give their Cartesian product.
- **WHERE** gives the selection condition, combining comparisons with AND, OR and NOT.
- **AS** renames relations and attributes.
- SQL names are case insensitive.

## Nested queries

A **subquery** is a SELECT-FROM-WHERE expression nested in another query, in WHERE, FROM or HAVING. Set comparisons include **IN**, **EXISTS** and **UNIQUE** and their negations NOT IN, NOT EXISTS and NOT UNIQUE. A **correlated** subquery refers to the outer query and is understood as a nested loop.

## Set operations

**UNION**, **INTERSECT** and **EXCEPT** correspond to the relational algebra operations and remove duplicates; **UNION ALL**, **INTERSECT ALL** and **EXCEPT ALL** keep them. A tuple occurring m times in r and n times in s occurs m + n times in r UNION ALL s, and max(0, m − n) times in r EXCEPT ALL s.

## Aggregates and grouping

The aggregate functions are **COUNT**, **SUM**, **AVG**, **MAX** and **MIN**.

- **GROUP BY** applies them to groups of tuples, for example the average balance at each branch.
- **HAVING** filters groups, for example branches whose average balance is over $1,200. It can contain a subquery.
- Aggregate operations **cannot be nested**.

## Null values

**Null** represents an unknown or inapplicable value. Nulls complicate comparisons and conditions, and aggregate functions simply **ignore** them.

## Views and WITH

CREATE VIEW defines a virtual relation; the **WITH** clause defines a temporary view available only to one query, such as all accounts with the maximum balance.

Source: DBMS Lecture Notes.pdf, Unit II (CSC 472)
