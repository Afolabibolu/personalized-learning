# IT Projects, Data-Centre Security and Services

## Managing IT projects

A **project proposal** states the problem, objectives, scope, approach, schedule, resources, cost and expected benefits, so management can approve it. **Project costing** estimates hardware, software, personnel, training, maintenance and contingency costs, often as a budget.

- **Milestones** are key points marking the completion of major stages.
- **Deliverables** are the tangible outputs, such as reports, designs and working software.

Scheduling tools include:

- **bar charts** and **Gantt charts**, which show tasks as bars against time;
- **activity networks** (PERT/CPM), which show task dependencies and the **critical path**, the longest chain of tasks that sets the project's length.

Projects are kept on track by **monitoring and reviews** against the plan. **Report writing** gives management progress, problems and recommendations. **Risk management** identifies, analyses, plans responses to and monitors risks.

## Securing devices and data

- **An employee's official laptop:** theft or loss and data leakage. Use full-disk encryption, strong passwords and remote wipe.
- **Computers and printers in an unsupervised laboratory:** tampering, theft and unauthorized use. Use locks, CCTV, user logins and access control.
- **Client data stored with a data-centre provider:** breaches and loss of control. Use encryption, access controls, audits and a clear contract.

**RAID** (redundant array of independent disks) stores data across several disks, by mirroring or parity, so a single disk failure does not lose data. It protects availability, but it is not a substitute for backups.

**AES-256** is the Advanced Encryption Standard with a **256-bit key**. It is a symmetric block cipher that encrypts 128-bit blocks in 14 rounds, is adopted by the US government, and is considered practically unbreakable by brute force.

**Password salting** adds a random value (the **salt**) to each password before hashing it. Identical passwords then give different hashes, which defeats precomputed rainbow-table attacks.

**DNS cache poisoning** (DNS spoofing) inserts false records into a DNS resolver's cache, redirecting users to malicious sites. It is prevented with **DNSSEC** (digitally signed records), randomized query IDs and source ports, keeping DNS software patched, and limiting recursive queries.

## Buying services

A **service-level agreement (SLA)** is the contract with an outside supplier of support services. It defines the services, performance levels (such as uptime and response times), responsibilities and penalties.

**Cloud service models:**

- **IaaS (Infrastructure as a Service):** virtual servers, storage and networks that the customer manages, such as Amazon EC2.
- **PaaS (Platform as a Service):** a ready platform to build and run applications without managing the infrastructure, such as Google App Engine.
- **SaaS (Software as a Service):** complete applications used over the Internet, such as Gmail.

**Customer dissatisfaction** often leads to revenue loss: an IT system that fails users' expectations drives customers to competitors.

Source: general knowledge, following the CSC 301 course outline and past papers (the course outline's proposal writing, costing, milestones, scheduling and risk management, and the 2023/24 paper, Questions 3 and 4); the course note covers security and backup only briefly
