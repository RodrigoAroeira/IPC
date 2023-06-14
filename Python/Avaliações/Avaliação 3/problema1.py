def tamanho_medio_palavras(path):
    with open(path, 'r') as arquivo:
        text = arquivo.read()
        #tirar simbolos
        simbolos = r"!@#$%¨&*()_+{}^:<>?/.,;~´`[]-='"
        palavras = text.split()
        for palavra in palavras:
            for simbolo in simbolos:
                if simbolo in palavra:
                   palavra.replace(simbolo, '')
        print (palavras)
        return sum(len(palavra) for palavra in palavras) / len(palavras)
    
    
print(tamanho_medio_palavras(r'C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\Avaliações\Avaliação 3\taylorswift.txt'))