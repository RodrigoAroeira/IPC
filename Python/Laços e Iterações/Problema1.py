popA = int(input("Digite a população da cidade A: "))
taxaA = float(input("Digite a taxa de crescimento da população da cidade A: "))/100
popB = int(input("Digite a população da cidade B: "))
taxaB = float(input("Digite a taxa de crescimento da população da cidade B: "))/100

growA = popA * (1+taxaA)
growB = popB * (1+taxaB)

print(f"{growB/growA}")