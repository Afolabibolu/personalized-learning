# Circuit and Packet Switching

## Packet switching

**Packet switching** breaks data into small pieces of variable length, called **packets**, each holding a payload and control information (a header with source and destination). No resources are reserved in advance. Packets are reassembled at the destination. Packet switching was designed because circuit-switched networks were not effective for small messages.

It uses **store and forward**: each hop first stores the whole packet, then forwards it. This allows a damaged packet to be discarded at a hop, and lets packets choose different paths around congestion.

**Delays in packet switching:**

1. **Transmission delay:** time to put the packet onto the link; depends on packet size and bandwidth.
2. **Propagation delay:** time to travel the link; depends on distance and signal speed.
3. **Processing delay:** time a router takes to process the packet.
4. **Queuing delay:** time waiting in a queue before transmission.

They are reduced by better routing algorithms, more bandwidth and quality-of-service (QoS) priorities.

**Advantages over circuit switching:**

- more efficient use of bandwidth;
- more reliable, since lost packets can be detected;
- more fault tolerant, since packets can avoid a failed link;
- cheaper to implement.

**Disadvantages:** packets may arrive out of order and need sequence numbers, nodes are more complex, and rerouting adds delay.

## Modes of packet switching

- **Virtual circuit (connection-oriented):** a logical path is set up first, and all packets follow it and arrive in order. It has three phases: setup, data transfer and teardown. During **setup**, each switch adds an entry to its switching table, mapping incoming port and **VCI (virtual circuit identifier)** to outgoing port and VCI. Afterwards packets carry only the local VCI. Used by X.25, Frame Relay, ATM and MPLS.
- **Datagram (connectionless):** each packet carries full addressing information and is routed independently, so packets may take different routes and arrive out of order. There is no setup or teardown, and delivery is not guaranteed, so end systems must add reliability.

## Circuit switching

**Circuit switching** obtains a physical path dedicated to one connection for its whole duration, as in ordinary telephone calls. Bandwidth and data rate are fixed, and it is connection-oriented. It has three phases:

1. **connection establishment** (call setup);
2. **data transfer**;
3. **connection release** (teardown).

Its delay is minimal once the circuit is set up, but the circuit is wasted when idle, so it is inefficient for bursty data traffic.

| Circuit switching | Packet switching |
| --- | --- |
| Dedicated physical path | No dedicated path |
| Same route for all data, in order | Packets may take different routes |
| No store and forward | Store and forward |
| Charged by time | Charged by packets |

Source: CSC322-Combined.pdf (CSC 322 lecture notes), Lecture 3 (packet switching, delays, virtual-circuit and datagram modes, circuit switching and the comparison); the VCI switching-table setup is general knowledge, following the CSC 322 past papers (2021/22 and 2024/25 papers)
