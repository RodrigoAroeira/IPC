numeros = {}
n=0
while n != -1:
    n = int(input())
    if n == -1:
        break
    numeros[n] = numeros.get(n, 0) + 1

maior = max(numeros, key = numeros.get)
print(maior)