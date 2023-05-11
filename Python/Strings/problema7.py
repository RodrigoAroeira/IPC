palavra = input() 
chave = int(input()) 

def cifra(palavra, chave, lc = []): # método 1
    for char in palavra.lower(): 
        if ord(char.lower()) + chave <= 122:
            lc.append(chr(ord(char.lower()) + chave)) 
        else: 
            lc.append(chr(ord(char.lower()) + chave - 26)) 
    x = "".join(lc) 
    print("Resultado: " + x) 
# cifra(palavra, chave) 

def cifra_cesar(palavra, chave): #método 2
    criptografado = ""
    for letra in palavra:
        if ord(letra) + chave <= 122:
            nova_letra = chr((ord(letra) + chave))
        else:
            nova_letra = chr((ord(letra) + chave) - 26)
        criptografado += nova_letra
    print("Resultado:", criptografado)
cifra_cesar(palavra, chave)