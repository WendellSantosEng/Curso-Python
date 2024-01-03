nome = input("Qual seu nome? ")
idade = input("Sua idade")

print(f"Seu nome e {nome}")

tam = len(nome)

print(f"Seu nome invetido e {nome[::-1]}")

if " " in nome:
    print("Existem espacos em su nome!")

print(f"Seu nome tem {tam} letras")

print(f"A primeira letra do seu nome e {nome[0::]}")

print(f"A ultima letra e {nome[-1]}")

