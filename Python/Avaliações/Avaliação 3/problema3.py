def remover_duplicados(tupla):
    tupla = tuple(map(int, tupla))
    lista = []
    for i in tupla:
        if i not in lista:
            lista.append(i)
    return tuple(lista)

xs = input().split()

print(remover_duplicados(xs))