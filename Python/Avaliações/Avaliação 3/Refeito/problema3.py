def remover_duplicados(tupla):
    # tupla = tuple(map(int, tupla)) # Não fazer isso, pois os elementos, não necessariamente, são inteiros
    dic = {}
    for i in tupla:
        dic[i] = dic.get(i, 0) + 1
    return tuple(dic.keys())

xs = input().split()

print(remover_duplicados(xs))