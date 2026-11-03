# Database and File Design

## Why data design matters

Data is one of the major assets of an information system. **Poor data design causes duplication, inconsistent records, difficult maintenance and unreliable reports.** The design flow is: **requirements → ERD → relational schema → normalisation → MySQL implementation → testing**.

- **Data** is raw facts (a matric number or score); **information** is processed data that has meaning and supports decisions.
- A **file** is a structured collection of records; a **database** is an organised collection of related data managed for storage, retrieval and sharing; and a **DBMS** is the software that defines, manipulates, secures and administers databases.

## File organisation

- **Sequential**: records in order, useful for **batch processing**.
- **Heap (unordered)**: no required order, so insertion is simple.
- **Indexed**: an index gives an extra access path.
- **Hash**: a hash function maps keys to storage locations for fast **equality lookup**.
- **Clustered**: related records are stored together.

File organisation is about **how records are stored and accessed**; database design is about **what data exists, how it relates and which rules keep it correct**.

## Design principles

Start from requirements and business rules; model real-world **entities, attributes and relationships**; choose stable identifiers; minimise redundancy; use constraints; and separate distinct concepts into tables.

## Keys

- A **superkey** can identify a row; a **candidate key** is a **minimal superkey**.
- The **primary key** is the candidate key **chosen** as the main identifier; **alternate keys** are candidates not chosen.
- A **foreign key** references a key in another table and so **creates a relationship**.
- A **surrogate key** is an artificial identifier, such as an AUTO_INCREMENT student_id; a **natural (business) key** is a real-world identifier, such as matric_no, which can stay **UNIQUE** even when a surrogate key is the primary key.

## Integrity

- **Entity integrity**: primary key values are **unique and not NULL**.
- **Referential integrity**: foreign key values must **match an existing parent key** (or be NULL where permitted).
- **Domain integrity**: values conform to their type, range and format.
- Key constraints and **business-rule constraints** enforce uniqueness and organisational rules.

## Normalisation and relationships

**Normalisation** organises tables to reduce redundancy and update anomalies:

- **First normal form (1NF)**: each attribute holds a **single, atomic value**, with no repeating groups.
- **Second normal form (2NF)**: 1NF, and every non-key attribute depends on the **whole** primary key (no partial dependency).
- **Third normal form (3NF)**: 2NF, and **no non-key attribute depends on another non-key attribute** (no transitive dependency).

An **ERD** becomes tables: each entity becomes a table, attributes become columns, and relationships become foreign keys. Relationships are **one-to-one**, **one-to-many** (the foreign key goes on the "many" side) and **many-to-many**, which needs a **junction (linking) table**, as between students and courses.

Source: System Analysis and Design: Database and File Design slides. The wording of the 2NF and 3NF definitions and the junction-table rule is from general knowledge, as the slides give them mainly in diagrams.
