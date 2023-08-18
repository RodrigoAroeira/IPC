numeros = {}

def getn():
    inp = input()
    return int(inp if inp != '' else -1)

n=getn()

while n != -1:
    numeros[n] = numeros.get(n, 0) + 1
    n = getn()

maior = max(numeros, key = numeros.get)
print(maior)