# Define qual será o gene buscado no arquivo GFF

gene_input = input("Digite o gene que deseja buscar no arquivo GFF: ").strip()
gff_file = input("Digite o caminho do arquivo GFF: ").strip()

# Faz a busca do gene alvo no arquivo GFF e exibe as informações encontradas

if gene_input:

    with open(gff_file, "r") as f:
        for line in f:
            if line.startswith('#'):
                continue
            if gene_input in line:
                columns = line.split('\t')
                print(f"Informações do gene {gene_input}:") # Informações do gene encontrado
                print(f"Cromossomo: {columns[0]}") # Indica o cromossomo onde o gene está localizado
                print(f"Tipo: {columns[2]}") # Região codificante
                print(f"Início: {columns[3]}") # Indica a posição inicial do gene no cromossomo
                print(f"Fim: {columns[4]}") # Indica a posição final do gene no cromossomo

                atributos = columns[8].split(";")
                product = next((a.split("=")[1] for a in atributos if a.startswith("product=")), "N/A")
                
                print(f"Produto: {product}") # Indica o produto do gene encontrado
                print(f"-----------------------------")