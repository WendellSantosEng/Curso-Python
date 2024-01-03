from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def numero_conta(self):
        return self._numero_conta
    
    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self._numero_conta = numero_conta

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def depositar(self, quant):
        self._saldo += quant
        return self.saldo

    @abstractmethod
    def sacar(self, quant):
        pass

def sacar_(cls):
    def sacar(self, quant):
        self._saldo -= quant
        return self.saldo
    return sacar

class ContaPoupanca(Conta):
    
    @sacar_
    def sacar(self, quant): ...

class ContaCorrente(Conta):

    @sacar_
    def sacar(self, quant): ...

############################################################################
    
class Pessoa(ABC):

    def __init__(self,nome,cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    @abstractmethod
    def nome(self) -> str:
        pass
    @property
    @abstractmethod
    def cpf(self) -> str:
        pass

class Cliente(Pessoa):

    @property
    def nome(self) -> str:
        return self._nome


    @property
    def cpf(self) -> str:
        return self._cpf


############################################################################
    

class Banco:

    def __init__(self):
        self._conta = None
        self._agencia = None
        self._cliente = None

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self, conta):
        self._conta = conta
    
    @property
    def agencia(self):
        return self._agencia
    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia
    
    @property
    def cliente(self):
        return self._cliente
    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente



conta1 = ContaPoupanca("123", "111111", 1000)
conta1.depositar(100)
print(conta1.saldo)

conta1.sacar(200)
print(conta1.saldo)

conta2 = ContaCorrente("456", "222222", 2000)
conta2.depositar(100)
print(conta2.saldo)

conta2.sacar(200)
print(conta2.saldo)



banco_bradesco = Banco()
pessoa1 = Cliente("Wendell", "123.456.789-10")


banco_bradesco.conta = conta1
banco_bradesco.agencia = conta1.agencia
banco_bradesco.cliente = pessoa1


print("DADOS")
print(banco_bradesco.agencia)
print(banco_bradesco.conta.numero_conta)
print(banco_bradesco.cliente.nome, banco_bradesco.cliente.cpf)