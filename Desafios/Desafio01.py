pontos = 0

resposta = input("Você esteve no local do crime? ")
if resposta == "sim":
    pontos = pontos + 1
else:
    pontos = pontos + 0

resposta = input("Você conhece a vítima? ")
if resposta == "sim":
    pontos = pontos + 1
else:
    pontos = pontos + 0

resposta = input("Você já teve algum desentendimento com a vítima? ")
if resposta == "sim":
    pontos = pontos + 1
else:
    pontos = pontos + 0

resposta = input("Você estava próximo do local na hora do ocorrido? ")
if resposta == "sim":
    pontos = pontos + 1
else:
    pontos = pontos + 0

resposta = input("Você tem algo que comprove sua inocência? ")
if resposta == "sim":
    pontos = pontos + 1
else:
    pontos = pontos + 0

if pontos >= 3:
    print("Pessoa suspeita.")
else:
    print("Pessoa não considerada suspeita.")
  
