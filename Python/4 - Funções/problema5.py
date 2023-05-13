def media(n1, n2, n3, letra):
    aritmetica = (n1 + n2 + n3) / 3
    ponderada = (n1 * 5 + n2 * 3 + n3 * 2) / 10
    if letra.upper() == 'A':
        return aritmetica
    elif letra.upper() == 'P':
        return ponderada