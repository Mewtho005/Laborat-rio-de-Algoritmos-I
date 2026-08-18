#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina
#e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

preco_litro = float(input("Digite o preço do litro: R$"))
valor_pagamento = float(input("Digite o valor que deseja abastecer: R$"))
litros = valor_pagamento / preco_litro


print("Quantidade de litros abastecidos:", litros, "L")
