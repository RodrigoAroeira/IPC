nums = []
pares = []
odd = []

# for i in range(5):
#     nums.append(int(input()))
[nums.append(int(input())) for i in range(5)]

# for num in nums:
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         odd.append(num)

[pares.append(num) if num % 2 == 0 else odd.append(num) for num in nums]

print(f"{nums}\n{pares}\n{odd}")