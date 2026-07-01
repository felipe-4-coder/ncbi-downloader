import os, time, ssl
from Bio import Entrez, SeqIO
import config

# Contorna problema de certificado SSL em redes corporativas
ssl._create_default_https_context = ssl._create_unverified_context

# Pede o organismo no terminal
organism_input = input(f"Organismo [{config.ORGANISM}]: ").strip()
if organism_input:
    config.ORGANISM = organism_input
    print(f"Organismo selecionado: {config.ORGANISM}")

# Pede o gene no terminal
gene_input = input(f"Gene [{config.GENE}]: ").strip()
if gene_input:
    config.GENE = gene_input

# Define o nome do arquivo de saída com base no gene e organismo
fasta_path = os.path.join(config.OUTPUT_DIR, f"{config.GENE}_{config.ORGANISM.replace(' ', '_')}.fasta")

# --- Configuração ---
Entrez.email = config.EMAIL

# --- Busca os IDs ---
print(f"Buscando {config.GENE} em {config.ORGANISM}...")
handle = Entrez.esearch(
    db="nucleotide",
    term=f"{config.GENE}[Gene] AND {config.ORGANISM}[Organism] AND mRNA[Filter]",
    retmax=config.MAX_RESULTS
)
ids = Entrez.read(handle)["IdList"]
handle.close()
print(f"{len(ids)} sequências encontradas: {ids}")

time.sleep(0.5)
handle = Entrez.efetch(
    db="nucleotide",
    id=",".join(ids),
    rettype="fasta",
    retmode="text"
)
with open(fasta_path, "w") as f:
    f.write(handle.read())
handle.close()

# --- Confirmação ---
seqs = list(SeqIO.parse(fasta_path, "fasta"))
print(f"Salvo em '{fasta_path}' — {len(seqs)} sequências.")
for s in seqs:
    print(f"  {s.id} — {len(s.seq)} bp")