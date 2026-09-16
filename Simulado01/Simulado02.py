ele_a = 0
ele_b = 0
ele_c = 0

morador = 1

while morador <= 10:
    elevador = input("Entre (A B C) Qual elevador vc mais usa? ").upper()
    morador = morador + 1

    if elevador == "A":
        ele_a = ele_a + 1
    elif elevador == "B":
        ele_b = ele_b + 1
    elif elevador == "C":
        ele_c = ele_c + 1

perc_a = (ele_a / 10) * 100
perc_b = (ele_b / 10) * 100
perc_c = (ele_c / 10) * 100

print(ele_a, perc_a, "%")
print(ele_b, perc_b, "%")
print(ele_c, perc_c, "%")
