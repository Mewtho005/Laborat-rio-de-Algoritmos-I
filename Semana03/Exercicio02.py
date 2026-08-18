#Faça um algoritmo que leia dois números distintos e apresente-os em ordem crescente.

numero1 = float(input())
numero2 = float(input())

if numero1 < numero2:
    print(numero1, numero2)
else:
    print(numero2, numero1)
