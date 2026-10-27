# Introduction to Database Systems

## Before databases

Before databases, banks kept every transaction by hand in ledgers and filing cabinets: retrieval was slow, errors were common and records could be stolen or damaged. **File-based systems** moved records onto computers but still had problems:

- **Data redundancy and inconsistency:** the same data in several files, so an update in one file is not reflected in another.
- **Data isolation:** data in separate files is hard to combine for reports.
- **Limited data sharing** between departments, **inadequate security** and **no concurrent access** (simultaneous updates corrupt data).
- **Complex data management**, **scalability issues**, **lack of standardization**, **difficult complex queries** and unreliable **backup and recovery**.

Databases and **database management systems (DBMS)** emerged to solve these problems.

## The DBMS environment

A **database** is a collection of interrelated data, and a **DBMS** is the software, a set of programs, that lets users define, access and manage it in a convenient and efficient way. **Data** are raw facts; **information** is processed data. The DBMS environment has five components: **hardware**, **software**, **data**, **procedures** and **people** (database administrators, designers, application developers and end users). A **view** mechanism gives each user their own picture of the data and adds security.

## History

The DBMS arose from the Apollo moon-landing project of the 1960s, which produced more information than any existing system could manage.

- **First generation:** hierarchical (IMS) and network or CODASYL (IDS) systems, mid-1960s.
- **Second generation:** the **relational model**, proposed by **E. F. Codd** of IBM in 1970.
- **Third generation:** object-relational and object-oriented DBMSs.

## Advantages and disadvantages

**Advantages:** data integration and centralization, security, consistency, improved sharing, data independence, backup and recovery, and better access and performance. **Disadvantages:** complexity, cost, performance overhead, a potential single point of failure, vendor lock-in, scalability challenges and security vulnerabilities.

## The three-level architecture

The ANSI-SPARC architecture describes data at three levels:

- **External level:** the users' views of the data.
- **Conceptual level:** the community view: what data is stored and how it is related.
- **Internal (physical) level:** how the data is physically stored.

Its main objective is **data independence**, meaning upper levels are unaffected by changes to lower levels:

- **Logical data independence:** external schemas are immune to changes in the conceptual schema, such as adding an entity or attribute.
- **Physical data independence:** the conceptual schema is immune to changes in the internal schema, such as new file organizations, storage devices or indexes.

## Data models and languages

A **data model** is a set of concepts for describing data, operations on it and integrity constraints. **Object-based** models (entity-relationship, semantic, functional, object-oriented) and **record-based** models (relational, network, hierarchical) describe the conceptual and external levels; **physical** models describe the internal level.

The **Data Definition Language (DDL)** creates and defines the database. The **Data Manipulation Language (DML)** retrieves and changes data; its query part is the **query language**.

Source: DB_LECTURE NOTE 1.pdf (CSC 472 Lecture Note 1, K. T. Ladoja)
