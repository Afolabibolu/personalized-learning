# 8086 System Bus and Multiprocessing

## Pins and signals

The 8086 multiplexes address and data on the same pins to save pins:

- **AD15–AD0** carry address bits A15–A0 when **ALE** is 1, and data bits D15–D0 when ALE is 0. ALE high means the bus holds address information.
- **A19–A16/S6–S3** carry the top address bits, then status bits.
- **BHE** enables the high data byte, D15–D8, during a read or write.
- **LOCK**, activated by the LOCK prefix, locks peripherals off the system.
- The **MN/MX** pin selects minimum or maximum mode.

## Bus cycles

One clock period is a **T-state**, and a bus cycle has **four T-states**:

- **T1:** the address goes on the address/data bus. M/IO, ALE and DT/R say memory or I/O, latch the address and set the data direction.
- **T2:** the 8086 issues RD or WR and DEN, plus the data for a write. **READY** is sampled at the end of T2.
- **T3:** gives memory time to access the data. Data is sampled for reads, and written for writes.
- **T4:** all bus signals are deactivated, ready for the next cycle.

A **wait state (Tw)** is an extra clock period inserted between T2 and T3 when READY is 0. It lets slow memory and I/O respond.

**Setup time** is how long data must be valid and stable *before* the clock edge. **Hold time** is how long it must stay valid *after* the edge.

## Minimum and maximum mode

- **Minimum mode** (MN/MX = 1, tied to Vcc): the 8086 generates all its control signals itself. This suits small, single-processor systems.
- **Maximum mode** (MN/MX = 0, tied to ground): some control signals are generated externally by the **8288 bus controller**. It is used when a maths coprocessor or several processors are present.

## Multiprocessor configurations

Maximum mode supports three configurations:

1. **Coprocessor:** the 8087 maths coprocessor shares the bus with the 8086. 8087 instructions sit in the 8086 program and start with the bits **11011**. Both chips read instruction bytes into their own queues. The 8086's **WAIT** instruction checks the TEST input from the 8087. A coprocessor cannot take control of the bus; everything goes through the CPU.
2. **Closely coupled:** like a coprocessor, but the other processor *can* take control of the bus independently. Two 8086s cannot be closely coupled.
3. **Loosely coupled:** for medium to large systems. Modules share the system bus, memory and I/O, but each has its own clock and local memory, and any module can be bus master. A **bus controller** watches the bus-busy and bus-request signals, grants the bus to a master and synchronises the clocks.

**Advantages of multiprocessing:**
- higher throughput from more than one CPU;
- modular expansion, because bus masters can be added or removed;
- a failure in one module does not usually bring down the system;
- each master has a local bus, which allows more parallel processing.

Source: Case Studies Microprocessors and Microcontrollers.pptx (Unit 2)
