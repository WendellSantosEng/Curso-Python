# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
# import csv
# from pathlib import Path

# CAMINHO_CSV = Path(__file__).parent / 'csv.csv'

# with open(CAMINHO_CSV, 'r', encoding="utf8") as arquivo:
#     leitor = csv.DictReader(arquivo)

#     for linha in leitor:
#         print(linha['Nome'], linha['Idade'], linha['Endereço'])

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)
        
#################################################################################################


# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding="utf8") as arquivo:
    nome_colunas = lista_clientes[0].keys() #cabeçalho
    escritor = csv.DictWriter( #escreve no csv um discionario
        arquivo,
        fieldnames=nome_colunas 
    )
    escritor.writeheader() #escreve o cabeçalho

    for cliente in lista_clientes: #escreve o corpo
        print(cliente)
        escritor.writerow(cliente)

# Aqui abaixo escreve uma lista em um csv

# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)