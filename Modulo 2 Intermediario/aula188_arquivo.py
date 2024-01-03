caminho_arquivo = ".\\aula188.txt"
arquivo = "aula188.txt"

#abre e fecha o arquivo, o encoding serve para aparecer caracteres diferentes
with open(arquivo, "w", encoding="utf8") as arquivo:
    arquivo.write("OLA\n")

#aqui le o arquivo e mostra na tela, o seek serve para colocar o cursor no inicio do arquivo
#strip tira o primeiro e ultimo caracter, faz como que tire a quebra de linha do final do arquivo
with open(caminho_arquivo, "r") as arquivo:
    arquivo.seek(0,0)
    print(arquivo.read().strip())
