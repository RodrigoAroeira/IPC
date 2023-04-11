start = int(input("Digite o valor do início do intervalo: "))
end = int(input("Digite o valor do final do intervalo: "))

pares = 0

for i in range(start, end+1):
    if i % 2 == 0:
        pares += 1
print (f"Quantidade de números pares: {pares}")