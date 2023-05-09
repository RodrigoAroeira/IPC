lista = []

for i in range(5):
    lista.append(float(input()))

lista.sort()
lista = lista[1:-1]


def med(lista):
    return sum(lista)/len(lista)

print(f"Média: {med(lista):.2f}")
