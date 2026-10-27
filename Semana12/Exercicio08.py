def converterhora(hora, minuto):
    if hora == 0:
        novahora = 12
        periodo = "A.M."
    elif hora < 12:
        novahora = hora
        periodo = "A.M."
    elif hora == 12:
        novahora = 12
        periodo = "P.M."
    else:
        novahora = hora - 12
        periodo = "P.M."
    
    return novahora, minuto, periodo

def mostrarhora(hora, minuto, periodo):
    print(hora, ":", minuto, periodo)

def main():
    hora = int(input("Digite a hora (0-23): "))
    minuto = int(input("Digite os minutos (0-59): "))
    
    if hora >= 0 and hora <= 23 and minuto >= 0 and minuto <= 59:
        h, m, p = converterhora(hora, minuto)
        mostrarhora(h, m, p)
    else:
        print("Horario invalido")

main()
