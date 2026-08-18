#Leia um número fornecido pelo usuário. Se esse número for positivo, apresente o dobro do valor digitado. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

numero = float(input("Seu numero é:"))


if numero >= 1:
    print(numero * 2)
else:
    print("Numero invalido")
