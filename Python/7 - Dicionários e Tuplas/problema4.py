numeros = {}
n=0
while n != -1:
    inp = input()
    n = int(inp if inp != '' else -1)
    if n == -1:
        break
    numeros[n] = numeros.get(n, 0) + 1

maior = max(numeros, key = numeros.get)
print(maior)