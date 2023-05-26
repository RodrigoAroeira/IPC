#criar duas funções: compactar_strings e intercalar_strings
#compactar_strings: recebe duas strings (com tamanhos que podem ser diferentes) e retorna pares de strings em sublistas com a i-ésima letra de cada string
#intercalar_strings: recebe duas strings e retorna uma string com as letras intercaladas

# def intercalar_strings(string1, string2, intercalado = ""):
#     if len(string1) > len(string2):
#         for i in range(len(string1)):
#             if i < len(string2):
#                 intercalado += string1[i] + string2[i]
#             else:
#                 intercalado += string1[i]
#     else:
#         for i in range(len(string2)):
#             if i < len(string1):
#                 intercalado += string1[i] + string2[i]
#             else:
#                 intercalado += string2[i]
#     return intercalado

# print(intercalar_strings("Tpo", "oCder")) # output deve ser TopCoder

def compactar_strings(string1, string2, compactado = []):
    if len(string1) > len(string2):
        string2 += " " * (len(string1) - len(string2))
    else:
        string1 += " " * (len(string2) - len(string1))
    for i in range(len(string1)):
        compactado.append([string1[i], string2[i]])
    return compactado

def intercalar_strings(string1, string2, intercalado = ''):
    strings = [string1, string2]; maior = len(max(strings)); menor = len(min(strings))
    if len(string1) > len(string2):
        for i in range(string1):
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

s1 = input("Digite a primeira palavra: ")
s2 = input("Digite a segunda palavra: ")
print("Compactação:", compactar_strings(s1, s2))
print("Combinação:", intercalar_strings(s1, s2))