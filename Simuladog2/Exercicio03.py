def menu():
    print("1 - Inserir total de vendas")
    print("2 - Apresentar valores registrados")
    print("3 - Apresentar média e maior valor")
    print("4 - Alterar valor de um dia")
    print("5 - Sair")
    return int(input("Escolha uma opção: "))


def inserir(vendas):
    dia = int(input("Digite o dia (1 a 30): "))
    valor = float(input("Digite o total de vendas: "))

    if dia >= 1 and dia <= 30:
        vendas[dia - 1] = valor
        print("Venda registrada!")
    else:
        print("Dia inválido!")


def apresentar(vendas):
    for i in range(30):
        if vendas[i] != None:
            print("Dia", i + 1, ":", vendas[i])


def media_maior(vendas):
    soma = 0
    quantidade = 0
    maior = 0

    for i in range(30):
        if vendas[i] != None:
            soma = soma + vendas[i]
            quantidade = quantidade + 1

            if quantidade == 1 or vendas[i] > maior:
                maior = vendas[i]

    if quantidade > 0:
        print("Média:", soma / quantidade)
        print("Maior valor:", maior)
    else:
        print("Nenhuma venda registrada.")


def alterar(vendas):
    dia = int(input("Qual dia deseja alterar? "))

    if dia >= 1 and dia <= 30:
        valor = float(input("Digite o novo valor: "))
        vendas[dia - 1] = valor
        print("Valor alterado!")
    else:
        print("Dia inválido!")


def main():
    vendas = [None] * 30
    opcao = 0

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            inserir(vendas)

        elif opcao == 2:
            apresentar(vendas)

        elif opcao == 3:
            media_maior(vendas)

        elif opcao == 4:
            alterar(vendas)

        elif opcao == 5:
            print("Saindo...")

        else:
            print("Opção inválida!")


main()
