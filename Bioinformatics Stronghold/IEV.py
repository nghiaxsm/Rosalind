file = open('rosalind_iev.txt','r')
line = file.readline().strip().split()
AA_AA = int(line[0])
AA_Aa = int(line[1])
AA_aa = int(line[2])
Aa_Aa = int(line[3])
Aa_aa = int(line[4])
aa_aa = int(line[5])
result=AA_AA*2+AA_Aa*2+AA_aa*2+Aa_Aa*2*3/4+Aa_aa*2*1/2+aa_aa*2*0
print(result)