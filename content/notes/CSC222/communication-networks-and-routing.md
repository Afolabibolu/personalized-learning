# Communication Networks: Switching, Delay and Routing

## Switches

A network with a dedicated link between every pair of computers needs a **quadratic** number of links (about N²), which is too expensive and spans huge distances. The key to practical networks is the **switch**, a device with multiple ports that lets many communications share each link. The communicating computers are **end points**; switches and links form the network infrastructure, and together they make the **network topology** of nodes and links. Switches **multiplex and demultiplex** data frames from different sessions, which breaks into three problems:

1. **Forwarding**: when a frame arrives, determine the correct outgoing link and when to send it.
2. **Routing**: determine the topology, collaboratively and in the background, to build the forwarding data structures.
3. **Resource allocation**: share link access and memory among the communications in progress.

## Circuit and packet switching

**Circuit switching** works in **three phases**: a **setup** phase configures state at each switch along the path, a **data transfer** phase carries the communication, and a **teardown** phase cleans up afterwards. It is commonly implemented with **time-division multiplexing (TDM)**: a link of capacity C is divided into N channels of rate R = C/N, each frame forwarded by its time slot. Other methods are wavelength, frequency and code division multiplexing (WDM, FDM, CDMA).

**Packet switching**, used by the Internet, **does not provide the illusion of a dedicated link** to any pair of end points, but: it **does not waste link capacity**, since a switch can send any waiting packet; it **needs no setup or teardown**, so small transfers have no overhead; and it gives **variable data rates** as needed. Switches absorb bursts of traffic with **queues**.

## Delay

Network latency (delay) has four sources: **propagation delay**, the time for a signal to travel the link, set by distance and the speed of light, and summed over links; **processing delay** in a switch; **transmission delay**, the time to send a packet of S bits on a link of rate R, which is **S/R**; and **queueing delay**, while a packet waits in a switch's queue.

## Routing

Packets are delivered in three parts: **addressing** (naming the nodes), **forwarding** (a switch sending a packet on the right link), and **routing** (the background process by which switches **construct their routing tables**). The pair of a destination and outgoing link is a **route**. Routing is hard because information is **distributed**, paths must be **efficient** (links have non-negative costs), and links and nodes **fail**. Most routing protocols have three components: **determining neighbours**, **sending advertisements** periodically, and **integrating advertisements** to compute routes. The two families are **distance-vector** and **link-state** protocols.

Source: CSC 222 Digital Communication lecture slides (Dr Adeniji Oluwashola David), Lecture 5 (Network Routing I: Without Any Failures) and Lecture 6 (Communication Networks: Sharing and Switches)
