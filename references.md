## references

1. identify residues of the interface(s)
- [Select interface in ChimeraX](https://mail.cgl.ucsf.edu/mailman/archives/list/chimerax-users@cgl.ucsf.edu/thread/LH4R4GFN4Q7SJQQAJJY3M6JO5DN3RCBC/)
- [List residues in interface in ChimeraX](https://mail.cgl.ucsf.edu/mailman/archives/list/chimerax-users@cgl.ucsf.edu/thread/XVXJYW66M73WUQ2VJBPWC4RD2XLRXEG5/)
- [List residues interface](https://mail.cgl.ucsf.edu/mailman/archives/list/chimerax-users@cgl.ucsf.edu/message/ME7T2XFNWJFOFP52VOERL4JFTUKHYF7B/)
- recent PROSS story https://www.biorxiv.org/content/10.1101/2025.07.07.663574v1.full.pdf

2. create list of mutations
- for StaB-ddG - check reference: https://github.com/LDeng0205/StaB-ddG?tab=readme-ov-file#predicting-delta-delta-g-for-a-list-of-mutants
- rename PDB (numbering starts at 1): Tools | Structure Editing | Renumber Sequences
- create a file with two columns `#Pdb` and `mutation`
- first column: 1JU5_A_B

Alphabet: 

>mutations.csv
#Pdb,mutation
1JU5_A_B,KA11A
1JU5_A_B,KA11M
1JU5_A_B,NA10A
...

## exercises

Foldseek: https://pubmed.ncbi.nlm.nih.gov/36408459/

## topics

0. docking

[medchem prep ChimeraX](https://www.youtube.com/watch?v=iZPDRLH9W2U)
[steps medchem prep ChimeraX](https://www.dropbox.com/scl/fi/2e1b7mi0ay3jyb9yydzp0/ChimeraX.pdf?rlkey=z0jqxvsizslfg9j95qi0bv1ht&e=1&dl=0)

[The Art and Science of Molecular Docking](https://www.annualreviews.org/content/journals/10.1146/annurev-biochem-030222-120000)
[Ten tips and tricks for molecular docking](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013030)
[Comparative analysis of virtual screening approaches](https://doi.org/10.1038/s42256-025-00993-0) (paywall)

1. transmembrane proteins
[paper TMVisDB](https://www.sciencedirect.com/science/article/pii/S0022283625000634#da005)
[URL TMVisDB](https://tmvisdb.rostlab.org/)

2. design of protein binder of targets


3. surface influenza neuraminidase


4. 
[](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1616328/full)

1. small molecule molecular docking – 
2. transmembrane proteins : recente publicatie die o.a. AlphaFoldDB gebruikt -> https://tmvisdb.rostlab.org/
3. antigenic changes at surface of influenza neuraminidase -> kunnen we X-ray structuren via ChimeraX visualiseren.
4. TCR-pMHC interactions -> recent papers: https://pubs.acs.org/doi/abs/10.1021/acs.jcim.5c00298 and https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1616328/full
5. ATG9A - https://www.nature.com/articles/s41594-024-01376-6
6. RiPPs - https://www.cell.com/trends/biochemical-sciences/fulltext/S0968-0004(25)00080-5
 
