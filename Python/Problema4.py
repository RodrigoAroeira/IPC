numero = int(input("Digite um número inteiro: "))
invertido = 0
while numero > 0:
    resto = numero % 10
    invertido = invertido * 10 + resto
    numero = numero // 10
print("O número invertido é: ", invertido)
