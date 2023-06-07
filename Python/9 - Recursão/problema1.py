# Implemente uma função recursiva chamada soma que receba dois parâmetros m e n e retorna o valor
# da soma conforme a definição acima. Em seguida, escreva um programa para testar essa função. O
# programa deve ler do usuário os valores de m e n, chamar a função e imprimir na tela o valor retornado pela função.

def soma(m, n):
    #somatorio de k=m até n de k = m se m = n, se n>m k = m + somatorio de k = m+1 até n de k
    if n == m:
        return m
    elif n > m:
        return m + soma(m+1, n)
    
