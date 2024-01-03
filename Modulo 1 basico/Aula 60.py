n1 = input("Digite numero 1: ")

if n1 is int:
    print("Numero e um inteiro")
    if int(n1) % 2 == 0:
        print("Numero par!")
    else:
        print("Numero impar!")
else:
    print("Numero nao e um inteiro")
