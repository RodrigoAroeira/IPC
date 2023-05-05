palavra = input()

if palavra.lower() == palavra[::-1].lower():
    print("É palíndromo")
else:
    print("Não é palíndromo")