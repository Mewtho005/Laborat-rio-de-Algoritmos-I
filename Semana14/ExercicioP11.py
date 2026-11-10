def verificar():
    lotes = []

    for i in range(5):
        codigo = int(input("Digite o código do lote: "))
        lotes.append(codigo)

    distintos = True

    for i in range(5):
        for j in range(i + 1, 5):
            if lotes[i] == lotes[j]:
                distintos = False

    if distintos:
        print("Distintos")
    else:
        print("Há duplicatas")

verificar()
