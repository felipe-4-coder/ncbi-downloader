# NCBI Downloader

Projeto de estudo para praticar ferramentas e conceitos básicos de bioinformática usando Python e Biopython.

## Filosofia do projeto

Todo sequenciamento começa com uma pergunta biológica. 
Este projeto é uma caixa de ferramentas para responder 
perguntas sobre genomas — desde o download dos dados até 
a comparação e busca de sequências. As ferramentas aqui 
desenvolvidas refletem o fluxo real de um projeto de 
genômica: primeiro entendemos as possibilidades, depois 
avançamos para as aplicações.

## O que esse projeto faz

- **gene_downloader.py** — baixa sequências de um gene específico diretamente do NCBI (formato FASTA), com escolha interativa do gene, organismo e e-mail via terminal
- **assembly_downloader.py** — permite baixar a montagem (assembly) de um genoma completo à escolha do usuário, utilizando o módulo `subprocess` para executar o `datasets.exe` de dentro do código
- **gene_comparison.py** — compara dois genes de organismos diferentes e retorna a taxa de similaridade entre as sequências em %
- **gc_analysis.py** — calcula o GC content (porcentagem de bases Guanina e Citosina) de um genoma completo a partir de um arquivo `.fna`
- **datasets.exe** — ferramenta oficial do NCBI para baixar genomas completos (assemblies) via terminal
- **config.py** — centraliza as configurações do projeto (e-mail, organismo, número de resultados)
- **gene_search.py** — busca a presença de um gene específico no arquivo GFF de um genoma, retornando cromossomo, tipo, posição de início e fim, e produto gênico

## Por que criei esse projeto

Sou estudante de Biomedicina com foco em genômica e estou aprendendo bioinformática de forma prática. Esse projeto foi meu primeiro contato real com acesso programático a dados do NCBI.

## O que aprendi

- Navegar pelo terminal do Windows com mais confiança — buscar arquivos, 
  pastas e executar comandos com menos dependência de interfaces gráficas
- Estruturar projetos Python com separação de responsabilidades (um módulo 
  para cada função)
- Escrever funções com `def` e entender quando e por que usá-las
- Usar o módulo `with open()` para leitura de arquivos
- Formatar saídas com `print()` e f-strings para tornar os dados legíveis
- Usar o módulo `pairwise2` para comparar sequências de DNA e retornar 
  similaridade em %
- Entender a estrutura de arquivos GFF e extrair informações relevantes 
  como cromossomo, tipo, locus e produto gênico
- Escrever código com menos dependência do autocomplete — entendendo o 
  que cada linha faz antes de aceitá-la
- Compreender que bioinformática começa com uma pergunta biológica: 
  a ferramenta certa só faz sentido quando a pergunta está clara

## Como usar

### Configuração
Antes de rodar, edite o `config.py` e substitua `seu@email.com` pelo seu e-mail real.

### Baixar sequências de um gene
```bash
python gene_downloader.py
```

### Calcular GC content de um assembly
```bash
python gc_analysis.py
```

### Baixar um genoma completo
```bash
python assembly_downloader.py
```

### Comparar dois genes entre organismos diferentes
```bash
python gene_comparison.py
```

### Buscar um gene no arquivo GFF de um genoma
```bash
python gene_search.py
```

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

### 02/07 - Atualiação em `gene_downloader.py`

**O que foi feito:**
Adição da possibilidade de inserir um e-mail próprio para fazer requisições ao NCBI.

## Gene comparison

## 03/07 - Adição do módulo "gene_comparison.py"

**O que foi feito**
Adição do módulo "gene comparison" que nos permite realizar a comparação de dois genes entre organismos diferentes, após o fim dessa comparação o módulo nos retorna o valor em " % " para a taxa de similaridade entre as bases.

**Resultados obtidos (gene TERT):**
- *Homo sapiens* vs *Pan troglodytes*: 94.51%
- *Homo sapiens* vs *Mus musculus*: 65.79%

## Gene Search

### 05/07 - Adição do módulo `gene_search.py`

**O que foi feito:**
Adição do módulo `gene_search.py`, que busca a presença ou ausência de um gene específico 
no arquivo GFF de um genoma. Caso o gene seja encontrado, o módulo retorna:

- Cromossomo onde o gene está localizado
- Tipo (CDS, exon, gene...)
- Posição de início e fim no cromossomo
- Produto gênico

**Aprendizado:**
Buscar por locus tag é mais preciso do que buscar pelo nome do gene, pois nomes são ambíguos 
mas locus tags são únicos. Para genomas desconhecidos ou mal anotados, o BLAST é a ferramenta 
ideal para identificar genes antes de buscá-los no GFF.

**Próximos passos:**
- Integrar BLAST ao projeto para identificação de genes desconhecidos
- Melhorar o sistema de busca para aceitar múltiplos termos

## AMR Search

### 07/07 - Adição do módulo `amr_search.py`

**O que foi feito:**
Implementação do módulo `amr_search.py`, que permite identificar genes de resistência 
antimicrobiana (AMR) em genomas bacterianos utilizando o BLAST e o banco de dados CARD 
(Comprehensive Antibiotic Resistance Database).

**Como funciona:**

*Primeira parte — Busca:*
1. O usuário informa o genoma bacteriano a ser analisado
2. O módulo executa o BLAST via `subprocess`, comparando o genoma contra o banco do CARD
3. Um arquivo `resultados.txt` é gerado com todos os hits encontrados

*Segunda parte — Tratamento dos resultados:*
1. O módulo lê o `resultados.txt` automaticamente
2. Filtra apenas resultados com identidade ≥ 90%
3. Exibe de forma limpa: nome do gene, identidade e posição no genoma

**Resultado obtido:**
Análise da *Klebsiella pneumoniae* (GCF_000240185.1) identificou genes das famílias 
**TEM** (beta-lactamases), **CTX-M-45** (ESBL) e **APH(6)-Id** (resistência a aminoglicosídeos) 
— confirmando o perfil multirresistente do isolado.

**Ferramentas utilizadas:**
- BLAST 2.17.0+
- CARD 4.0.1
- `subprocess` do Python

**Próximos passos:**
- Remover genes duplicados dos resultados
- Adicionar o mecanismo de resistência de cada gene
- Expandir para análise de múltiplos genomas simultaneamente

### 09/07 - Aprimoramento do `amr_search.py`

**O que foi feito:**
Aprimoramento da função `search_amr_genes()` com a implementação de um dicionário 
`melhores = {}` que armazena, para cada posição no genoma, apenas o gene com maior 
identidade. O resultado passou de 1374 linhas com duplicatas para uma lista limpa 
com o melhor match por posição.


## Ambiente

- Python 3.14
- Biopython
- NCBI Datasets CLI v18.31.0