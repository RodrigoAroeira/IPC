import random

def busca_binaria(lista, elemento):
    meio = len(lista) // 2
    if elemento not in lista:
        return False
    if len(lista) == 0:
        return False
    if lista[meio] == elemento:
        return True
    if lista[meio] < elemento:
        nova = lista[meio + 1:]
    if lista[meio] > elemento:
        nova = lista[:meio]
    return busca_binaria(nova, elemento)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elemento = random.randint(1, 20); print(elemento)
print(busca_binaria(lista, elemento))