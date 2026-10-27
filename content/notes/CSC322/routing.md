# Routing

## Routers and routing tables

**Routing** is the process of selecting the path along which data travels from source to destination. It is performed by a **router**, which works at the network layer (layer 3) of OSI and the Internet layer of TCP/IP. A router forwards each packet using the information in the packet header and its **forwarding (routing) table**. The **routing algorithm** is the software that initialises and maintains the table and decides the optimal path.

## Routing metrics

**Metrics** are the network variables used to judge the best route:

- **Hop count:** the number of routers a packet passes through; the fewest hops wins.
- **Delay:** the time to process, queue and transmit a datagram; the lowest delay wins.
- **Bandwidth:** the link's capacity in bits per second; higher is preferred.
- **Load:** how busy a router or link is.
- **Reliability:** a rating, often set by the administrator, of how often a link fails.

## Types of routing

**Static (non-adaptive) routing:** the administrator adds routes to the table manually, and decisions ignore the current network condition.

- **Advantages:** no CPU overhead (cheaper routers), no bandwidth used between routers, and security, since only the administrator controls the routes.
- **Disadvantages:** adding every route by hand is very hard on a large network, and the administrator must know the topology well.

**Default routing:** the router sends all packets to one next-hop device. It suits networks with a single exit point. A specific route in the table is always preferred over the default.

**Dynamic (adaptive) routing:** routers discover routes and update their tables automatically as the network changes, using protocols such as **RIP** and **OSPF**. All routers must run the same protocol and broadcast changes.

- **Advantages:** easier to configure, and better at choosing routes as conditions change.
- **Disadvantages:** costs more CPU and bandwidth, and is less secure.

## Distance-vector routing

Each router keeps a table (vector) of the best known distance and next hop to every destination.

- **Initialisation:** each router knows only its directly connected neighbours.
- **Sharing:** routers send their tables to their neighbours.
- **Updating:** a router updates its table whenever a neighbour's distance plus the link cost is shorter.

Tables are sent at regular intervals (**periodic update**, every 30 seconds in RIP) or whenever something changes (**triggered update**). A failed node's routes are spread slowly, which can cause the **count-to-infinity** problem.

## Link-state routing

Each router floods information about its links to all routers, so every router builds a map of the whole network. It then runs **Dijkstra's algorithm** to find the least-cost path to every destination, adding the nearest unvisited node at each step. OSPF uses link-state routing.

Source: CSC322-Combined.pdf (CSC 322 lecture notes), Lecture 4 (routing, metrics, static, default and dynamic routing); distance-vector and link-state routing are general knowledge, following the CSC 322 past papers (2021/22 and 2024/25 papers)
