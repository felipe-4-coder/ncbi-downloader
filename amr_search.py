# Este módulo permite realizar a busca no banco de dados AMR (Antiresistance Gene Database) para identificar genes de resistência a antibióticos em sequências de DNA.

import subprocess

def search_amr_genes():

    # Solicita ao usuário o caminho do arquivo de sequência de DNA que será analisado.
    dna_sequence_file = input("Digite o caminho do arquivo de sequência de DNA a ser analisado: ")

    # Solicita ao usuário o banco de ados que será usado para realizar a comparação e busca de genes de resistência a antibióticos.
    amr_database = input("Digite o caminho do banco de dados AMR (Antimicrobial Resistance) que será utilizado para a comparação e busca:")

    # Solicita ao usuário o diretório onde os resultados ficarão armazenados.
    output_dir = input("Digite o diretório onde os resultados da busca ficarão armazenados:")

    # Executa o comando para realizar a busca de genes de resistência a antimicrobianos.
    subprocess.run(["blastn", "-query", dna_sequence_file, "-db", amr_database, "-out", f"{output_dir}/resultados.txt", "-outfmt", "6", "-perc_identity", "90"])

    # Carrega o banco de dados AMR presetes em aro.tsv
    mecanismo = {}
    with open("data/references/card-ontology/aro.tsv", "r") as aro_file:
        for line in aro_file:
            columns = line.strip().split('\t')
            if len(columns) >= 3:
                nome_gene = columns[1]
                descricao = columns[2]
                mecanismo[nome_gene] = descricao

    with open(f"{output_dir}/resultados.txt", "r") as resultados:

        # Lê o arquivo de resultados da busca e exibe as informações dos genes encontrados com identidade maior ou igual a 90%, juntamente com informações relevantes, como a posição inicial e final do gene na sequência de DNA analisada.

        # Etapa 1: popular o dicionário
        melhores = {}
        for linha in resultados:
            columns = linha.split('\t')
            if float(columns[2]) >= 90.0:
                gene = columns[1].split('|')[-1]
                identidade = float(columns[2])
                posicao = columns[6]
        
                if posicao not in melhores:
                    melhores[posicao] = (gene, identidade)
                else:
                    if identidade > melhores[posicao][1]:
                        melhores[posicao] = (gene, identidade)

        # Etapa 2: printar os resultados
        for posicao, (gene, identidade) in melhores.items():
            print(f"Gene: {gene}")
            print(f"Identidade: {identidade}%")
            print(f"Posição inicial: {posicao}")
            print(f"Mecanismo: {mecanismo.get(gene, 'Não encontrado')}")
            print("-----------------------------")
                
search_amr_genes()