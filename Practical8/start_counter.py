seq = "CAATCGACTAATGCGATCAATCGAGGGCC"
seq1= "ATG"
import re
x = re.findall(seq1, seq)
y = len(x)
print("The total number of 'ATG' is "+str(y)+"")
#the result is 1
