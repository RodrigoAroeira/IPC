def imprime_naturais_impares(n):
    if n > 0:
        if n % 2 == 1:
            print(n)
        imprime_naturais_impares(n-1)

imprime_naturais_impares(n=int(input()))

    