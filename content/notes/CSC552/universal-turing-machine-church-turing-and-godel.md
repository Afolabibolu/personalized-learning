# Universal Turing Machine, Church–Turing Thesis and Gödel

## The universal Turing machine

An ordinary Turing machine must be built anew for every computation. The **universal Turing machine (UTM)** takes the description of a machine M together with an input, simulates M on that input and returns the result. To simulate a machine, it keeps three pieces of information: a basic description of the machine, the contents of its tape and its internal state.

Differences in the course table:
- A TM is a formal model of a computer with a fixed program; a UTM is a programmable TM.
- A TM does not minimise space complexity; a UTM does.

## The Church–Turing thesis

In 1936 Alonzo Church created the λ-calculus, which defines the Church numerals, and Alan Turing created his machines. Church's mechanical method M had to meet four conditions:

1. It has a finite number of instructions.
2. It produces output after a finite number of steps.
3. It is not imaginary; it can be made in real life.
4. It needs no complex understanding.

The thesis says: "Every computation that can be carried out in the real world can be effectively performed by a Turing machine." In short, the intuitive notion of an algorithm equals a Turing machine. The thesis cannot be proved.

## Algorithms and Hilbert's tenth problem

In 1900 David Hilbert posed 23 problems. The tenth asked for a process to test whether a polynomial has an **integral root**. Proving that no such algorithm exists needed a precise definition of algorithm, which the 1936 papers of Church and Turing supplied. In 1970 **Yuri Matijasevič**, building on Davis, Putnam and Robinson, showed that no such algorithm exists. The set D of polynomials with an integral root is Turing-recognisable but not decidable.

## Gödel's incompleteness theorems

Until 1931 mathematics was thought complete. Kurt Gödel's 1931 paper, "On Formally Undecidable Propositions of Principia Mathematica and Related Systems", changed that.

- **First theorem:** any consistent formal system that can express basic arithmetic contains true statements that cannot be proved within it. The proof builds a self-referential Gödel sentence that asserts its own unprovability.
- **Second theorem:** such a system cannot prove its own consistency.

Together they ended Hilbert's dream of a complete, consistent set of axioms for all of mathematics: there is no mathematical theory of everything.

## Gödel numbering

Gödel mapped every symbol, formula and proof to a unique number. In the Nagel and Newman version, 12 elementary symbols get the numbers 1 to 12; for example ~ is 1, = is 5, 0 is 6 and s ("successor of") is 7. Variables take the primes greater than 12. A formula is encoded by raising successive primes to the symbols' numbers, so 0 = 0 becomes 2⁶ × 3⁵ × 5⁶ = 243,000,000. Unique prime factorisation lets it be decoded. Statements about formulas then become statements about numbers.

Source: DLC CSC 552 Theory of Computation.pdf, Study Sessions 2 and 3
