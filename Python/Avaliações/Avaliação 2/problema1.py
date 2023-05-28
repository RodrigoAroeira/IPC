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


def compactar_strings(string1, string2, compactado = []):
    if len(string1) > len(string2):
        string2 += " " * (len(string1) - len(string2))
    else:
        string1 += " " * (len(string2) - len(string1))
    for i in range(len(string1)):
        compactado.append([string1[i], string2[i]])
    for elemento in compactado:
        if elemento[0] == " ":
            elemento[0] = ""
        if elemento[1] == " ":
            elemento[1] = ""
    return compactado

def intercalar_strings(string1, string2, intercalado = ''):
    compactado = compactar_strings(string1, string2)
    for i in range(len(compactado)//2):
        intercalado += compactado[i][0] + compactado[i][1]
    return intercalado


    # if len(string1) > len(string2):
    #     for i in range(len(string1)):
    #         if i < len(string2):
    #             intercalado += string1[i] + string2[i]
    #         else:
    #             intercalado += string1[i]
    # else:
    #     for i in range(len(string2)):
    #         if i < len(string1):
    #             intercalado += string1[i] + string2[i]
    #         else:
    #             intercalado += string2[i]
    # return intercalado

print(compactar_strings("Tpo", "oCder"))
print(intercalar_strings("Tpo", "oCder")) # output deve ser TopCoder







# s1 = input("Digite a primeira palavra: ")
# s2 = input("Digite a segunda palavra: ")
# print("Compactação:", compactar_strings(s1, s2))
# print("Combinação:", intercalar_strings(s1, s2))