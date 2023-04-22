def mdc(n, m):
    nums = [n, m]
    nums.sort()
    divs = []
    for i in range(1, max(nums)):
        if n % i == 0 and m % i == 0:
            divs.append(i)
    return max(divs)

n = int(input("Digite o primeiro número: "))
m = int(input("Digite o segundo número: "))
print("mdc:", mdc(n, m))