from Bio.Seq import Seq

seq = Seq("ATGGCCATTGTAATGGGCCGCTGA")
print(seq.reverse_complement())
print(seq.translate())