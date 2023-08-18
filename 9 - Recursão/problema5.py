def imprime_naturais(n):
    # imprime os n primeiros naturais a partir de 0, recursivamente
    if n == 0:
        print(n)
    else:
        return imprime_naturais(n-1), print(n)


imprime_naturais(n=int(input("Digite N: ")))