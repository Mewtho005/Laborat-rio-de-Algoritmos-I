pessoa = 1
soma = 0
maior = 0
menor = 999999
todos = 0

while pessoa <= 20:
    vezes = int(input("Quantas vezes por semana toma chimarrão? "))

    soma = soma + vezes

    if vezes > maior:
        maior = vezes

    elif vezes < menor:
        menor = vezes

    elif vezes >= 7:
        todos = todos + 1

    pessoa = pessoa + 1

media = soma / 20

print("Média:", media)
print("Maior quantidade:", maior)
print("Menor quantidade:", menor)
print("Tomam todos os dias:", todos)
