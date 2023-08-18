num = int(input("Digite um número: "))
div = []

[div.append(i) if num % i == 0 else 0 for i in range (1,num)]

# for i in range(1, num):
#     if num % i == 0:
#        div.append(i)

print("Resultado:", sum(div))