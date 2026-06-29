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

## Ambiente

- Python 3.14
- Biopython
- NCBI Datasets CLI v18.31.0