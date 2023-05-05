palavra = input()
chave = int(input())

def cifra(palavra, chave, lc = []):
    for char in palavra.lower():
        lc.append(chr(ord(char.lower()) + chave))
    print("".join(lc))

cifra(palavra, chave)