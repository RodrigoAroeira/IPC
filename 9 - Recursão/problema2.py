def power(k, n):
    # recursivo
    #nao usar ** ou pow
    if n == 0:
        return 1
    elif n == 1:
        return k
    else: 
        return k * power(k, n-1)
    
def power2(k, n):
    resultado = 1
    if n == 0:
        return 1
    else:
        for i in range(n):
            resultado *= k
        return resultado

n = int(input()); m = int(input())
print(power(n,m))

#fezes 33