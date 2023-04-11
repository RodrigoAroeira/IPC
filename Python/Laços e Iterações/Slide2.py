def fatorial():
    produto = 1
    x = int(input("Insira um número inteiro: "))
    for i in range(1, x+1):
        produto *= i
    print (f"O valor de {x}! é:\n> {produto}")
    return produto

fatorial()