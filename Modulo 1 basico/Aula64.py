print("\nBEM VINDO A CALCULADORA!")
op=0
while op != 5:
    num1 = int(input("Digite numero 1: "))
    num2 = int(input("Digite o numero 2: "))
    op = int(input("DIGITE A OPERACAO: \n1- SOMA\n2- SUBTRACAO\n3 - MULTIPLICACAO\n4- DIVISAO\n Insira uma opcao: "))

    if op == 1:
        res = num1 + num2
    elif op == 2:
        res = num1 - num2
    elif op == 3:
        res = num1 * num2
    elif op == 4: 
        res = num1 // num2
    elif op == 5:
        print("Saindo...")
    else: 
        print("Digite uma opcao valida")

    print(f"O resultado e {res}")