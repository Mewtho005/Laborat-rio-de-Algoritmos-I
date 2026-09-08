secreto = 50
tentativa = 0
quantidade = 0

while quantidade != secreto:

    quantidade = int(input("Digite um número: "))

    tentativa = tentativa + 1

    if quantidade < secreto:
        print("Tente um número maior!")

    elif quantidade > secreto:
        print("Tente um número menor!")

print("Parabéns! Você encontrou a embalagem premiada!")
print("Tentativas:", tentativa)
