#achar a linha com maior numero de caracteres

with open("texto.txt", "r") as arquivo:
    maior = 0
    for linha in arquivo:
        if len(linha) > maior:
            maior = len(linha)
            linha_maior = linha
    print(linha_maior)
        