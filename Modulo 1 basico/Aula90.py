lista_compra = []

op = "0"

while op != "4":

    op = input("Selecione\n1- COLOCAR ITEM\n2- RETIRAR ITEM\n3- IMPRIMIR LISTA\n4- SAIR\n    ->Digite a opcao: ")
   
    if op == "1":

        item = input("Digite o item: ")
        lista_compra.append(item)
    elif op == "2":

        item = input("Digite o item que deseja remover: ")
        lista_compra.remove(item)
    elif op == "3":

        print(lista_compra)
    else:
        print("SAINDO")