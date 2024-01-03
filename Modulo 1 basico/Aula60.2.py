hora = int(input("Qual hr? "))

if hora > 0 and hora <= 11:
    print("Bom dia")
elif hora >= 12 and hora <= 18:
    print("Boa tarde")
else:
    print("Boa noite")