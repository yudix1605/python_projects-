import random


def escolher_computador():
    return random.choice(["pedra", "papel", "tesoura"])


def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        return "jogador"
    else:
        return "computador"


def jogo():
    jogador_pontos = 0
    computador_pontos = 0

    while True:
        print("\nEscolha: pedra, papel ou tesoura (ou 'sair')")

        jogador = input("Sua escolha: ").lower()
        print("'" + jogador + "'")
        if jogador == "sair":
            print("Jogo encerrado!")
            break

        if not jogador in ["pedra", "papel", "tesoura"]:
            print("Jogada inválida, tente novamente!")
            continue  # aqui o loop volta, mas não trava

        computador = escolher_computador()
        print(f"Computador escolheu: {computador}")

        resultado = verificar_vencedor(jogador, computador)

        if resultado == "empate":
            print("Empate!")
        elif resultado == "jogador":
            print("Você ganhou!")
            jogador_pontos += 1
        else:
            print("A máquina venceu!")
            computador_pontos += 1

        print(f"Placar: Você {jogador_pontos} x {computador_pontos} Máquina")


jogo()