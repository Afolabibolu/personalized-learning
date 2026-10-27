# The 8259A Interrupt Controller and 8257 DMA Controller

## The 8259A Programmable Interrupt Controller

The **8259A** is a programmable interrupt controller for Intel's 8080A, 8085, 8086 and 8088. It can:

1. Handle **eight interrupt inputs**, like adding eight interrupt pins to the processor.
2. **Vector** an interrupt request anywhere in the memory map, with the eight interrupts spaced at intervals of four or eight locations. This removes a drawback of the 8085's own interrupts, which are vectored to fixed locations.
3. Resolve **eight levels of priority** in a variety of modes.
4. **Mask** each interrupt request individually.
5. Read the status of **pending** (IRR), **in-service** (ISR) and **masked** (IMR) interrupts.
6. Be **cascaded** in a master–slave configuration to handle up to **64** interrupts.

It comes in a 28-pin package. **CS** (chip select) enables it to accept command words; the **CAS** lines form a private bus for a multiple-8259A structure and identify a slave; and a dual-function pin tells whether the 8259A is a master or a slave. A priority resolver selects the highest-priority request in the IRR.

## Direct memory access

**Direct memory access (DMA)** is the **fastest** mode of data transfer: the device moves data directly to or from memory without the CPU. Through a DMA controller, the device asks the CPU to give up the buses with **HOLD**; the transfer starts only after the CPU answers with **HLDA**. When the transfer is complete, control of the bus is handed back to the CPU.

The two common **modes of operation** are:

- **Burst mode:** the DMA controller transfers a whole block before releasing the bus.
- **Cycle stealing mode:** it takes the bus only when the CPU is not using it.

## The 8257 DMA controller

The **8257** is Intel's **four-channel** DMA controller: four peripherals can request DMA transfers independently. It has an 8-bit internal data buffer, a read/write unit, a control unit, a **priority resolving unit** and a set of registers.

- Each channel has two 16-bit registers: a **DMA address register** and a **terminal count register**. The top two bits of the terminal count register choose the cycle: verify (00), **write** (01, data written into memory) or **read** (10).
- Two registers are common to all channels: the **mode set register** and the **status register**.
- The **mode set register** enables channels individually and sets the modes of operation, such as **rotating priority** and **TC STOP**, which disables a channel when its terminal count is reached.

With an 8086, the 8257 requests the bus with HOLD in minimum mode, or the RQ/GT pin in maximum mode. The control signals for DMA are therefore **HOLD**, **HLDA**, and each channel's **DRQ** (request) and **DACK** (acknowledge).

Source: CSC 412 MICROPROCESSOR INTERFACING.pdf (CSC 412 course material, Adebola K. Ojo), Study Sessions 9 and 10; My CSC 412 Note-7.pdf (DMA modes)
