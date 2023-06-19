def remover_duplicados(tupla):
    tupla = tuple(map(int, tupla))
    dict = {}
    for i in tupla:
        dict[i] = dict.get(i, 0) + 1
    return tuple(dict.keys())

xs = input().split()

print(remover_duplicados(xs))