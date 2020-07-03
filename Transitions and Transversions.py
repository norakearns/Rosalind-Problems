
from Bio import SeqIO
from Bio import Seq

seqarray = []
for record in SeqIO.parse("C:\\Users\\Nora Kearns\\Downloads\\rosalind_tran (1).txt",'fasta'):
    sequence = str(record.seq)
    seqarray.append(sequence)
    print(seqarray)

s1 = seqarray[0]
s2 = seqarray[1]
print(s1, s2)

transitions = 0
transversions = 0
for i in range(len(s1)):
    if s1[i] == 'G' and s2[i] == 'A':
        transitions += 1
    elif s1[i] == 'A' and s2[i] == 'G':
        transitions += 1
    elif s1[i] == 'C' and s2[i] == 'T':
        transitions += 1
    elif s1[i] == 'T' and s2[i] == 'C':
        transitions += 1
    elif s1[i] == 'G' and s2[i] == 'T':
        transversions += 1
    elif s1[i] == 'G' and s2[i] == 'C':
        transversions += 1
    elif s1[i] == 'T' and s2[i] == 'G':
        transversions += 1
    elif s1[i] == 'T' and s2[i] == 'A':
        transversions += 1
    elif s1[i] == 'A' and s2[i] == 'C':
        transversions += 1
    elif s1[i] == 'A' and s2[i] == 'T':
        transversions += 1
    elif s1[i] == 'C' and s2[i] == 'A':
        transversions += 1
    elif s1[i] == 'C' and s2[i] == 'G':
        transversions += 1
print(transitions/transversions)