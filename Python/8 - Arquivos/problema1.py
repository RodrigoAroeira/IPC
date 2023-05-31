#achar a linha com maior numero de caracteres

with open("texto.txt", "r") as arquivo:
    arquivo.readline()
    maior = 0
    for linha in arquivo:
        if len(linha) > maior:
            maior = len(linha)
            linha_maior = linha
    print(linha_maior)
        