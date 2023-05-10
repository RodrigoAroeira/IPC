def avg(lista):
    return sum(lista)/len(lista)

lista =[]
for i in range(12):
    lista.append(float(input()))

print(lista)
lista.sort()
print(lista)

print(f"Média: {avg(lista):.2f}")

x = len(lista)//2

for i in lista[x:]:
    if i > avg(lista):
        print(i)