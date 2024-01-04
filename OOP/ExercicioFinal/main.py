from classes import *

banco_global = Banco()

def estabelecer_dados(usuario: Cliente, banco):
    novo_banco = BancoUsuario(agencia=usuario.conta.agencia, cliente=usuario)
    banco.adicionar_banco(novo_banco)
    print(banco)

def cadastrar_cliente(nome, cpf, numero_conta, senha):
    cliente = Cliente(nome, cpf, senha)
    return cliente

def cadastrar_conta_poupanca(usuario, agencia, numero_conta, saldo):
    conta = ContaPoupanca(agencia, numero_conta, saldo)
    usuario.conta = conta
    estabelecer_dados(usuario,banco_global)

def cadastrar_conta_corrente(usuario, agencia, numero_conta, saldo):
    conta = ContaCorrente(agencia, numero_conta, saldo)
    usuario.conta = conta
    estabelecer_dados(usuario,banco_global)

def depositar_valor(usuario):
    valor = int(input("Qual o valor que sera depositado? "))
    saldo_atual = usuario.conta.depositar(valor)
    print("Valor depositado !")
    print("Seu saldo agora é: " , usuario.conta.saldo)

def sacar_valor(usuario):
    msg = "Qual o valor que sera sacado (lembre-se, voce possui",usuario.conta.saldo,")? "
    valor = int(input(msg))
    saldo_atual = usuario.conta.sacar(valor,usuario.conta)
    if saldo_atual:
        print("Valor sacado!")
        print("Seu saldo agora é: " , usuario.conta.saldo)

def dentro_do_banco(usuario,banco):

    while True:

        op2 = int(input(
                "1 - Cadastrar uma conta corrente\n"
                "2 - Cadastrar uma conta poupanca\n"
                "3 - Depositar valor\n"
                "4 - Sacar valor\n"
                "5 - Mostrar todos seus dados\n\n"
                "0 - Voltar ao menu anterior\n"
            ))
        
        if op2 == 1:
            if usuario.conta:
                print("Voce ja possui uma conta")
            else:
                cadastrar_conta_corrente(usuario, "123", "222222", 2000)
                print("Conta cadastrada")
        elif op2 == 2:
            if usuario.conta:
                print("Voce ja possui uma conta")
            else:
                cadastrar_conta_poupanca(usuario, "123", "111111", 1000)
                print("Conta cadastrada")
        elif op2 == 3:
            depositar_valor(usuario)
        elif op2 == 4:
            sacar_valor(usuario)
        elif op2 == 5:
            for bank in banco.bancos_cadastrados:
                print(bank)
        else:
            print("\nUsuario inexistente ou senha incorreta")
            break
    
list_cliente = []

while 1:

    op = int(input(
        "Insira uma opcao: \n"
        "1 - Abrir um cadastro no banco\n"
        "2 - Entrar no Banco\n"
        "0 - SAIR\n"
        ))

    if op == 1:
        #cadastro automatico, para poupar tempo

        cliente = cadastrar_cliente("User1", "123.456.789-10",123456, 123)
        list_cliente.append(cliente)

        cliente2 = cadastrar_cliente("User2", "444.333.222-20",654321, 456)
        list_cliente.append(cliente2)

    elif op == 2:

        nome = str(input("Digite seu nome: "))
        senha = int(input("Digite sua senha: "))

        for usuario in list_cliente:

            if usuario.nome == nome and usuario.senha == senha:
                print("BEM VINDO ", usuario.nome)

                dentro_do_banco(usuario,banco_global)
        
    elif op == 0:
        break

    else:
        print("Insira uma opção correta!")