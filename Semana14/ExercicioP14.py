import random

def confronto():
    colheita = []
    pragas = random.sample(range(1, 101), 5)

    protegidos = 0
    perdidos = 0

    for i in range(5):
        forca = float(input("Digite a força da equipe: "))
        colheita.append(forca)

    print("\nForças da equipe:", colheita)
    print("Forças das pragas:", pragas)

    for i in range(5):
        if colheita[i] > pragas[i]:
            print("Lote", i + 1, "- Protegido")
            protegidos += 1
        else:
            print("Lote", i + 1, "- Praga resistiu")
            perdidos += 1

    print("\nPlacar final:")
    print("Lotes protegidos:", protegidos)
    print("Lotes perdidos:", perdidos)

confronto()
