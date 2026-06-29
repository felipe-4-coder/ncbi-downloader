import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Lê o arquivo .fna da Drosophila
arquivo = r"C:\Biopython\ncbi_downloader\data\ncbi_dataset\data\GCF_000001215.4\GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna"

total_bases = 0
total_gc = 0

print("Calculando GC content por cromossomo...")
for record in SeqIO.parse(arquivo, "fasta"):
    gc = gc_fraction(record.seq) * 100
    tamanho = len(record.seq)
    total_bases += tamanho
    total_gc += tamanho * gc / 100
    print(f"  {record.id} — {tamanho} bp — GC: {gc:.2f}%")

print(f"\nGC content total do genoma: {total_gc/total_bases*100:.2f}%")