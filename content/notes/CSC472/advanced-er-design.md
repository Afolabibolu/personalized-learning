# Structural Constraints and Enhanced ER Design

## Attributes on relationships

A relationship can have its own attributes. In "each pharmacy sells several drugs and has a price for each", **price** belongs to the Sells relationship between Pharmacy and Drug, not to either entity.

## Structural constraints

**Multiplicity** is the number (or range) of possible occurrences of an entity type that may relate to a single occurrence of an associated entity type through a relationship. It represents the enterprise's **business rules**. Binary relationships are:

- **One-to-one (1:1):** a member of staff manages a branch.
- **One-to-many (1:\*):** a member of staff oversees properties for rent.
- **Many-to-many (\*:\*):** newspapers advertise properties for rent.

Multiplicity is made up of two constraints:

- **Cardinality:** the **maximum** number of relationship occurrences for an entity; the maximum values of the multiplicity ranges, such as 1:1.
- **Participation:** whether **all** entity occurrences take part in the relationship (**mandatory**) or only **some** (**optional**).

For an **n-ary** relationship, multiplicity is the range of occurrences of one entity type when the other n−1 values are fixed. Not every integrity constraint can be shown in an ER model.

## Connection traps

- A **fan trap** exists where a model represents a relationship between entity types, but the pathway between certain entity occurrences is **ambiguous**.
- A **chasm trap** exists where a model suggests a relationship between entity types, but the pathway **does not exist** between certain entity occurrences.

## Superclasses and subclasses

- A **superclass** is an entity type with one or more distinct subgroupings that must be represented in the model, such as Staff.
- A **subclass** is one such distinct subgrouping, such as Manager.

The superclass/subclass relationship is one-to-one. These concepts avoid describing similar concepts more than once and add meaning: "Manager IS-A member of staff". A subclass **inherits** the attributes of its superclass. An entity with its subclasses, and theirs, is a **type hierarchy**, also called a specialization, generalization or **IS-A hierarchy**.

## Specialization and generalization

- **Specialization:** maximizing the differences between members of an entity by identifying their distinguishing characteristics; a **top-down** approach.
- **Generalization:** minimizing the differences between entities by identifying their common characteristics; the reverse, **bottom-up** process.

Two constraints may apply:

- **Participation constraint:** **mandatory** (every superclass member must belong to a subclass) or **optional** (it need not).
- **Disjoint constraint:** applies only when there is more than one subclass. If the subclasses are **disjoint**, an entity can be a member of only one subclass; otherwise they may overlap.

## Aggregation

**Aggregation** represents a "has-a" or "is-part-of" relationship between a "whole" and a "part", as in Branch Has Staff and Branch Offers PropertyForRent.

Source: LN_Week 3- Database Systems.pdf (CSC 472 Lecture Note 3, K. T. Ladoja); DB Lecture Note 2.pptx
