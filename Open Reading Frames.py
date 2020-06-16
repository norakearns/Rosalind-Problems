import Bio
from Bio import Seq
from Bio import Alphabet
from Bio.Seq import IUPAC
#
# codons = {
#     'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
#     'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
#     'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
#     'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
#     'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
#     'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
#     'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
#     'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
#     'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
#     'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
#     'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
#     'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
#     'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
#     'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
#     'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
#     'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
# }

# mRNA = translate(Seq)
# print(mRNA)
from Bio import SeqIO
from Bio import Alphabet
from Bio.Seq import Seq
for record in SeqIO.parse("C:\\Users\\Nora Kearns\\Downloads\\rosalind_orf (3).txt",'fasta'):
    for_sequence = record.seq
print(for_sequence)

rev_sequence = for_sequence.reverse_complement()
print(rev_sequence)
import re
# matches = re.findall('(GGG)(.+)(CCCC)', str(for_sequence))
#matches = re.findall("ATG", str(for_sequence))
pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
matches = re.findall(pattern, str(for_sequence))
rev_matches = re.findall(pattern, str(rev_sequence))
print(matches)
print(rev_matches)

from Bio import Seq
for i in matches:
    forORF = Seq.translate(i)
    print(forORF)

print(".......REVERSE.........")
for i in rev_matches:
    revORF = Seq.translate(i)
    print(revORF)



