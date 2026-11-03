# Microsoft Access and Databases

## Databases

**Microsoft Access 2013** is a **relational database application** for entering, managing and reporting on large amounts of data. A **database** is a **collection of data stored in a computer system**; think of it as a **collection of lists (tables)**, such as a store's customers, items and staff. Excel is good at numbers, but **Access is far stronger at non-numerical data** such as names and descriptions. What sets databases apart is **connectivity**: a **relational database** understands how lists relate, **without repeating data**.

## The four Access objects

- **Tables** store the data; they are the true "base of data", and everything else depends on them.
- **Queries** show a selection of data from one or more tables, **limiting records with criteria** and showing only the fields you want; running a query is like asking the database a detailed question.
- **Forms** give a **user-friendly** way to view and enter data.
- **Reports** **print data in a formatted structure**, grouping it.

Each object has a **Design View** (where its structure is built) and a data view: **Datasheet View** for tables and queries, **Form View** for forms and **Report View** for reports.

## Planning and design rules

Plan the **input**, **output** and **process**, then follow these rules:

- **Organise data** into several tables rather than numbered columns such as Medication1 and Medication2.
- **No derived fields**: derive data, such as a patient's name, from related tables.
- Break data into its **smallest logical parts**.
- Use **descriptive** and **unique field names** (does "DOB" mean date of birth?).
- **No calculated fields** in tables; calculate in queries, forms and reports.
- Keep **records unique** with a **primary key**, which allows **no duplicates and no blanks**; an **AutoNumber** gives a unique number when no natural key exists.

## Tables

In **Design View** you give each **field name**, its **data type** and properties. Data types include **Short Text** (up to **255** characters), **Number**, **Date/Time**, **AutoNumber**, **Yes/No** and the **Lookup Wizard**. A **key symbol** marks the primary key. Data entered in Datasheet View saves itself, but **structural changes must be saved manually**.

## Terms

A **field** is one column, common to all records and holding one type of data; a **record** is one row with all the data about one entry; a **table** is one set of related data; and a **database** is a structured collection of related tables. The ribbon's four standard tabs are **Home, Create, External Data** and **Database Tools**.

In entity-relationship terms, an **entity** is a thing about which data is kept (a table), an **attribute** is a property of it (a field), and a **relationship** links entities, with a cardinality of one-to-one, one-to-many or many-to-many. A **foreign key** is a field that refers to another table's primary key.

Source: CSC 272 lecture Notes.pdf (Dr N. C. Woods) (Lectures Nine to Eleven, Microsoft Access); the final paragraph on entities, cardinality and foreign keys is from general knowledge, because the past papers ask about them
