# Software Validation and Testing

## Verification and validation

**Software validation**, or more generally **verification and validation (V & V)**, is intended to show that a system both **conforms to its specification** and **meets the expectations of the customer**. Program testing, running the system with simulated test data, is the main technique, but validation also involves inspections and reviews at each stage. Systems are not tested as one monolithic unit: in a plan-driven process there are three stages:

1. **Component testing**: components are tested independently by their developers.
2. **System testing**: components are integrated into a complete system and tested for errors from unanticipated interactions and interface problems.
3. **Acceptance testing**: the final stage before operational use, testing with **data supplied by the customer** rather than simulated data.

## The goals of testing

Testing is intended to show that a program does what it is intended to do and to **discover defects** before it is put into use. It has two distinct goals:

1. To demonstrate to the developer and customer that the software **meets its requirements**: for custom software, at least one test for every requirement. This leads to **validation testing**, using test cases that reflect expected use.
2. To discover situations where the software behaves incorrectly or does not conform to its specification. This leads to **defect testing**, which roots out undesirable behaviour.

## Development testing

**Development testing** is all the testing carried out by the team developing the system, usually by the programmer. It has three levels of granularity:

1. **Unit testing**: individual program units or object classes, focusing on the functionality of objects or methods.
2. **Component testing**: several units integrated into composite components, focusing on component interfaces.
3. **System testing**: some or all components integrated and tested as a whole, focusing on component interactions.

Development testing is mainly **defect testing** and is interleaved with **debugging**, locating and fixing problems.

## User testing

In **user (customer) testing**, users give input and advice on testing. Its three types are:

1. **Alpha testing**: users work with the development team to test the software **at the developer's site**.
2. **Beta testing**: a release is made available to users to **experiment and report problems**.
3. **Acceptance testing**: customers test the system to decide whether it is ready to be **accepted and deployed**.

Acceptance testing has six stages: **define acceptance criteria**, **plan acceptance testing**, **derive acceptance tests**, **run acceptance tests**, **negotiate test results**, and **reject or accept the system**.

Source: SEN 201 Lecture Notes.docx, Software Validation and Software Testing
