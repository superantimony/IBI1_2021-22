import re
fname = input('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
file = open(fname)
inp = file.read()
inp = re.sub(r'\n', '', inp)
genes = re.split(r'>', inp)
get_start_genes = []
for x in range(0, len(genes)):
    if re.search("ATG", genes[x]):
        get_start_genes.append(genes[x])
#creat lists to store gene name and sequence
gene_name = re.findall('gene:(......)', str(get_start_genes))
sequence = re.findall('[A-T]{20}', str(get_start_genes))
number = []
for a in range(0, len(get_start_genes)):
    x = re.findall("ATG", get_start_genes[a])
    y = len(x)
    number.append(y)



