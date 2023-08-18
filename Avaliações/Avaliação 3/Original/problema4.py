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

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(busca_binaria(lista, 9))