'''
Given: A DNA string s
 of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s
. Strings can be returned in any order.

import Bio
from Bio import Seq
from Bio import Alphabet
from Bio.Seq import IUPAC
'''

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



