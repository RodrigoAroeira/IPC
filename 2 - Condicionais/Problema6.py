custo = float(input("Digite o custo de fábrica: "))

if custo <= 12000:
    print(f"Custo total: {1.05*custo:.2f}")
elif custo <= 25000:
    print(f"Custo total: {1.25*custo:.2f}")
else:
    print(f"Custo total: {1.35*custo:.2f}")