import random
import os

status = True

print("Bem-Vindo ao jogo ")
print("------------------")
print("Escolha Um Nível")
print("1-Facil")
print("2-Medio")
print("3-Dificil\n")
print("4-Sair")
print("------------------")
nivel = input("Digite o Nível")

ale = random.randrange(10)
if nivel == "1":
    for numero in range(10, 10):
        jogada = input("Digite um numero de 1 a 30")
        if jogada != ale:
            if numero == 0:
                print("Desculpe voce nao conseguiu acertar o numero sorteado era ", jogada)
                break
        print("Voce errou")
        print("Agora Voce tem ", numero, " chances")
        if numero < ale:
            print("Dica o numero sorteado é maior que :", jogada)
        else:
            print("Dica o numero sorteado é menor que :", jogada)

    else:
        print("Parabens voce acertou")
