with open("texto.txt", "r") as arquivo:
    arquivo.readline()
    maior = 0
    for linha in arquivo:
        for palavra in linha.split():
            if len(palavra) > maior:
                maior = len(palavra)
                palavra_maior = palavra

print(palavra_maior)
print(maior)