def nested_sum(lista, l=[]):
    if lista != []:
        for i in lista:
            if type(i) == list:
                nested_sum(i, l)
            else:
                l.append(i)
        return sum(l)
    else:
        return 0