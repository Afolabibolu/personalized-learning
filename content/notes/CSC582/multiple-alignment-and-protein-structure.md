# Multiple Sequence Alignment and Protein Structure Prediction

## Multiple sequence alignment (MSA)

A **multiple sequence alignment** lines up three or more biological sequences, DNA, RNA or protein, so that matching positions sit in the same column. Gaps are inserted where sequences have gained or lost residues.

MSA matters because columns that stay the same across many related sequences point to **conserved regions**, which are usually important for function or structure. Its main applications are:

- finding conserved motifs and functional domains
- building **phylogenetic trees**, showing how sequences evolved
- predicting protein structure and function
- designing PCR primers from conserved regions
- annotating new sequences by comparison with known ones

Aligning many sequences exactly with dynamic programming takes time that grows exponentially with the number of sequences, so practical tools use heuristics.

**Progressive alignment**, used by the Clustal programs, works in three steps:

1. Align every pair of sequences and compute a distance matrix.
2. Build a **guide tree** from the distances, for example by neighbour-joining.
3. Align the sequences in the order given by the tree, most similar first, adding each sequence or group to the growing alignment.

Its main weakness is "once a gap, always a gap": errors made early are never corrected. The result also depends on the guide tree and on the gap penalties, and it is poor when sequences are very divergent. **Iterative** methods (MUSCLE, MAFFT) refine the alignment repeatedly, and **consistency-based** methods (T-Coffee) use information from all pairwise alignments. Common tools: Clustal Omega, MUSCLE, MAFFT, T-Coffee.

## Protein structure

A protein's function follows from its 3D shape, described at four levels:

- **Primary:** the amino acid sequence.
- **Secondary:** local shapes held by hydrogen bonds, mainly the α-helix and the β-sheet.
- **Tertiary:** the full 3D fold of one chain.
- **Quaternary:** several chains (subunits) together, as in haemoglobin.

Structures are determined experimentally by **X-ray crystallography**, **NMR spectroscopy** and **cryo-electron microscopy**, and stored in the PDB. These methods are slow and costly, so many structures are predicted computationally.

## Structure prediction

The three main computational approaches are:

- **Homology (comparative) modelling:** builds the target from a related protein of known structure.
- **Threading (fold recognition):** fits the sequence onto known folds when sequence similarity is low.
- **Ab initio (de novo):** predicts the fold from physical principles alone.

Deep learning (AlphaFold) now predicts many structures accurately.

**Homology modelling** needs a template structure with clear sequence similarity to the target. Its steps are: identify a template (for example by BLAST against the PDB), align the target to it, build the model, refine it, and validate it (for example with a Ramachandran plot). Tools include MODELLER and SWISS-MODEL. Its limits are novel folds with no template, alignment errors, loop regions and low similarity.

Source: general knowledge (no CSC 582 lecture file covers these topics); they are the topics asked in the CSC 725 M.Sc. papers filed with this course
