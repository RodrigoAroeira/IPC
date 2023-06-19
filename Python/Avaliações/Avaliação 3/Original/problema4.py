def busca_binaria(lista, elemento):
    if elemento not in lista:
        return False
    if len(lista) == 0:
        return False
    if len(lista) % 2 == 0:
        meio = len(lista) // 2
    else:
        meio = (len(lista) // 2) + 1
    if lista[meio] == elemento:
        return True
    else:
        lista.remove(lista[meio])
        return busca_binaria(lista, elemento)

