
s= 'UCUCCGGGACUGGAUGUAGCGUCUGAAGCCGGUCUACUUUGUAGAUCACUAACAACUACAGUAGGAUCCA'
from Bio import Seq
print(s.count("A"), s.count("G"))
from math import factorial
answer = factorial(s.count("A"))*factorial(s.count("G"))
print(answer)