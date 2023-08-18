def compactar_strings(s1, s2):
    tamanho_min = min(len(s1), len(s2))
    letras_compactadas = []
    for i in range(tamanho_min):
        par = [s1[i], s2[i]]
        letras_compactadas.append(par)
    for i in range(tamanho_min, len(s1)):
        par = [s1[i], '']
        letras_compactadas.append(par)
    for i in range(tamanho_min, len(s2)):
        par = ['', s2[i]]
        letras_compactadas.append(par)
    return letras_compactadas

print(compactar_strings("Tpo", "oCder"))

def intercalar_strings(s1, s2):
    pares = compactar_strings(s1, s2)
    # s = ''
    # for c1, c2 in pares:
    #     s += c1 + c2
    # return s
    return ''.join([c1 + c2 for c1, c2 in pares])

print(intercalar_strings("Tpo", "oCder"))