lista = []


while True:
    x = (int(input("Digite um número: ")))
    if x >= 0:
        lista.append(x)
        continue
    else:
        break


print(f"Soma: {sum(lista)}")