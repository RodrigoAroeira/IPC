numeros = [] 
nomes = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]

for i in range(len(nomes)):
    num = int(input(f"Digite o {nomes[i]} inteiro: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

div3 = 0
for num in numeros:
    if num % 3 == 0:
        div3 += 1

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Quantidade de divisíveis por 3: {div3}")