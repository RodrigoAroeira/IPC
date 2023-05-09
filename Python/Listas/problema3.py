nums = []
pares = []
odd = []

for i in range(5):
    nums.append(int(input()))

for num in nums:
    if num % 2 == 0:
        pares.append(num)
    else:
        odd.append(num)


print(f"{nums}\n{pares}\n{odd}")