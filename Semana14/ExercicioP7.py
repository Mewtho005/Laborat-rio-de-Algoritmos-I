import random

def gerar_lotes():
    lotes = []

    for i in range(10):
        numero = random.randint(1, 100)
        lotes.append(numero)

    print("Todos os lotes:", lotes)
    print("IDs pares:")

    for i in range(10):
        if lotes[i] % 2 == 0:
            print(lotes[i])

gerar_lotes()
