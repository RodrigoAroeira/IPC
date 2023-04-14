popA = int(input("Digite a população da cidade A: "))
taxaA = float(input("Digite a taxa de crescimento da população da cidade A: "))/100
popB = int(input("Digite a população da cidade B: "))
taxaB = float(input("Digite a taxa de crescimento da população da cidade B: "))/100

anos = 0

while popA < popB:
    popA += popA * taxaA
    popB += popB * taxaB
    anos += 1
    
    
print(f"{anos}")