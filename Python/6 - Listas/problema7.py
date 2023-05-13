def nested_sum(lista, l=[]):
    if lista:
        for i in lista:
            if type(i) == list:
                nested_sum(i, l)
            else:
                l.append(i)
        return sum(l)
    else:
        return 0

# lista = [1, 2, [3], [4, [5, 6], 7], 8, [9, [10]]]

# print(nested_sum(lista))