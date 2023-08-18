nums = []

a = int(input("Digite o primeiro número: "))
nums.append(a)

b = int(input("Digite o segundo número: "))
nums.append(b)

c = int(input("Digite o terceiro número: "))
nums.append(c)

nums.sort()

print(nums)
print(f"Mediana: {nums[1]}")