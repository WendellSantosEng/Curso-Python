# Tudo que esta comentado é outra maneira de fazer
# 
# Essa aula foi sobre decorators em classes, utilizando o __repr__
# para evitar repetição de codigo

def meu_repr(cls):

    def repr(self):
        class_name = self.__class__.__name__
        class_dict_ = self.__dict__
        class_repr = f"{class_name}({class_dict_})"
        return class_repr
    cls.__repr__ = repr

    return cls

@meu_repr
class Planeta:

    def __init__(self, nome):
        self.nome = nome

    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict_ = self.__dict__
    #     class_repr = f"{class_name}({class_dict_})"
    #     return class_repr
        
@meu_repr
class Time:

    def __init__(self, nome):
        self.nome = nome

    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     class_dict_ = self.__dict__
    #     class_repr = f"{class_name}({class_dict_})"
    #     return class_repr

# Time = meu_repr(Time)
time1 = Time("Brasil")
time2 = Time("Argentina")

planeta1 = Planeta("Terra")
planeta2 = Planeta("Marte")

print(time1)
print(time2)

print(planeta1)
print(planeta2)
