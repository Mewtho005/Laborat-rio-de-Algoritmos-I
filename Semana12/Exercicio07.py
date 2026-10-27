def somaimposto(taxaimposto, custo):
    imposto = custo * (taxaimposto / 100)
    custofinal = custo + imposto
    
    return custofinal

def main():
    custo = float(input("Digite o custo do item: "))
    taxa = float(input("Digite a taxa de imposto (%): "))
    
    valorfinal = somaimposto(taxa, custo)
    
    print("Valor com imposto: R$", valorfinal)

main()
