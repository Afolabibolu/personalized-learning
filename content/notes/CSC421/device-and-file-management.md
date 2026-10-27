# Device and File Management

## Device management

The device manager tracks each device's status, decides by policy which process gets it and for how long, allocates it, and deallocates it at the process and job level. Devices are:

- **Dedicated:** assigned to one job for its whole run, such as a tape drive or plotter; often wasteful.
- **Shared:** used by several processes, such as direct access storage devices (DASD).
- **Virtual:** dedicated devices made shareable, such as a printer through **spooling** to a disk.

**Sequential access media** (magnetic tape) store records one after another, individually with inter-record gaps or in **blocks** with inter-block gaps; blocking means fewer I/O operations and less wasted tape. **Direct access** devices reach any location directly. Access time on a disk is **seek time** (moving the head to the track; not on fixed-head devices) plus **search time** (rotational delay) plus **transfer time**. A magnetic disk spins at constant angular velocity; an optical disc has one spiral track.

The I/O subsystem has **channels**, **control units** and devices. Completion is detected by **polling** or more efficiently by **interrupts**. **Direct memory access (DMA)** lets a control unit transfer data to main memory without the CPU, and **buffers** smooth the speed difference between devices and CPU. The **I/O traffic controller**, **I/O scheduler** and **I/O device handler** manage requests.

## Disk scheduling

The aim is to minimize arm movement and response time:

- **FCFS:** fair, for light loads, but much arm movement.
- **SSTF:** the request on the nearest track next (moderate loads).
- **SCAN:** the arm serves requests in one direction to the end, then reverses; **LOOK** turns at the last request instead of the edge; **N-step SCAN** holds new requests for the next sweep.
- **C-SCAN:** serves requests in one direction only, then returns; **C-LOOK** is its LOOK version.

## File management

A file is a named collection of records, and records consist of fields. File characteristics include **volatility** and **activity**. Each volume has a descriptor and a **master file directory**. File organization may be **sequential**, **direct** (records located by address, often with hashing) or **indexed sequential**. Records are **fixed length** or **variable length**.

Physical storage is:

- **Contiguous:** records one after another; simple, but files cannot grow easily and external fragmentation needs compaction.
- **Chained (linked):** each block points to the next; a null pointer marks the end.
- **Indexed:** each file has an index block listing its sectors; supports sequential and direct access.

An **access control matrix** lists users against files with rights such as read, write, execute and delete.

Source: Operating System CSC 421 for DLC2.docx (Ibadan Distance Learning Series, CSC 421 Operating System II), Units 7 and 8
