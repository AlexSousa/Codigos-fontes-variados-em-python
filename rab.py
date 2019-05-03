import os
import random

ale = random.randrange(30)
for num in range(10, 0, -1):

    while True:
        try:
            numero = int(input("digite"))
            if not 0 <= numero <= 10:
                raise ValueError("Nota fora do range permitido")
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break

    print(numero)


    if numero == ale:
        print("Voce Acertou o numero sorteado era ", ale)
        break
    else:
        print("voce errou agora voce tem ", num, " tentativas")
        if numero > ale:
            print("o numero è menor que ", numero)
        else:
            print("o numero é maior que ", numero)
