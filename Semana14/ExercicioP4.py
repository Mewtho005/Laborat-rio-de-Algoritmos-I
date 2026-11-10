def producao():
    arvores = []

    for i in range(5):
        valor = int(input("Digite a produção da árvore: "))
        arvores.append(valor)

    maior = arvores[0]
    menor = arvores[0]
    pos_maior = 0
    pos_menor = 0

    for i in range(5):
        if arvores[i] > maior:
            maior = arvores[i]
            pos_maior = i

        if arvores[i] < menor:
            menor = arvores[i]
            pos_menor = i

    print("Maior produção:", maior, "Árvore:", pos_maior + 1)
    print("Menor produção:", menor, "Árvore:", pos_menor + 1)

producao()
