# Biological Databases and Tools

## Biological databases

Biological databases are repositories in which biological data at several levels are organised. A bioinformatician needs to know which databases exist and which tools can mine them. Databases can be public or private, nucleotide, protein, structure, literature or annotation, generalised or specialised, curated or non-curated, and sequence-centred or genome-centred.

**Nucleotide (DNA sequence) databases** are annotated collections of publicly available DNA sequences. An entry usually includes a description, the taxonomy of the source organism, coding regions, mutation sites and references.

- **Primary** databases hold original submissions by experimentalists: EMBL-EBI, NCBI **GenBank** and DDBJ. Together they form the International Nucleotide Sequence Database Collaboration (**INSDC**) and are updated regularly.
- **Secondary** databases are derived from the primary ones. They are curated, non-redundant and richly annotated, for example UniGene and **RefSeq**.

**Protein databases:**

- **Primary:** PIR, **SWISS-PROT** (reviewed and manually annotated) and **TrEMBL** (unreviewed and automatically annotated). They describe a protein's function, domains and modifications.
- **Secondary (composite):** filter several primary databases into non-redundant sets of families, domains and patterns, for example PROSITE, Pfam, PRINTS and PANTHER.

**Other kinds:**

- **Genome databases** store whole genomes: Ensembl, the NCBI Data Viewer and the UCSC Genome Browser.
- **Structural databases:** **PDB**, the main primary database of 3-D structures from X-ray crystallography and NMR; CATH, a hierarchical classification of protein domain structures; and SCOP.
- **Genetic variation:** **dbSNP**, the largest general database of variations, including InDels.
- **Gene expression:** GEO, Expression Atlas and ArrayExpress, which hold microarray data.
- Literature, organism-specific, disease-specific and gene ontology databases.

## Bioinformatics tools

- **Entrez:** a retrieval system that searches several databases, such as GenBank and Swiss-Prot.
- **BLAST and FASTA:** compare a DNA or protein sequence against databases and retrieve the matching entries, a similarity search.
- **Dotplot:** compares two sequences. **Clustal:** aligns multiple sequences.
- **SEQIO and READSEQ:** convert sequence formats.
- **TACG2:** finds restriction-enzyme cut sites. **SAPS:** protein sequence analysis. **BCM Gene Finder:** nucleic acid analysis.
- **nnPredict, COPIA, Rasmol, PROSPECT:** protein structure prediction.
- **EMBOSS:** sequence analysis. **PatternHunter:** repeat identification.

The most popular resources are the **National Centre for Biotechnology Information (NCBI)** and the **European Bioinformatics Institute (EMBL-EBI)**. Data can be searched by accession number or gene name.

Source: Week 4 -CSC 582-Biological Databases&Tools.pptx
