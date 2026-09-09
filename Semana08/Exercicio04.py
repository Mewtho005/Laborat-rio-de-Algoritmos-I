chimarraos = int(input("Quantos chimarrões prepara por dia? "))

consumo = chimarraos * 40 * 30

print("Consumo mensal:", consumo, "gramas")

if consumo > 3000:
    print("Grande consumidor de erva-mate")
else:
    print("Consumidor moderado de erva-mate")
