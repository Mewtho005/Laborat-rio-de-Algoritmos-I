def main():
    vetor = []

    for i in range(30):
        numero = int(input("Digite um número: "))

        if numero % 4 == 0:
            vetor.append(numero)
        else:
            vetor.append(4)
            print("Erro! Número substituído por 4.")

    print("Vetor:", vetor)


main()
