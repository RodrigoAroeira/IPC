def power(k, n):
    #nao usar ** ou pow ou power
    if n == 0:
        return 1
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