num = int(input("Digite um número: "))
div = []

for i in range(1, num):
    if num % i == 0:
       div.append(i)

print("Resultado:", sum(div))

haha