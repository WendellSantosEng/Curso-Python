nome = input("Seu nome? ")
tam = len(nome)

if tam <= 4:
    print("Seu nome e curto")
elif tam >= 5 and tam <= 6:
    print("Nome normal")
else:
    print("Nome grande")
