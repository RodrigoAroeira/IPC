def tamanho_medio_palavras(path):
    with open(path, 'r') as arquivo:
        text = file.read()
        palavras = text.split()
        return sum(len(palavra) for palavra in palavras) / len(palavras)
    