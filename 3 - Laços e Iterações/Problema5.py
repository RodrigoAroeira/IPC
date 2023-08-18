start = int(input("Digite o valor do início do intervalo: "))
end = int(input("Digite o valor do final do intervalo: "))

pares = 0

for i in range(start, end+1):
    if i % 2 == 0:
        pares += 1
pares2 = (end+1 - start)
print (f"Quantidade de números pares: {pares}")
print(((pares2/2) if (pares2-1) % 2 == 1 else (pares2-1)/2))