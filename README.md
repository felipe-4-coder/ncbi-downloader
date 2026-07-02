# NCBI Downloader

Projeto de estudo para praticar ferramentas e conceitos básicos de bioinformática usando Python e Biopython.

## O que esse projeto faz

- **downloader.py** — baixa sequências de um gene específico diretamente do NCBI (formato FASTA), com o gene escolhido interativamente pelo terminal
- **gc_analysis.py** — calcula o GC content (porcentagem de bases Guanina e Citosina) de um genoma completo a partir de um arquivo `.fna`
- **datasets.exe** — ferramenta oficial do NCBI para baixar genomas completos (assemblies) via terminal
- **config.py** — centraliza as configurações do projeto (e-mail, organismo, número de resultados)

## Por que criei esse projeto

Sou estudante de Biomedicina com foco em genômica e estou aprendendo bioinformática de forma prática. Esse projeto foi meu primeiro contato real com acesso programático a dados do NCBI.

## O que aprendi

- Navegar pelo terminal do Windows (PowerShell)
- Criar e organizar um projeto Python no VSCode
- Usar o módulo `Bio.Entrez` para buscar e baixar sequências do NCBI
- Resolver erros de SSL, caminhos de arquivo e ambiente virtual
- Calcular GC content de um genoma completo com Biopython

## Como usar

## Configuração
Antes de rodar, edite o `config.py` e substitua `seu@email.com` pelo seu e-mail real.

### Baixar sequências de um gene
```bash
python downloader.py
```

### Calcular GC content de um assembly
```bash
python gc_analysis.py
```

### Baixar um genoma completo
```bash
.\datasets.exe download genome taxon "organismo" --reference --filename data/output.zip
```

## Assembly Downloader

### 30/06 — Implementação do `assembly_downloader.py`

**O que foi feito:**
Criação do módulo `assembly_downloader.py`, que permite baixar a montagem (assembly) de um genoma completo à escolha do usuário diretamente pelo terminal.

**Como funciona:**
O módulo utiliza a função `def download_assembly()`, que solicita ao usuário o nome do organismo e o nome do arquivo de saída via `input()`. Em seguida, usa o módulo `subprocess` do Python para executar o `datasets.exe` de dentro do código — como se os comandos fossem digitados manualmente no terminal, mas de forma automatizada via Python.

```python
subprocess.run([".\\datasets.exe", "download", "genome", "taxon", assembly_taxon, "--reference", "--filename", output_dir])
```

Cada elemento da lista é executado de forma ordenada pelo `subprocess.run()`.

**Próximos passos:**
- Permitir escolha da fonte (GenBank, RefSeq)
- Baixar múltiplas montagens de uma vez

### 01/07 - Aprimoramento do sistema de busca de genes `gene_downloader.py`

**O que foi feito:**
Aprimoramento do sistema de busca `downloader.py`, agora `gene_downloader.py`. O novo mecanismo permite a escolha de um organismo do qual o gene específico será baixado.

## Ambiente

- Python 3.14
- Biopython
- NCBI Datasets CLI v18.31.0