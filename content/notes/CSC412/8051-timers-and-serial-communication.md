# 8051 Timers and Serial Communication

## TMOD and TCON

The 8051's two timer/counters, Timer 0 (TH0–TL0) and Timer 1 (TH1–TL1), are configured with **TMOD**, which is not bit-addressable. Its upper nibble is for Timer 1 and its lower nibble for Timer 0:

- **GATE:** when set, the timer runs only if the INTx pin is high and TRx is set. When clear, TRx alone starts it.
- **C/T:** set means **counter**, counting pulses on the Tx pin. Clear means **timer**, counting the internal clock.
- **M1, M0:** the mode. **Mode 1** is a 16-bit timer, with a maximum count of FFFFH. **Mode 2** is an 8-bit timer with **auto-reload**. Mode 0 is 13-bit, with a maximum of 1FFFH.

**TCON** holds TF1, TR1, TF0 and TR0 in its upper nibble, for the timers, and the interrupt bits IE1, IT1, IE0 and IT0 in its lower nibble.
- **TR** is set by the programmer to start or stop a timer.
- **TF** works like a carry. It becomes 1 when TH–TL rolls over from FFFFH to 0000H. If interrupts are enabled, TF = 1 triggers the interrupt service routine.

## Programming Timer 0 in mode 1

1. Load TMOD, for example MOV TMOD,#01 for Timer 0, mode 1.
2. Load the starting value into TH0 and TL0.
3. Clear TF0.
4. Start the timer with SETB TR0.
5. The timer counts up once per machine cycle.
6. When TH0–TL0 rolls over from FFFFH to 0000H, the 8051 sets TF0 = 1.
7. Keep checking TF0, for example with JNB TF0.
8. Stop the timer with CLR TR0.
9. Clear TF0 for the next round.

Mode 1 does not reload automatically, so TH and TL must be reloaded every time.

## Delay calculation

With an **11.0592 MHz** crystal, one machine cycle takes **1.085 µs**. For starting values YYXX in TH and TL:

delay = (FFFF − YYXX + 1) × 1.085 µs, or (65536 − NNNNN) × 1.085 µs, where NNNNN is YYXX in decimal.

**Example.** To make a 50 Hz square wave on P2.3:
- the period is 1/50 = 20 ms, so each half is 10 ms;
- 10 ms / 1.085 µs = 9216;
- 65536 − 9216 = 56320 = **DC00H**;
- so load TH1 = DCH and TL1 = 00H.

## Serial communication

Serial data uses two methods. **Synchronous** sends a block at a time. **Asynchronous** sends one byte at a time. In asynchronous framing, the **start bit is always 0** and the **stop bit is 1**. Rates are given in bits per second; **baud rate** means signal changes per second.

The 8051 uses two registers:
- **SCON** controls the serial port: the mode, reception enable (REN), multiprocessor mode, and the 9th data bit in modes 2 and 3.
- **SBUF** is an 8-bit register for serial data. A byte to send on **TxD** is placed in SBUF, and a byte received on **RxD** arrives in SBUF.

Source: Case Studies Microprocessors and Microcontrollers.pptx (Unit 5)
