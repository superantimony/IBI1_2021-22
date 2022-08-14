import re
#read the file
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
inp = xfile.read()
#to extract all genes from the file
inp =re.sub(r'\n','',inp)
genes = re.split(r'>',inp)
get_start_genes =[]
for x in range(0,len(genes)):
    if re.search("ATG",genes[x]):
        get_start_genes.append(genes[x])
gene_name = re.findall('gene;(......)',str(get_start_genes))
sequence = re.findall('[A-T]{20,}',str(get_start_genes))
gene_lenth = []
for i in range (0,len(sequence)):
    gene_lenth.append(len(sequence[i]))
start_genes_list = []
for a in range(0,len(sequence)):
    start_genes_list.append('>'+str(gene_name[a])+' '+str(gene_lenth[a]) + '\n'+str(sequence[a])+'\n')
start_genes_list = "".join(start_genes_list)
start_genes = open('start_genes.fa','w')
start_genes.write(start-genes_list)
start_genes.close()