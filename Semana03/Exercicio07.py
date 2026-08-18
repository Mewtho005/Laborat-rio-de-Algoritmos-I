#Peça o valor de uma compra.
#Se o valor for maior que R$100, aplique 10% de desconto.
#Senão, não aplique desconto.

valordacompra = float(input("Preço dog?"))
if valordacompra > 100:
    valorfinal = valordacompra * 0.90
    print("Descontou, agr paga isso: ", valorfinal)
else:
    print("Deu isso tudo dog: ", valordacompra)
