nums=[]
divs=[]
n = int(input("Digite o primeiro número: "))
nums.append(n)
m = int(input("Digite o segundo número: "))
nums.append(m)
nums.sort()

for i in range(1, max(nums)):
    if n % i == 0 and m % i == 0:
        divs.append(i)
print("mdc:", max(divs))
