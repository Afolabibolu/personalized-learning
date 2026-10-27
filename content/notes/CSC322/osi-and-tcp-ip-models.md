# The OSI and TCP/IP Models

The **OSI (Open Systems Interconnection)** model was developed by **ISO** (1984). It has seven layers that work together to carry data between users. It is a reference model; the Internet uses the TCP/IP model.

## The seven layers

1. **Physical:** transmits individual **bits**; handles bit synchronisation, bit rate, physical topology and transmission mode. Devices: hub, repeater, modem, cables.
2. **Data link:** node-to-node delivery of **frames** using MAC addresses, with sublayers LLC and MAC. Functions: framing, physical addressing, error control, flow control and access control. Devices: switch, bridge.
3. **Network:** delivers **packets** between hosts on different networks; does **routing** and **logical (IP) addressing**. Device: router.
4. **Transport:** end-to-end delivery of **segments**; segmentation and reassembly, port (service point) addressing, flow and error control. It offers connection-oriented and connectionless service.
5. **Session:** establishes, maintains and ends sessions; synchronisation checkpoints; dialog control.
6. **Presentation:** the translation layer; translation (ASCII to EBCDIC), encryption and compression. Examples: JPEG, MPEG, GIF.
7. **Application:** the window for applications: remote login, file transfer (FTAM), mail and directory services. Example: SMTP.

Layers 1 to 3 are the lower (hardware) layers. In TCP/IP, layers 5 to 7 are merged into one application layer.

## TCP/IP model

TCP/IP has four layers: **network access (link), Internet, transport and application**. Its **IP** layer gives unreliable packet delivery. **TCP** provides a reliable stream with flow control, while **UDP** is a simpler connectionless protocol for video streaming or voice.

## Framing and bit stuffing

The data link layer marks frame boundaries with a **flag**, 01111110. So that data never imitates the flag, the sender **stuffs a 0 after every five consecutive 1s** in the payload, and the receiver removes it.

## Error detection

- A **single-bit error** changes one bit of a data unit; a **burst error** changes two or more bits.
- **Parity check:** a parity bit makes the number of 1s even (or odd); it detects single-bit errors.
- **Cyclic redundancy check (CRC):** the sender divides the data by an agreed generator and appends the remainder; the receiver repeats the division, and a non-zero remainder means an error. It detects burst errors well.

Source: CSC322-Combined.pdf (CSC 322 lecture notes), Lecture 2 (OSI model and its layers; TCP and UDP); the four TCP/IP layers, bit stuffing and error detection are general knowledge, following the CSC 322 past papers (2020/21, 2021/22 and 2023/24 papers)
