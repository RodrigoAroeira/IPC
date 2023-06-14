def remover_duplicados(tupla):
    lista = list(tupla)
    lista = list(dict.fromkeys(lista))
    return tuple(lista)

print(remover_duplicados((1,1,2,3,1,2)))