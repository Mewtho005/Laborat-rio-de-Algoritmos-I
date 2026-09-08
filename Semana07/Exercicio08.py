empresa = 5000
concorrente = 8000
meses = 0

while empresa < concorrente:
    empresa = empresa * 1.05
    concorrente = concorrente * 1.01
    meses = meses + 1

print("Meses necessários:", meses)
print("Produção da empresa:", int(empresa))
print("Produção da concorrente:", int(concorrente))
