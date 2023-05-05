nome = input()
char = len(nome)
while char > 0:
    print(nome[:char])
    char -= 1