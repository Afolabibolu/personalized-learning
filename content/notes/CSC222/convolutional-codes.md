# Convolutional Codes and Viterbi Decoding

## Where they are used

Space probes from Voyager onwards, and Cassini, Mars Exploration Rover and others, use **convolutional codes** decoded by **Viterbi decoding**; Cassini combined a convolutional code with a Reed-Solomon block code, a **concatenated code**. Convolutional codes and Viterbi decoding are also used in many terrestrial applications: **most mobile phones**, digital video broadcasting, and Wi-Fi.

## How they differ from block codes

1. Convolutional codes **act on message bits streaming into the encoder**, rather than on fixed blocks.
2. They **transmit only the parity bits**, not the data bits plus parity bits, so they are **non-systematic** codes.

Error correction comes from each message bit affecting **many different parity bits**. The **code rate** tells how many parity bits are sent per message bit; a rate-1/r code sends r parity bits per message bit.

## An example

A simple code has two parity equations (modulo 2):

p₀[n] = x[n] + x[n − 1] + x[n − 2]
p₁[n] = x[n] + x[n − 2]

The encoder moves through the message with a **sliding window**: for n = 2 it uses x[0] to x[2], for n = 3, x[1] to x[3]. The **width of this window is the constraint length K**; here **K = 3**. The parity sequences are interleaved and sent: p₀[0]p₁[0]p₀[1]p₁[1]…. The code rate is 1/2. A larger K gives stronger error correction but makes decoding more complex, which is the **trade-off between constraint length and decoding complexity**.

## Shift registers, state machines and trellises

The encoder is a **shift register**: the values held in the register, x[n − 1] and x[n − 2], are the encoder's **state**, so there are **2^(K−1) states**, four for K = 3 (00, 01, 10, 11). In the **state-machine** view, each input bit moves the encoder to a new state, and each edge is labelled with input/parity bits, such as 1/11. The **trellis** spreads the state machine out over time, so it records the sequence of states the encoder has passed through; this is what decoding needs.

## Decoding

**Viterbi decoding** finds the most likely transmitted message by tracking, through the trellis, the path whose parity bits differ least from the received bits. The **free distance** of a convolutional code is the smallest Hamming distance between the parity streams of any two different messages; it sets how many errors the code can correct, as the minimum distance does for block codes.

Source: CSC 222 Digital Communication lecture slides (Dr Adeniji Oluwashola David), slides 6 and 7 (Convolutional Coding; Viterbi Decoding) and Chapters 7 and 8 of the notes filed with the course
