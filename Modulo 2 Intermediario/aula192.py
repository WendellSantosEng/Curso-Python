def acao(acao, lista=None, lista_secundaria = None):
    if lista == None:
        lista = []
    if acao == "refazer":
        refaz(lista, lista_secundaria)
    elif acao == "desfazer":
        desfazer(lista,lista_secundaria)
    elif acao == "listar":
        print(lista)
        print()
    else:
        lista.append(acao)
        
    return lista

def refaz(lista, lista_secundaria):
    tam = len(lista_secundaria)
    var = lista_secundaria[tam-1]
    lista.append(var)
    lista_secundaria.pop()

def desfazer(lista, lista_secundaria):
    tam = len(lista)
    var = lista[tam - 1]
    lista_secundaria.append(var)
    lista.pop()

lista_principal = []
lista_secundaria = []

while True:
    print(
        "Digite algo:\n",
        "refazer -> refaz o que foi desfeito( ctrl + y)\n", 
        "desfazer -> desfaz uma acao feita anteriormente ( ctrl + z)\n",
        "listar -> mostra a lista\n",
        "outra coisa -> lista essa acao\n",
        "SAIR -> fecha o programa\n",
    )

    action = input()
    
    if action == "SAIR" :
        break

    acao(action,lista_principal,lista_secundaria)