# Interfacing with the 8086

## Data transfer and interfacing

Data transfer is either **synchronous**, usual when peripherals sit in the same computer as the CPU and share its timing, or **asynchronous**, where source and destination do not share a clock.

**Interfacing** connects memory (RAM, ROM, EPROM) and I/O devices to the 8086. An **address decoding circuit** selects the required chip or device. There are two schemes:

- **Memory-mapped I/O:** devices take memory addresses. The whole address space is usable, memory control signals are used, and arithmetic and logic can operate on the data directly.
- **I/O-mapped I/O:** special instructions (IN, OUT) and control signals are used. Data moves only between the accumulator and the port, and arithmetic cannot be done directly on it.

## 8255 Programmable Peripheral Interface (PPI)

The 8255 is a 40-pin chip with **24 programmable I/O lines** in three ports:
- **Group A:** Port A and Port C upper (PC7–PC4);
- **Group B:** Port B and Port C lower (PC3–PC0).

CS selects the chip, RD and WR mark reads and writes, and A1–A0 choose a port or the control register. The control word selects the mode:

- **Mode 0:** simple I/O, with no handshake or interrupts.
- **Mode 1:** I/O with **handshake**. Each port uses three Port C lines.
- **Mode 2:** **bidirectional** transfer on Port A, using five Port C lines.

## 8251 USART

The 8251 (Universal Synchronous Asynchronous Receiver Transmitter) handles serial communication. It converts parallel data from the CPU into a serial bit stream with start and stop bits on **TxD**, and turns serial bits received on **RxD** back into parallel bytes. C/D, RD and WR select the control register, the status register or the data buffer. Modem control signals support communication over telephone lines.

## A/D and D/A conversion

A **DAC** turns digital values into an analogue voltage. Resolution is (1/2ⁿ) × Vref, so an 8-bit DAC with 5 V gives 39.06 mV. **Settling time** is how long it takes to settle after a full-scale change. The **DAC 0800** is an 8-bit DAC from National Semiconductor, and the **ADC 0808/0809** are A/D converters.

## Timers, keyboards and interrupts

- **8253/8254 timer:** counters with six modes:
  - 0, event counter;
  - 1, one-shot;
  - 2, a series of one-clock-wide pulses;
  - 3, continuous square wave;
  - 4, software-triggered one-shot;
  - 5, hardware-triggered one-shot.
- **8279 keyboard/display controller:** runs keyboard and display operations at the same time.
  - Its keyboard section has eight return lines, **2-key lockout** or **N-key rollover**, and an **8 × 8 FIFO** that holds eight key codes.
  - Its display section has a **16 × 8 display RAM**, and four scan lines are shared with the keyboard.
  - It needs an internal clock of **100 kHz**, obtained through a prescaler.
- **8259A Programmable Interrupt Controller (PIC):** simplifies the interrupt interface of 8086 systems and is treated as a peripheral.

Case studies include traffic-light control, LED and LCD displays and an alarm controller.

Source: Case Studies Microprocessors and Microcontrollers.pptx (Unit 3)
