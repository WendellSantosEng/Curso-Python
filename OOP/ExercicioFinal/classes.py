from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    def __str__(self):
        return f'Agencia: {self._agencia}\nNumero da Conta: {self._numero_conta}\nSaldo: {self.saldo}\n'
   
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

    @property
    def pessoa(self):
        return self._pessoa
    
    @pessoa.setter
    def pessoa(self, pessoa):
        self._pessoa = pessoa



    def depositar(self, quant):
        self._saldo += quant
        return self.saldo

    @abstractmethod
    def sacar(self, quant):
        pass
class ContaPoupanca(Conta):
    def sacar(self, quant):
        self._saldo -= quant
        return self.saldo

class ContaCorrente(Conta):
    def sacar(self, quant):
        self._saldo -= quant
        return self.saldo

############################################################################
    
class Pessoa(ABC):

    def __init__(self,nome,cpf):
        self._nome = nome
        self._cpf = cpf

    def __str__(self):
        return f"=> Nome {self._nome}\n=> CPF {self._cpf}"

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
    def conta(self) -> str:
        return self._conta


############################################################################
    

class Banco:

    def __init__(self):
        self._nome = None
        self._cpf = None
        self.cadastradas = []
        
    def adicionar_conta_cadastrada(self, conta):
        self.cadastradas.append(conta)

    def __str__(self):
        output = "Contas Cadastradas:\n"
        # print(f"\nNome: {self._nome}   CPF: {self._cpf}")
        for conta in self.cadastradas:
            output += f"{conta}\n"
        return output
    
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

