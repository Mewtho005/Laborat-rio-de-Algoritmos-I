#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde  h corresponde a altura): 
#Homens: (72.7 ∗ h) − 58
#Mulheres: (62, 1 ∗ h) − 44, 7


altura = float(input("Digite sua altura: "))
sexo = (input("Digite seu sexo: H ou M: ")).upper()

if sexo == "H":
    peso_homem = 72.7 * altura - 58
    print("Peso ideal", peso_homem)
if sexo == "M":
    peso_muie = 62.1 * altura - 44.7
    print("Peso ideal", peso_muie)
  
