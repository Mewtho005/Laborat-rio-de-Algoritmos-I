def verificar_lote():
    lotes = [101, 202, 303, 404, 505]

    codigo = int(input("Digite o código do lote: "))

    encontrado = False

    for lote in lotes:
        if lote == codigo:
            encontrado = True

    if encontrado:
        print("Encontrado")
    else:
        print("Não encontrado")


verificar_lote()
