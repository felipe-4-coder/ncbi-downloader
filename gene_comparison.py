from Bio import SeqIO
from Bio import pairwise2

# Função para comparar duas sequências de DNA

def compare_sequences(seq1, seq2):
     
    # Compare duas sequências de DNA e retorna a pontuação de alinhamento.
    
    gene_comp = pairwise2.align.globalxx(seq1, seq2)
    best = gene_comp[0]

    similaridade = (best.score / max(len(seq1), len(seq2))) * 100

    return similaridade

# Solicita ao usuário que insira quais genes ele deseja comparar

gen1 = input("Digite o caminho do primeiro arquivo FASTA: ")
gen1_seq = next(SeqIO.parse(gen1, "fasta")).seq

gen2 = input("Digite o caminho do segundo arquivo FASTA: ")
gen2_seq = next(SeqIO.parse(gen2, "fasta")).seq

# Calcula a similaridade entre os dois genes usando a função compare_sequences

similaridade = compare_sequences(gen1_seq, gen2_seq)

# Exibe a similaridade entre os genes

print(f"A similaridade entre os genes é: {similaridade:.2f}%")