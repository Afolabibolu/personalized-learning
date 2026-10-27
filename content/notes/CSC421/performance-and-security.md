# System Performance and Security

## Performance measures

Performance is how effectively the OS manages resources, judged by:

- **Turnaround time:** in batch systems, from job submission to output returned.
- **Response time:** in interactive systems, from pressing Enter to the start of a reply.
- **System reaction time:** from pressing Enter to the first time slice of service.
- **Throughput:** jobs completed in a given time.
- **Workload, capacity** (maximum throughput) and **resource utilization** (percentage of time a resource is in use).

A **system performance monitor** supports selection evaluation (which vendor to buy from), performance projection (a system that does not yet exist) and performance monitoring.

## Evaluation techniques

- **Timing** (instructions per second) and **instruction mixes** for quick comparisons.
- **Kernel programs**, timed on different systems at installation.
- **Analytical models:** mathematical representations.
- **Benchmarks:** real programs run on real data. **LINPACK** measures floating-point work; **Whetstone** is a synthetic number-crunching benchmark; **Dhrystone** measures how well an architecture runs system programs; **Savage** checks trigonometric accuracy.
- **Simulation**, event-driven or script-driven.

## Bottlenecks and feedback

A **bottleneck** forms when a resource becomes **saturated** and competing processes interfere with one another. **Feedback loops** keep the system stable: a **negative feedback loop** slows the arrival of requests when the system is congested, and a **positive feedback loop** increases requests when it is underused.

## Security

Security means protecting resources such as CPU, memory, disk, programs and above all data from unauthorized use, from outside and inside. Measures include:

- **User interface security** and **operational security** (dividing duties among super users, programmers and operators).
- **Surveillance:** monitoring, auditing and authenticating users, for example by voice or thumbprint.
- **Threat monitoring** through a surveillance program, with **amplification** granting it extra rights.
- **Password protection** and **auditing**, with an audit log of important events.
- **Access control**, the key to internal security, and a **security kernel**.

**Survivability** is the ability to fulfil the system's mission in time despite attacks, failures or accidents.

## Levels of protection

- **Physical:** stolen backup tapes or root console access.
- **Human:** trustworthy users; threats include **phishing**, **dumpster diving** and **password cracking**.
- **Operating system:** runaway processes, memory-access and stack overflow violations.
- **Network:** protecting communications.

Regular **backup and recovery** protect against data loss.

Source: Operating System CSC 421 for DLC2.docx (Ibadan Distance Learning Series, CSC 421 Operating System II), Units 9 and 10
