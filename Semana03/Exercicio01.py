#Faça um algoritmo para calcular o salário mensal de um funcionário. Sabe-se que o funcionário recebe R$35,00 por hora, faça um algoritmo que leia o total de horas trabalhadas no mês
#e apresente o salário final. Se o salário for menor que R$1000,00 dê um aumento de R$300,00 no salário recebido, senão apresente somente o resultado da multiplicação.

salaro = float(input("Tempo de trabaio:"))

valor = salaro * 35
if valor < 1000:
    salaro_ajustado = valor + 300
    print("ajutsinho", salaro_ajustado)
else:
    print("valu", valor)
