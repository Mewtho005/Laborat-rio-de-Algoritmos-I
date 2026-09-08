total = 0
maior = -1
menor = 999999
dia = 1
dia_maior = 0
dia_menor = 0

while dia <= 7:
    producao = float(input("Digite a produção do dia {dia} (kg): "))

    total += producao

    if producao > maior:
        maior = producao
        dia_maior = dia

    if producao < menor:
        menor = producao
        dia_menor = dia

    dia += 1

media = total / 7

print("Total produzido:", total, "kg")
print("Dia da maior produção:", dia_maior)
print("Dia da menor produção:", dia_menor)
print("Média diária:", media, "kg")
