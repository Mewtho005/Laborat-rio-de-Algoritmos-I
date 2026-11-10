def cadastrar():
    etiquetas = []

    while len(etiquetas) < 15:
        codigo = int(input("Digite o código da etiqueta: "))

        repetido = False

        for i in range(len(etiquetas)):
            if etiquetas[i] == codigo:
                repetido = True

        if repetido:
            print("Código repetido! Digite outro.")
        else:
            etiquetas.append(codigo)
            print("Código cadastrado!")

    print("Etiquetas cadastradas:", etiquetas)

cadastrar()
