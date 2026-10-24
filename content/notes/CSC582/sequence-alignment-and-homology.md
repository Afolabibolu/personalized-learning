# Sequence Alignment and Homology

## What alignment is

An alignment is a mutual arrangement of two sequences that shows where they are similar and where they differ. More precisely, sequence alignment establishes residue-to-residue correspondence between two or more sequences, keeping the order of residues in each. It arranges DNA, RNA or protein sequences to find regions of similar character patterns in the same order.

An **optimal alignment** shows the most correspondences and the fewest differences. It is the alignment with the highest score, which may or may not be biologically meaningful.

## Why align sequences

- **Discovering function:** similar sequences probably have the same function.
- **Predicting structure:** similar protein sequences probably have similar secondary and 3-D structures.
- **Discovering evolutionary relationships:** similar sequences probably shared an ancestor, though not always.

Alignment supports the annotation of new sequences, the modelling of protein structures and phylogenetic analysis.

## Homology and mutation

One goal of alignment is to infer **homology**, origin from a common ancestor, from observed similarity. Species families diverged during evolution through three kinds of mutation:

- **Substitution** changes a residue: ACGTTGAC → ACGATGAC.
- **Deletion** removes residues.
- **Insertion** adds residues.

Gaps (−) may be introduced so that order is preserved. For example, abcde and acdef align as abcde− over a−cdef.

## Identity, similarity and homology

- **Identity** means exactly the same nucleotide or amino acid in the same position.
- **Similarity** is the degree of likeness, which includes substitutions with similar chemical properties.

As rules of thumb, 25% amino acid identity is needed to call protein homology and 70% nucleotide identity to call gene homology. Similarity is a percentage; homology is a yes-or-no statement about shared ancestry, so there is no "% homology". Similarity does not imply homology, but homology usually implies similarity.

- **Orthologous** sequences are similar sequences in different species, from a speciation event, with a similar function.
- **Paralogous** sequences are related through gene duplication and can have different functions within one species.

A sequence can be both, and orthology is a form of homology.

## Types of alignment

- **Pairwise:** compares the residues of two sequences to find the best pairing.
- **Multiple:** aligns more than two sequences at once. It suits the search for subtle conserved patterns in a protein family.
- **Global:** the best match of both sequences over their entire length. It is useful when the sequences are related throughout, such as similar proteins from close species. Gaps may appear inside the alignment or at its ends.
- **Local:** the best match between subsequences. It is useful for proteins that share a motif or domain but differ elsewhere, and for comparing proteins against long genomic DNA.

Source: Week 6 and 7- CSC 582-Sequence Alignment.pptx
