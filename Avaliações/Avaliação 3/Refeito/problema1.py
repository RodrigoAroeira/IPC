def tamanho_medio_palavras(path):
    with open(path, 'r') as arquivo:
        text = arquivo.read()
        #tirar simbolos
        simbolos = r",.;:!?"
        palavras = text.strip().split() 
        palavras_processadas = []
        for palavra in palavras:
            for simbolo in simbolos:
                if simbolo in palavra:
                    palavra = palavra.replace(simbolo, '')
            palavras_processadas.append(palavra)
        return sum(len(palavra) for palavra in palavras_processadas) / len(palavras_processadas)

print(tamanho_medio_palavras('C:\\Users\\Rodrigo\\OneDrive - \
Universidade Federal de Minas Gerais\\Documentos\\Programação\\IPC\\Python\\\
Avaliações\\Avaliação 3\\taylorswift.txt'))