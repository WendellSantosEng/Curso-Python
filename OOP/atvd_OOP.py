from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self,nome,idade,sobrenome):
        self._nome = nome
        self._idade = idade
        self._sobrenome = sobrenome

    @property
    @abstractmethod
    def nome(self) -> str: ...
        # pass

    @property
    @abstractmethod
    def idade(self) -> int: ...
        # pass

    @property
    @abstractmethod
    def sobrenome(self) -> str: ...
        # pass


class Professor(Pessoa):

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade

    @property
    def sobrenome(self) -> str:
        return self._sobrenome


class Aluno(Pessoa):

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade

    @property
    def sobrenome(self) -> str:
        return self._sobrenome


professor = Professor(nome="João", idade=40, sobrenome="Silva")

print("Nome do Professor:", professor.nome)
print("Idade do Professor:", professor.idade)
print("Sobrenome do Professor:", professor.sobrenome)

aluno = Aluno(nome="Maria", idade=22, sobrenome="Oliveira")

# Acessando as propriedades
print("Nome do Aluno:", aluno.nome)
print("Idade do Aluno:", aluno.idade)
print("Sobrenome do Aluno:", aluno.sobrenome)