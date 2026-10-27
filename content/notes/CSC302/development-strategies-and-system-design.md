# Development Strategies, Data Design and Architecture

## Development strategies

**In-house development** is often the first option considered, but it may not be feasible when:

- the company lacks the IT staff, skills or time;
- a suitable software package already exists at lower cost;
- the system is a standard business function, such as payroll, that a vendor already supports well.

The alternatives are:

- **buying a software package** (commercial off-the-shelf), with or without customisation;
- **outsourcing** development to an outside firm;
- using a **service provider** (software as a service, or an application service provider);
- having **end users** develop it themselves.

To evaluate packages, analysts check vendor claims by contacting other users, testing the package, and reviewing independent evaluations and benchmarks.

## Entity-relationship diagrams

An **ERD** models the data. It shows **entities** (people, places or things about which data is kept), their **attributes**, and the **relationships** between them. **Cardinality** describes how many instances of one entity relate to another:

- **one-to-one (1:1)**;
- **one-to-many (1:M)**: one team has many players;
- **many-to-many (M:N)**: students and courses. An M:N relationship is resolved by an **associative entity**, such as Registration between Student and Course.

## Normalization

**Normalization** removes redundancy and anomalies from table designs.

- **First normal form (1NF):** no repeating groups; every field holds a single value.
- **Second normal form (2NF):** in 1NF, and every non-key field depends on the **whole** primary key (no partial dependency).
- **Third normal form (3NF):** in 2NF, and no non-key field depends on another non-key field (no **transitive dependency**).

**Example:** in PRODUCT(Prodname, Salesperson, Compname, Vendor), Vendor depends on Compname, which depends on Prodname. That is a transitive dependency, so the table is split into PRODUCT(Prodname, Salesperson, Compname) and COMPONENT(Compname, Vendor).

## System architecture

- **File server architecture:** a server stores shared files, but the **client computers do all the processing**, so whole files travel over the network.
- **Client/server architecture:** the work is divided. The **server** processes requests and returns only the results, and the **client** handles the user interface. This reduces network traffic and improves performance.
- **Internet-based architecture:** the system runs through web browsers.
  - **Advantages:** access from anywhere, easy maintenance on a central server, and scalability.
  - **Disadvantages:** dependence on network availability, security risks, and slower response under heavy load.

## Top-down and bottom-up approaches

- **Top-down** starts from the whole system and decomposes it into subsystems and functions, as in a **functional decomposition diagram**. It gives a clear overall structure, but early decisions can be hard to change.
- **Bottom-up** starts from existing detailed components and combines them. It suits enhancing an existing system or reusing modules, but risks losing sight of the whole.

Source: general knowledge, following the CSC 302 past papers (2020/21 Questions 1 and 2, 2021/22 Questions 2 and 5, the 2020/21 test Question 3 and the 2024/25 paper)
