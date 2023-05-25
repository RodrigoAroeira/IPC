#criar duas funções: compactar_strings e intercalar_strings
#compactar_strings: recebe duas strings (com tamanhos que podem ser diferentes) e retorna pares de strings em sublistas com a i-ésima letra de cada string
#intercalar_strings: recebe duas strings e retorna uma string com as letras intercaladas

def compactar_strings(string1, string2, compactado = []):
    if len(string1) > len(string2):
        for i in range(len(string1)):
            if i < len(string2):
                compactado.append([string1[i], string2[i]])
            else:
                compactado.append([string1[i], ""])
    else:
        for i in range(len(string2)):
            if i < len(string1):
                compactado.append([string1[i], string2[i]])
            else:
                compactado.append(["", string2[i]])
    return compactado
# print(compactar_strings("abcgh", "def"))


# print(intercalar_strings("Tpo", "oCder")) # output = TopCoder

def intercalar_strings(string1, string2, intercalado = ""):
    if len(string1) > len(string2):
        for i in range(len(string1)):
            if i < len(string2):
                intercalado += string1[i] + string2[i]
            else:
                intercalado += string1[i]
    else:
        for i in range(len(string2)):
            if i < len(string1):
                intercalado += string1[i] + string2[i]
            else:
                intercalado += string2[i]
    return intercalado

print(intercalar_strings("Tpo", "oCder")) # output = TopCoder