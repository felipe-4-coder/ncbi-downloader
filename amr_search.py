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

    with open(f"{output_dir}/resultados.txt", "r") as resultados:

        # Lê o arquivo de resultados da busca e exibe as informações dos genes encontrados com identidade maior ou igual a 90%, juntamente com informações relevantes, como a posição inicial e final do gene na sequência de DNA analisada.

        for linha in resultados:
            columns = linha.split('\t')
            if float(columns[2]) >= 90.0:
                print(f"Gene: {columns[1].split('|')[-1]}")
                print(f"Identidade: {columns[2]}%")
                print(f"Posição inicial: {columns[6]}")
                print(f"Posição final: {columns[7]}")
                print("-----------------------------")
                
search_amr_genes()