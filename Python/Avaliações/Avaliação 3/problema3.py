def remover_duplicados(tupla):
    lista = []
    for i in tupla:
        if i not in lista:
            lista.append(i)
    return tuple(lista)

print(remover_duplicados((1,1,2,3,1,2)))