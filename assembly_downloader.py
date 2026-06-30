import subprocess

def download_assembly():

    assembly_taxon = input("Digite o nome do organismo a ser baixado: ")
    output_dir = input("Digite o diretório onde os dados do organismo serão baixados: ")
    
    subprocess.run([".\\datasets.exe", "download", "genome", "taxon", assembly_taxon, "--reference", "--filename", output_dir])

download_assembly()