nome = input()
'''
nome = input()
char = len(nome)
while char > 0:
    print(nome[:char])
    char -= 1
'''
print(*[nome[:i] for i in range(len(nome), 0, -1)], sep='\n')