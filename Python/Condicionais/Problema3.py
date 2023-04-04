nomes = ["primeiro", "segundo", "terceiro"]
pontos = []

for i in range(3):
    cesta = float(input(f"Digite o {nomes[i]} arremesso: "))
    if cesta == -1:
        pontos.append(1)
    else:
        pontos.append(3 if cesta > 7.24 else 2)

pont = sum(pontos)
print(f"Pontuação: {pont}")