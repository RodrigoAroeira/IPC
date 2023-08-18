letras = {} 
palavra = input()

for letra in palavra:
    letras[letra] = letras.get(letra, 0) + 1

maior = max(letras, key = letras.get)

print(maior)
