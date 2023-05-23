def nested_sum(lista, l=[]):
    if lista:
        for item in lista:
            if type(item) == list:
                nested_sum(item, l)
            else:
                l.append(item)
        return sum(l)
    else:
        return 0

# lista = [1, 2, [3], [4, [5, 6], 7], 8, [9, [10]]]

# print(nested_sum(lista))