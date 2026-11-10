def rendimento():
    lotes = []
    rendimento = 0.18

    for i in range(6):
        kg = float(input("Digite os kg de azeitona: "))
        lotes.append(kg)

    for i in range(6):
        litros = lotes[i] * rendimento
        print("Lote", i + 1, ":", litros, "litros")

rendimento()
