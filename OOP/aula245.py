#  Classes Decoradoras

class Multiplicar:

    def __init__(self, multiplicador):
        self.multiplicador = multiplicador

    def __call__(self,func):
        def interno(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interno

@Multiplicar(5)
def soma(x,y):
    return x+y

somando = soma(1,3)

print(somando)