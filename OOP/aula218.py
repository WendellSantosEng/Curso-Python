class Carro:

    def __init__(self):
        self._nome = None
        self._motor = None
        self._fabricante = None
#carro
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome
#motor
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,motor):
        self._motor = motor
#fabricante   
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,fabricante):
        self._fabricante = fabricante

#########
        
class Motor:

    def __init__(self):
        self._nome = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

#########

class Fabricante:

    def __init__(self):
        self._nome = None

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

########
        
def listar(obj):
    print(carro.nome, carro.fabricante.nome, carro.motor.nome)

carro = Carro()
motor = Motor()
fabricante = Fabricante()

carro.fabricante = fabricante
carro.motor = motor

carro.nome = "GOL"
carro.motor.nome = "1.4"
carro.fabricante.nome = "Volkswagen"

listar(carro)