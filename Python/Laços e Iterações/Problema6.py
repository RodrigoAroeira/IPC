par = []
odd = []

while True:
    x = (int(input("Digite um número: ")))
    if x % 2 == 0 and x > 0:
        par.append(x)
        continue
    elif x % 2 != 0 and x > 0:
        odd.append(x)
        continue
    else:
        break



print(f"Soma pares: {sum(par)}\nSoma ímpares: {sum(odd)}")