pacotes = int(input("Digite a quantidade total de pacotes: "))
caixas = int(input("Digite a quantidade de caixas disponíveis: "))

quantidade = pacotes // caixas
sobra = pacotes % caixas

print("Pacotes em cada caixa:", quantidade)
print("Pacotes sobrando:", sobra)
