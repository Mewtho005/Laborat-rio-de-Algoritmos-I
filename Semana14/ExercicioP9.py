import random

def contar():
    lotes = []
    pares = 0
    impares = 0

    for i in range(10):
        numero = random.randint(1, 50)
        lotes.append(numero)

    for i in range(10):
        if lotes[i] % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Lotes:", lotes)
    print("Quantidade de pares:", pares)
    print("Quantidade de ímpares:", impares)

contar()
