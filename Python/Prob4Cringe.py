numero = int(input("Digite um número inteiro: "))
invertido = 0

while numero > 0:
    resto = numero % 10
    print(f"resto: {resto}")
    invertido = invertido * 10 + resto
    print(f"invertido: {invertido}")
    numero = numero // 10
    print(f"numero: {numero}")
    
print("O número invertido é:", invertido)
