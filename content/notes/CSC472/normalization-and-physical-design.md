# Functional Dependencies, Normalization and Physical Design

## The evils of redundancy

Storing the same information in more than one place causes:

- **Redundant storage:** some information is stored repeatedly.
- **Update anomalies:** updating one copy leaves the others inconsistent.
- **Insertion anomalies:** some information cannot be stored without other, unrelated information.
- **Deletion anomalies:** some information cannot be deleted without losing other information.

The main refinement technique is **decomposition**: replacing a relation such as ABCD with smaller ones such as AB and BCD.

## Functional dependencies

A **functional dependency (FD)** X → Y holds over a relation R if, in every allowable instance, two tuples that agree on X also agree on Y. FDs are integrity constraints that identify redundancy. The **closure** F+ of a set F of FDs is every FD implied by F. **Armstrong's axioms** generate it:

- **Reflexivity:** if Y ⊆ X, then X → Y.
- **Augmentation:** if X → Y, then XZ → YZ.
- **Transitivity:** if X → Y and Y → Z, then X → Z.

They also give **decomposition**: if X → YZ then X → Y and X → Z. To test whether X → Y holds, compute the **attribute closure** X+ instead of F+.

## Normal forms

Each normal form is stricter than the last: every BCNF relation is in 3NF, every 3NF relation in 2NF, and every 2NF relation in 1NF.

- **1NF:** every field holds only atomic values, not lists or sets.
- **2NF:** in 1NF, and every nonprime attribute is **fully** functionally dependent on a whole key, not on part of it. EMP_PROJ2(SSN, PNO, HOURS, ENAME, PNAME) violates it because SSN → ENAME and PNO → PNAME; it decomposes into (SSN, PNO, HOURS), EMP(SSN, ENAME) and PROJ(PNO, PNAME).
- **3NF:** in 2NF, and no nonprime attribute depends **transitively** on a key. In SUPPLIER(SNAME, STREET, CITY, STATE, TAX), STATE → TAX is nonkey to nonkey, so TAX moves to TAXINFO(STATE, TAX). Formally, every FD X → A is trivial, or X contains a key, or A is part of some key.
- **BCNF:** for every FD X → A, either it is trivial or X contains a key: the only non-trivial FDs are key constraints. BCNF implies 3NF.

Decompositions should be **lossless-join** and ideally **dependency preserving**.

## Physical design

A DBMS stores data on external storage because the data is vast and must persist, and **I/O costs** dominate query time. Each record has a **record id (rid)**, so it can be fetched in one I/O. An **index** on a search key speeds up queries. In a **clustered** index the file is ordered like the index; an **unclustered** index may point to a different page for each matching record, so a range query through it can be worse than scanning the file. Physical design chooses file organizations and indexes to suit the most important queries.

Source: DBMS Lecture Notes.pdf, Unit III; DATABASE MANAGEMENT solution.pdf (Ramakrishnan and Gehrke, solutions manual, Chapter 8)
