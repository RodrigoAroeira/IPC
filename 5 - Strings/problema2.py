# string = input()

# for i in range(len(string)):
#     if string[i] == string[i+1]:
#         string[i+1] = string[i+1].upper()
#         string[i] = ''
        

# print(string)

# def repeatedChar(texto):
#     # Inicializa uma variável para armazenar o texto com as substituições
#     novo_texto = texto[0]  # adiciona o primeiro caractere ao novo texto
#     ultima_letra = texto[0]  # armazena a última letra adicionada
    
#     # Itera sobre os caracteres do texto, verificando se há repetição
#     for i in range(1, len(texto)):
#         if texto[i] == ultima_letra and texto[i].isalpha():
#             # Substitui por uma única ocorrência em maiúscula
#             novo_texto = novo_texto[:-1] + texto[i].upper()
#         else:
#             novo_texto += texto[i]
#             ultima_letra = texto[i]
    
#     return novo_texto

# print(repeatedChar('Aaararraa'))

str = [*input()]

for i in range(len(str)-1):
    if str[i] == str[i+1]:
        str[i+1] = str[i+1].upper()
        str[i] = ''
print(''.join(str))