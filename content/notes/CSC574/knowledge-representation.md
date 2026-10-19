# Knowledge Representation and Reasoning

## What the topic is

Knowledge representation (KR) is a way to structure information so that machines can reason about it. It covers symbols, logic, rules, networks, frames and ontologies, and it lets AI make decisions, solve problems and learn. An agent can act accurately on an input only when it has knowledge about that input.

## Subtopics

**What must be represented.** Objects, events, performance, facts, meta-knowledge and the knowledge base.

**Types of knowledge.**
- **Declarative:** concepts, facts and objects, expressed in declarative sentences.
- **Structural:** relationships between concepts and objects.
- **Procedural:** how to do something (rules, strategies, procedures).
- **Meta knowledge:** knowledge about other types of knowledge.
- **Heuristic:** expert knowledge in a field.

**The AI knowledge cycle.** Perception retrieves data from the environment. Learning learns from it. Knowledge representation and reasoning, the main component, shows human-like intelligence. Planning and execution depend on that analysis: planning finds the sequence of actions that reaches a goal, and execution carries it out.

**Logic.** Propositional logic uses simple declarative statements joined by AND, OR, NOT and IMPLIES, with truth tables for inference (for example, Rain → Wet). First-order logic adds predicates and quantifiers, as in ∀x (Human(x) → Mortal(x)). Logic is precise, but can be hard to work with and inefficient for inference.

**Rule-based reasoning.** IF-THEN rules derive conclusions from facts. Forward chaining is data-driven and backward chaining is goal-driven. Example: IF EarthquakeDetected THEN SendAlert.

**Semantic networks.** A graph representation: nodes are concepts and edges are relationships, supporting inheritance and association. Examples: Dog is_a Mammal; Dog has Tail. They are natural and easy to understand. But they take more computational time at runtime, have no equivalent quantifiers and depend on whoever built them.

**Ontologies and frames.** An ontology defines the concepts, relationships and properties in a domain (Product hasCategory Electronics). A frame is a record-like structure of slots and values describing an entity.

**Requirements of a good KR system.** Representational accuracy, inferential adequacy, inferential efficiency and acquisitional efficiency.

## Key terms

- **Inheritance (is_a):** a concept takes on the properties of its parent.
- **Knowledge base:** the stored facts and rules a system reasons over.

## Exam-style point

Past papers ask for a semantic graph from a narrative, such as diseases, drugs, genes and compounds. Draw each concept as a node and label every edge with its relationship ("treats", "causes", "part_of"). Then read sentences off the graph: "Drug treats Disease."

Source: Lecture 3; Knowledge-Representation-in-AI.pdf
