num = int(input("Digite um inteiro n: "))
fib = [0, 1]

for i in range(2, num+1):
    fib.append(fib[i-1]+fib[i-2])

print(fib[num])

# fib.remove(0)

# print(fib)