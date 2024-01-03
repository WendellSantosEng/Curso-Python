palavra = input("Digite a palavra: ")

tam = len(palavra)

palavra_2 = "*" * tam

print(palavra_2)

while "*" in palavra_2:

    letra = input("Digite uma letra: ")

    for j in range(tam):
        if letra in palavra:
            palavra_2[j] = letra

            print(f"palavra = {palavra_2}")

#ta errado , str é imutavel