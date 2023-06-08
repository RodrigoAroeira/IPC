def imprime_naturais(n, numeros = []):
    [numeros.append(n) if n % 2 == 0 else None]
    [imprime_naturais(n-1, numeros) if n > 0 else None]
    return numeros[::-1]

n = int(input())
numeros = imprime_naturais(n)
for numero in numeros:
    print(numero)

# def imprime_naturais(n):
#     if n % 2 == 0:
#         print(n)
#     if n > 0:
#         imprime_naturais(n-1)

# n = int(input())
# imprime_naturais(n)