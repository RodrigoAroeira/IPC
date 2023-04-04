vmax = float(input("Digite o valor da velocidade máxima: "))
vreg = float(input("Digite o valor da velocidade registrada: "))

percent = vreg / vmax

if percent <= 1:
    print("Sem Infração")
elif percent <= 1.2:
    print("Infração Média")
elif percent <= 1.5:
    print ("Infração Grave")
else:
    print("Infração Gravíssima")