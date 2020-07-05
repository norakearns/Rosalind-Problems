
from Bio import SeqIO
from Bio import Seq

seqarray = []
for record in SeqIO.parse("C:\\Users\\Nora Kearns\\Downloads\\rosalind_sseq.txt",'fasta'):
    sequence = str(record.seq)
    seqarray.append(sequence)

s = seqarray[0]
t = seqarray[1]
print(s, t)
print(len(t))
count = 0
match_count = 0
while count < len(s) and match_count < len(t):
    if (s[count] == t[match_count]):
        print((count+1), end= ' ')
        match_count +=1
    count += 1
