def menu():
    print("\n1 - Somar dois valores")
    print("2 - Subtrair dois valores")
    print("3 - Mostrar valores")
    print("4 - Sair")
    return int(input("Escolha uma opção: "))


def somar(valor1, valor2):
    print("Resultado:", valor1 + valor2)


def subtrair(valor1, valor2):
    print("Resultado:", valor1 - valor2)


def apresentar(valor1, valor2):
    print("Primeiro valor:", valor1)
    print("Segundo valor:", valor2)


def main():
    opcao = 0
    valor1 = 0
    valor2 = 0

    while opcao != 4:
        opcao = menu()

        if opcao == 1:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            somar(valor1, valor2)

        elif opcao == 2:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
            subtrair(valor1, valor2)

        elif opcao == 3:
            apresentar(valor1, valor2)

        elif opcao == 4:
            print("Saindo...")

        else:
            print("Opção inválida!")


main()
