from classes import *

def cadastrar_cliente(nome, cpf, numero_conta, senha):
    conta = ContaPoupanca("123", str(numero_conta), 0)
    pessoa = Cliente(nome, cpf, senha, conta)
    return pessoa

while 1:
    op = int(input(
        "Insira uma opcao: \n"
        "1 - Abrir um cadastro no banco\n"
        "2 - Entrar no Banco\n"
        "0 - SAIR\n"
        ))

    if op == 1:

        cliente = cadastrar_cliente("Wendell", "123.456.789-10",123456, 123)
        print(f"Cliente cadastrado:\n{cliente}")

        cliente = cadastrar_cliente("William", "444.333.222-20",654321, 456)
        print(f"Cliente cadastrado:\n{cliente}")

    elif op == 2:

        nome = str(input("Digite seu nome"))
        senha = int(input("Digite sua senha"))

        if cliente.nome == nome and cliente.senha == senha:
            print("BEM VINDO ", cliente.nome)

            op2 = input(
                "1 - Cadastrar uma conta corrente\n \
                2 - Cadastrar uma conta poupanca\n \
                3 - Depositar valor\n \
                4 - Sacar valor\n \
                5 - Mostrar todos seus dados\n"
            )
        else: 
            print("Usuario inexistente ou senha incorreta")

    elif op == 3:
        ...
    elif op == 4:
        ...
    elif op == 5:
        ...
    elif op == 6:
        ...
    elif op == 0:
        break

    else:
        print("Insira uma opção correta!")






banco_bradesco = Banco()
pessoa1 = Cliente("Wendell", "123.456.789-10")

banco_itau = Banco()
pessoa2 = Cliente("William", "444.333.222-20")

conta_usuario_1 = ContaPoupanca("123", "111111", 1000)
conta_usuario_1.depositar(100)
print("SALDO: ", conta_usuario_1.saldo)
conta_usuario_1.sacar(200)
print("SALDO: ", conta_usuario_1.saldo)
conta_usuario_1.pessoa = pessoa1

conta_usuario_2 = ContaCorrente("456", "222222", 2000)
conta_usuario_2.depositar(100)
print("SALDO: ", conta_usuario_2.saldo)
conta_usuario_2.sacar(200)
print("SALDO: ", conta_usuario_2.saldo)
conta_usuario_2.pessoa = pessoa1

conta_usuario_1.pessoa = pessoa1
banco_bradesco.adicionar_conta_cadastrada(conta_usuario_1)
banco_bradesco.agencia = conta_usuario_1.agencia
banco_bradesco.cliente = pessoa1
banco_bradesco.adicionar_conta_cadastrada(conta_usuario_2)
banco_bradesco.agencia = conta_usuario_2.agencia
banco_bradesco.cliente = pessoa1

conta_usuario_3 = ContaPoupanca("223", "555555", 10000)
conta_usuario_3.depositar(300)
print("SALDO: ", conta_usuario_3.saldo)
conta_usuario_3.sacar(50)
print("SALDO: ", conta_usuario_3.saldo)
conta_usuario_3.pessoa = pessoa2

conta_usuario_4 = ContaCorrente("888", "777777", 45000)
conta_usuario_4.depositar(500)
print("SALDO: ", conta_usuario_4.saldo)
conta_usuario_4.sacar(400)
print("SALDO: ", conta_usuario_4.saldo)
conta_usuario_4.pessoa = pessoa2

banco_itau.adicionar_conta_cadastrada(conta_usuario_3)
banco_itau.agencia = conta_usuario_3.agencia
banco_itau.cliente = pessoa2

banco_itau.adicionar_conta_cadastrada(conta_usuario_4)
banco_itau.agencia = conta_usuario_4.agencia
banco_itau.cliente = pessoa2

print()
print("X" * 50)
print()

cadastro_de_conta = Banco()

cadastro_de_conta.adicionar_conta_cadastrada(banco_bradesco)
cadastro_de_conta.adicionar_conta_cadastrada(banco_itau)

lista_de_bancos = [cadastro_de_conta]

for banco in lista_de_bancos:
    print(banco)