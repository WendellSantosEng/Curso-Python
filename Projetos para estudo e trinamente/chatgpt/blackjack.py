import random

def criar_baralho():
    naipes = ['Espadas', 'Copas', 'Ouros', 'Paus']
    valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
    baralho = [{'valor': valor, 'naipe': naipe} for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

def calcular_pontuacao(mao):
    pontos = 0
    as_contado = 0

    for carta in mao:
        if carta['valor'] == 'Ás':
            as_contado += 1
            pontos += 11
        elif carta['valor'] in ['Valete', 'Dama', 'Rei']:
            pontos += 10
        else:
            pontos += int(carta['valor'])

    while pontos > 21 and as_contado:
        pontos -= 10
        as_contado -= 1

    return pontos

def mostrar_mao(jogador, mao):
    print()
    print(f"{jogador} mão:")
    for carta in mao:
        print(f"{carta['valor']} de {carta['naipe']}")
    print(f"Pontuação: {calcular_pontuacao(mao)}")

def jogar_blackjack():
    baralho = criar_baralho()
    mao_jogador1 = [baralho.pop(), baralho.pop()]
    mao_jogador2 = [baralho.pop(), baralho.pop()]

    while True:
        # Jogador1
        mostrar_mao('Jogador1', mao_jogador1)
        acao_jogador1 = input("Jogador1, deseja 'pedir' ou 'parar'? ").lower()

        if acao_jogador1 == 'pedir':
            mao_jogador1.append(baralho.pop())
        elif acao_jogador1 == 'parar':
            break
        else:
            print("Opção inválida. Tente novamente.")

    while calcular_pontuacao(mao_jogador2) < 17:
        mao_jogador2.append(baralho.pop())

    # Jogador2
    mostrar_mao('Jogador1', mao_jogador1)
    mostrar_mao('Jogador2', mao_jogador2)

    if calcular_pontuacao(mao_jogador2) > 21 or calcular_pontuacao(mao_jogador1) > calcular_pontuacao(mao_jogador2):
        print("Jogador1 venceu!")
    elif calcular_pontuacao(mao_jogador1) == calcular_pontuacao(mao_jogador2):
        print("Empate!")
    else:
        print("Jogador2 venceu!")

if __name__ == "__main__":
    print("Bem-vindo ao Blackjack!")
    jogar_blackjack()
