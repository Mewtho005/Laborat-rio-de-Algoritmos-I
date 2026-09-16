numero = int(input("Digite um número inteiro positivo: "))

while numero < 0:
    numero = int(input("Número inválido! Digite outro número: "))

while numero >= 0:
    print(numero)
    numero = numero - 1
