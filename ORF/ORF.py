#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
# Authors:
#   Nora Kearns <nora.c.kearns@gmail.com>

# Problem sourced from: https://rosalind.info/problems/orf/

"""
Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s
Strings can be returned in any order.
"""

import argparse
import regex as re
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Seq
import os


def main() -> None:
    parser = argparse.ArgumentParser(
       description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
   )
    parser.add_argument("fasta", help="Input fastq")
    parser.add_argument("output", help="Output counts file")
    args = parser.parse_args()

    pattern = re.compile(r"(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))") # regex for an Open Reading Frame (ORF)
    results_fh = open(args.output, "wt")

    for record in SeqIO.parse(args.fasta,'fasta'):
        for_sequence = record.seq
        rev_sequence = for_sequence.reverse_complement()

        fwd_matches = re.findall(pattern, str(for_sequence)) # find all ORF matches in forward sequence
        rev_matches = re.findall(pattern, str(rev_sequence)) # find all ORF matches in reverse sequence

        unique_proteins = []

        for i in fwd_matches:
            forORF = Seq.translate(i) # translate ORF matches to AA sequences
            if forORF not in unique_proteins:
                unique_proteins.append(forORF)

        for i in rev_matches:
            revORF = Seq.translate(i) # translate ORF matches to AA sequences
            if revORF not in unique_proteins:
                unique_proteins.append(revORF)
    
        results_fh.write(">" + record.id + "\n")
        results_fh.write("\n".join(unique_proteins))


if __name__ == "__main__":
    main()




