def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    if len(lista) % 2 == 0:
        meio = len(lista) // 2
    else:
        meio = (len(lista) + 1) // 2
    valor = int(input("Digite o valor a ser encontrado: "))
    while inicio <= fim:
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
        meio = (inicio + fim) // 2
    return -1