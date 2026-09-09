quantidade = int(input("Quantidade de pacotes: "))

valor_original = quantidade * 20.00

if quantidade <= 5:
    desconto = 0
elif quantidade <= 10:
    desconto = 5
elif quantidade <= 20:
    desconto = 10
else:
    desconto = 15

valor_desconto = valor_original * desconto / 100
valor_final = valor_original - valor_desconto

print(f"Valor original: R$ {valor_original}")
print(f"Percentual de desconto: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto}")
print(f"Valor final da compra: R$ {valor_final}")
