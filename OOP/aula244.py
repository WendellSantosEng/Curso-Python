# Metodos com funcoes decoradoras


def meu_repr(cls):

    def repr(self):
        class_name = self.__class__.__name__
        class_dict_ = self.__dict__
        class_repr = f"{class_name}({class_dict_})"
        return class_repr
    cls.__repr__ = repr

    return cls

def funcao_decoradora(metodo):
    def interno(self, *args, **kwargs):
        retorno = metodo(self, *args, **kwargs)

        if "Terra" in retorno:
            return "Voce esta em casa, Terra"
        return retorno
    
    return interno

@meu_repr
class Planeta:

    def __init__(self, nome):
        self.nome = nome

    @funcao_decoradora
    def falar_nome(self):
        return f"Meu planeta é {self.nome}"
    
@meu_repr
class Time:

    def __init__(self, nome):
        self.nome = nome

time1 = Time("Brasil")
time2 = Time("Argentina")

planeta1 = Planeta("Terra")
planeta2 = Planeta("Marte")

print(time1)
print(time2)
print(planeta1)
print(planeta2)

print(planeta1.falar_nome())
print(planeta2.falar_nome())