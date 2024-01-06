from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia: str| None, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    def __str__(self):
        return f'\n     => Agencia: {self._agencia}\n     => Numero da Conta: {self._numero_conta}\n     => Saldo: {self.saldo}'
   
    @property
    def agencia(self) -> str | None:
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
    def sacar(self, quant,conta):
        pass
class ContaPoupanca(Conta):
    def sacar(self, quant,conta):
        if isinstance(conta, ContaPoupanca):
            if self._saldo - quant < -500 : # A conta é Poupança, entao o Banco esta dando 500 a mais pra sacar
                print("Sua conta é poupanca, o seu limite de saque ja foi atingido!")
                return False
            self._saldo -= quant
            return self.saldo
        elif isinstance(conta, ContaCorrente):
            if self._saldo - quant < 0 :
                print("Nao foi possivel sacar esse valor")
                return False
            self._saldo -= quant
            return self.saldo

class ContaCorrente(Conta):
    def sacar(self, quant,conta):
        if isinstance(conta, ContaPoupanca):
            if self._saldo - quant < 500 : # A conta é Poupança, entao o Banco esta dando 500 a mais pra sacar
                print("Sua conta é poupanca, o seu limite de saque ja foi atingido!")
                return False
            self._saldo -= quant
            return self.saldo
        elif isinstance(conta, ContaCorrente):
            if self._saldo - quant < 0 :
                print("Nao foi possivel sacar esse valor")
                return False
            self._saldo -= quant
            return self.saldo

############################################################################
    
class Pessoa(ABC):

    def __init__(self,nome,cpf):
        self._nome = nome
        self._cpf = cpf

    def __str__(self):
        return f"\n     => Nome {self._nome}\n     => CPF {self._cpf}"

    @property
    @abstractmethod
    def nome(self) -> str:
        pass

    @property
    @abstractmethod
    def cpf(self) -> str:
        pass

class Cliente(Pessoa):

    def __init__(self, nome, cpf, senha, conta=None):
        super().__init__(nome, cpf)
        self._senha = senha
        self._conta = conta

    def __str__(self):
        return f"{super().__str__()}\n\n   Conta: {self._conta}\n"

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def senha(self) -> int:
        return self._senha

    @property
    def conta(self):
        return self._conta
    
    @conta.setter
    def conta(self,conta):
        self._conta = conta

############################################################################

class Banco:

    def __init__(self):
        self.bancos_cadastrados = []

    def __str__(self):
        output = "Informações do Banco:\n"
        output += "Bancos Cadastrados:\n"
        for banco in self.bancos_cadastrados:
            output += f"   Cliente: {banco.cliente.nome}\n   Agência: {banco.agencia}\n\n"
        return output

    def adicionar_banco(self, novo_banco):
        self.bancos_cadastrados.append(novo_banco)

    def mostrar_bancos(self):
        for banco in self.bancos_cadastrados:
            print(banco)

class BancoUsuario:

    def __init__(self, agencia : str | None, cliente: Cliente | None):
        self._agencia = agencia
        self._cliente = cliente

    def __str__(self):
        return f"Cliente: {self.cliente}\nAgência: {self.agencia}\n"

    @property
    def agencia(self) -> str | None:
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

