# Transactions, Concurrency Control and Recovery

## Transactions and ACID

A **transaction** is a collection of operations that performs a single logical function. It must have the **ACID** properties:

- **Atomicity:** all of its operations happen or none do; a transfer that debits A but fails before crediting B would leave the database inconsistent.
- **Consistency:** executed alone, it takes the database from one consistent state to another, for example the sum of A and B is the same before and after the transfer.
- **Isolation:** although transactions run concurrently, each appears to run alone; ensured by the **concurrency control** component.
- **Durability:** once a transaction completes successfully, its updates persist even if the system fails; ensured by the **recovery management** component.

## Transaction states

A transaction is **active** while executing, **partially committed** after its final statement, **committed** after successful completion, **failed** when normal execution can no longer proceed, and **aborted** after it has been rolled back. An aborted transaction can be **restarted** if there was no internal logical error, or **killed**.

## Schedules and serializability

A **schedule** is the chronological order of the instructions of concurrent transactions. In a **serial** schedule, each transaction's instructions run together. A schedule is **serializable** if it is equivalent to a serial schedule:

- **Conflict serializable** if it is conflict equivalent to a serial schedule. It is tested with a **precedence graph**, whose vertices are the transactions: the schedule is conflict serializable if and only if the graph is **acyclic**, and a topological sort gives the serial order.
- **View serializable** if it is view equivalent to a serial schedule.

## Locking

- A **shared (S)** lock lets a transaction read but not write an item, and many transactions can hold one at once.
- An **exclusive (X)** lock lets it read and write, and no other transaction may hold any lock on the item.

**Two-phase locking (2PL)** has a **growing phase**, in which a transaction obtains locks but releases none, and a **shrinking phase**, in which it releases locks but obtains none. It ensures conflict-serializable schedules, ordered by the transactions' **lock points**. 2PL does not prevent **deadlock**, two transactions each waiting for the other, which is resolved by rolling one back, and it allows cascading rollback. **Strict 2PL** holds exclusive locks until commit or abort; **rigorous 2PL** holds all locks until then.

## Timestamps

In the **timestamp-ordering protocol**, each transaction gets a timestamp on entry, and each item Q keeps a **W-timestamp(Q)** and **R-timestamp(Q)**, the largest timestamps of transactions that wrote and read it. Conflicting reads and writes run in timestamp order; a transaction that would read an overwritten value or write an obsolete one is rolled back.

## Recovery

Recovery keeps information on stable storage so the database can be restored after a failure. The two approaches are **log-based recovery**, which records each update in a log, and **shadow paging**, which keeps a shadow copy of the page table.

Source: DBMS Lecture Notes.pdf, Unit IV (CSC 472)
