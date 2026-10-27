# Managing Systems Projects

## Project management

A successful project must be completed **on time, within budget**, and deliver a quality product that satisfies users and meets requirements. A **project manager** (or project leader) leads it, often helped by a **project coordinator**. Project managers perform four main tasks:

1. project planning;
2. project scheduling;
3. project monitoring and controlling;
4. project reporting.

## Planning and estimating

**Identifying tasks:** a project twice as large will be much more than twice as complex. Multiple interactions cause misunderstandings and delay, and **project creep** adds work. **Brooks's Law** says that adding people to a late project makes it later.

Time is measured in **person-days**, but in most analysis tasks time and people are not interchangeable.

Each task's duration is estimated from three cases: **best case (B)**, **probable case (P)** and **worst case (W)**. The weighted expected duration is:

**Expected duration = (B + 4P + W) ÷ 6**

**Example:** with B = 30, P = 35 and W = 45 days, the expected duration is (30 + 140 + 45) ÷ 6 ≈ **35.8 days**.


## Gantt and PERT/CPM charts

A **project schedule** is a specific timetable.

- A **Gantt chart** shows tasks as horizontal bars against a calendar, giving a rapid overview of timing, duration and progress.
- A **PERT/CPM chart** (Program Evaluation Review Technique / Critical Path Method) shows tasks as boxes holding the task name, ID, duration, and start and finish days, linked by arrows.

The two are not mutually exclusive; PERT/CPM is often more helpful for control.

Task patterns are **dependent tasks** (one after another), **multiple successor tasks** and **multiple predecessor tasks**.

- The **critical path** is the longest sequence of dependent tasks. It sets the project's total duration, and any delay on it delays the whole project.
- **Slack (float)** is how long a task can be delayed without delaying the project. Tasks on the critical path have zero slack.

## Risk, monitoring and reporting

Every IT project involves **risks**. The steps of risk management are:

1. develop a risk management plan;
2. identify the risks;
3. analyse them, qualitatively and quantitatively;
4. create a risk response plan;
5. monitor the risks.

The project manager monitors tasks against the plan with **structured walkthroughs** (design, code and testing reviews), and reports through status meetings and reports.

**Software change control** handles change requests in four steps: complete a request form, take initial action, analyse the impact and decide the outcome.

Cost overruns come from unrealistic estimates, a poor TCO forecast, weak monitoring, schedule delays and human resource factors. When problems occur, the manager may trim less critical requirements, add resources, or move a flexible deadline.

Source: CSC 302 Lecture 1.pdf and Lecture 2.pdf (lecture slides from Shelly Cashman, Systems Analysis and Design, 9th ed.), Chapter 3 (project management, planning, estimating, Gantt and PERT/CPM charts, risk management, monitoring, reporting, change control, keys to success); critical path and slack follow the 2020/21 and 2021/22 papers
