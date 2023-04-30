nome = input()

nome = nome.split()
sobrenome = nome[-1]
nome = nome[0:-1]
nome = " ".join(nome)

print(f"Nome formatado: {sobrenome}, {nome}")