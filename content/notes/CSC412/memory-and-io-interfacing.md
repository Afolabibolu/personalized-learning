# Interfacing Memory and I/O with the 8085

## Interfacing memory chips

The 8085's memory address space runs from **0000H to FFFFH** (64 KB). A memory chip is interfaced by connecting its address lines to the low address lines of the 8085, its data lines to the data bus, and the remaining high address lines to an **address decoder**, which enables the chip only for its assigned range. Decoders are built from **NAND gates** or a **74LS138** decoder. The course works examples such as interfacing an **IC 2764** (8K × 8 EPROM), a **6264** (8K × 8 RAM) and two **6116** RAM chips with the 74LS138.

## Two schemes for I/O

Input and output devices can be interfaced in two ways:

- **Peripheral-mapped (I/O-mapped) I/O:** I/O devices are treated differently from memory and have their own 8-bit addresses, used with the IN and OUT instructions. Up to **256 input** and **256 output** devices (2⁸ each) can be interfaced. The IO/M signal tells I/O operations from memory operations.
- **Memory-mapped I/O:** I/O devices are treated as memory locations and share the 16-bit memory address space, so any memory instruction can access them. For example, a DIP switch read through a 74LS244 buffer is enabled when its decoded address and MEMR are both active.

## The 8255 Programmable Peripheral Interface

The **8255A** is a general-purpose programmable I/O device for Intel microprocessors, configured by software to meet different I/O needs. It has three 8-bit ports:

- **Port A:** an 8-bit output latch/buffer and an 8-bit input buffer.
- **Port B:** the same as port A.
- **Port C:** can be used as one 8-bit port or split into **Port C upper (PC7–PC4)** and **Port C lower (PC3–PC0)**, and can supply handshake signals for ports A and B.

The ports form two groups:

- **Group A:** port A and port C upper.
- **Group B:** port B and port C lower.

## 8255 modes

The groups can be programmed in three modes, selected through the **control word register**, which can only be written, not read:

- **Mode 0, basic input/output:** each port (A, B, C upper and C lower) is a simple input or output port.
- **Mode 1, strobed input/output:** port A or B transfers 8 bits with **handshaking** and interrupt control signals from port C.
- **Mode 2, bidirectional bus:** port A only works as a bidirectional bus, with five port C lines used for handshaking.

Pins such as **CS** (chip select), **RD**, **WR**, the address lines A0 and A1 (which select a port or the control register) and **RESET** connect the 8255 to the processor.

Source: CSC 412 MICROPROCESSOR INTERFACING.pdf (CSC 412 course material, Adebola K. Ojo), Study Sessions 7 and 8
