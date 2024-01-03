lista_a = []
lista_b = []
lista_c = []
lista_d = []
soma = 0
mult = 10

cpf = "146.869.086-??"

for digito in cpf:
    lista_a.append(digito)

for item in lista_a:
    if item == ".":
        continue
    if item == "-":
        break
    else:
        if item.isdigit():
            lista_b.append(int(item))

for digito in lista_b:
    int(digito)

    valor = digito * mult
    lista_c.append(valor)
    soma = valor + soma
    
    mult = mult - 1

resto = (soma *10) % 11

primeiro_digito = resto if resto <= 9 else 0
print("O primeiro digito e: ", primeiro_digito)
lista_b.append(primeiro_digito)
print(lista_b)

mult = 11
soma = 0

for digito in lista_b:
    int(digito)

    valor = digito * mult
    lista_d.append(valor)
    soma = valor + soma

    mult = mult - 1

soma = soma*10
resto = soma % 11

segundo_digito = resto if resto <= 9 else 0

print("O segundo digito e: ", segundo_digito)

lista_b.append(segundo_digito)
print(lista_b)

