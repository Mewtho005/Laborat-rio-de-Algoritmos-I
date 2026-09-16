opc = 0
total_gas = 0
total_diesel = 0

while opc != 2:
    print("1. Vender Combustível")
    print("2. Sair")
    opc = int(input("Digite sua opção: "))

    if opc == 1:
        print("1. Gasolina: R$ 6.89")
        print("2. Diesel: R$ 4.80")

        combustivel = int(input("Qual combustível chefe? "))
        litros = float(input("E quantos litros você quer? "))

        valor = 0

        if combustivel == 1:
            valor = litros * 6.89
            total_gas = total_gas + litros

        elif combustivel == 2:
            valor = litros * 4.80
            total_diesel = total_diesel + litros

        else:
            print("Opção inválida")

        if valor > 0:
            print("Total a pagar: R$", valor)

            pagamento = float(input("Valor do pagamento? "))

            if pagamento >= valor:
                troco = pagamento - valor
                print("Troco: R$", troco)
            else:
                print("Valor insuficiente")

    elif opc == 2:
        print("Saindo...")

    else:
        print("Opção inválida")
