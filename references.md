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



