# Alignment Scoring and Methods

## Scoring an alignment

Since the evolutionary history is unknown, alignments are ranked by a score. The alignment is split into columns, each column is given a weight, and the weights are summed. A **scoring scheme** is a set of rules that gives any alignment its score. It is residue-based: substitution scores for each pair of aligned residues, plus penalties for gaps. It rewards matches and punishes mismatches and gaps. The alignment score is the sum of the substitution scores and the gap penalties.

## Distance scoring

Every alignment gets a non-negative score. Identical sequences score zero, and the **best alignment has the smallest score**. Typically d(a, a) = 0 for identity, d(a, b) > 0 for a substitution, and g = d(a, −) > 0 for a gap. Distance scores are used to build phylogenetic trees.

**Example.** Take AGCCGTAT and ACGATT, with d(a, b) = +2 and g = +4. The alignment A−GCCGTAT over ACGA−−T−T scores 18. The alignment AGCCGTAT over A−−CGATT scores 12, so the second is better.

## Similarity scoring

Scores can be positive, zero or negative. More similar sequences score higher, and the **best alignment has the largest score**. Typically s(a, a) > 0, s(a, b) ≤ 0 and g = s(a, −) < 0. Similarity scores are used for database searching.

**Example.** With s(a, a) = +5, s(a, b) = −3 and g = −8, the same two alignments score −15 and −2. The second is again better.

## Methods of pairwise alignment

- **Brute force (by hand):** slide one sequence along the other and count the identities at each position. List all possible alignments, score them and pick the best. It only suits short, closely related sequences.
- **Dot matrix (dot plot):** write one sequence across the top of a grid and the other down the side. Put a dot wherever the residues match. A **diagonal** run of dots marks a similar region; isolated dots off the diagonal are random matches. It gives a quick picture. Comparing DOROTHYHODGKIN with DOROTHYCROWFOOTHODGKIN, for example, shows two diagonals separated by a gap.
- **Dynamic programming:** considers every pairing of characters under the scoring scheme and returns the optimal alignment. It breaks the problem into sub-problems, solves them optimally, and builds the full solution from them. **Needleman–Wunsch** (1970) does global alignment; **Smith–Waterman** (1981) does local alignment.
- **Heuristic methods:** faster but only approximate, for example **BLAST** (1990) and **FASTA** (1985).

## In exams

Typical questions ask you to compute an alignment's score under given match, mismatch and gap values. Some also separate a **gap opening** penalty from a **gap extension** penalty. Others ask you to apply the dot matrix method to two short sequences, or to name the dynamic programming algorithm for global and for local alignment.

Source: Week 6 and 7- CSC 582-Sequence Alignment.pptx
