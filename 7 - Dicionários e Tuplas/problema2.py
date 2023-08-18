letras = {} 
palavra = input()

for letra in palavra:
    for vogal in 'aeiou':
        if letra.lower() == vogal.lower():
            if letra not in letras:
                letras[letra] = 1
            else:
                letras[letra] += 1

maior = max(letras, key = letras.get)

print(maior)
