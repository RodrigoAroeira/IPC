def avg(lista):
    return sum(lista)/len(lista)

lista =[]
for i in range(12):
    lista.append(float(input()))


print(f"Média: {avg(lista):.2f}")

# for i in lista:
#     if i > avg(lista):
#         print(int(i))

[print(int(i)) for i in lista if i > avg(lista)]