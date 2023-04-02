num = int(input("Digite um inteiro de 4 algarismos: "))

num_str = str(num)
invert_str = num_str[::-1]
invert = int(invert_str)

print(f"O número invertido é: {invert}")