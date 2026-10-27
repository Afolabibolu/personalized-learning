# The Intel 8051 Microcontroller

## Features

The **8051** is Intel's **8-bit** microcontroller, with:

- **4 KB** of on-chip program ROM, within a **64 KB** program address space;
- **four register banks** (Bank 0–3), each with R0–R7;
- **32 I/O lines** in four 8-bit ports, P0–P3;
- **two 16-bit timer/counters** and a **UART** serial port.

It is a subset of the **8052**; the **8031** is a ROM-less 8051, which loses two ports to external ROM.

## Ports and pins

- **P0:** I/O, and the multiplexed low address/data bus for external memory (address when **ALE** = 1, data when ALE = 0).
- **P1:** a simple bidirectional I/O port.
- **P2:** I/O, and the high address byte for external memory.
- **P3:** I/O, with serial, interrupt, timer and read/write functions.
- **EA:** 0 fetches code only from external ROM; 1 uses internal and external ROM.

## Registers and addressing

The PC points to the next instruction; the 8-bit **SP** points to the stack top; **DPTR** is a 16-bit data pointer. The **special function registers** include A, B, PSW, SP, DPTR, P0–P3, TMOD, TCON, SCON, SBUF, IE and IP. Addressing modes are immediate (#data), register, direct, register indirect (@R0 or @R1 only), relative, absolute and long, and indexed.

## TMOD and TCON

**TMOD** configures Timer 0 (lower nibble) and Timer 1 (upper nibble):

- **GATE:** when set, the timer runs only if the INTx pin is high and TRx is set.
- **C/T:** 1 = counter of external pulses; 0 = timer of the internal clock.
- **M1, M0:** mode 0 = 13-bit, **mode 1 = 16-bit**, **mode 2 = 8-bit auto-reload**.

**TCON** holds **TR** (set by the program to start a timer) and **TF** (set when TH–TL rolls over from FFFFH to 0000H; it can trigger an interrupt).

## Timer mode 1 and delays

To use Timer 0 in mode 1: MOV TMOD,#01; load TH0 and TL0; clear TF0; SETB TR0; wait until TF0 = 1 (JNB TF0); CLR TR0; clear TF0. Mode 1 does not reload, so TH and TL are reloaded each time.

With an **11.0592 MHz** crystal, one machine cycle is **1.085 µs**, and the delay for a starting value YYXX is (FFFF − YYXX + 1) × 1.085 µs. For a 50 Hz square wave, each half period is 10 ms = 9216 cycles, so TH–TL = 65536 − 9216 = **DC00H**.

## Serial communication

**Synchronous** transfer sends a block at a time; **asynchronous** sends one byte at a time, framed by a **start bit (0)** and a **stop bit (1)**. **Baud rate** is signal changes per second.

- **SCON** controls the serial port: mode, reception enable (REN) and the 9th bit in modes 2 and 3.
- **SBUF** holds the byte sent on **TxD** or received on **RxD**.

Source: CSC 412 MICROPROCESSOR INTERFACING.pdf (Study Session 12); Case Studies Microprocessors and Microcontrollers.pptx (Units 4 and 5)
