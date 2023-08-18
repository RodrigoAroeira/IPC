def eh_triangular(n):
    if n < 1:
        return False
    
    # Encontrar o maior número natural consecutivo cujo cubo é menor ou igual a n
    candidato = 1
    while candidato * (candidato + 1) * (candidato + 2) < n:
        candidato += 1
    
    # Verificar se o produto dos três números consecutivos é igual a n
    return candidato * (candidato + 1) * (candidato + 2) == n

# Teste a função com alguns exemplos
print(eh_triangular(120))  # True
print(eh_triangular(2730))  # True
print(eh_triangular(10))   # False
