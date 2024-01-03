def mult(num):
    resul = 1
    for numero in num:
        resul = resul * numero
    return resul

num = (1,2,3,4,5)

res = mult(num)
print(res)