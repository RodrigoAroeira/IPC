# checar se lista está ordenada
# def esta_ordenada(lista):
#     return True if lista == sorted(lista) else False


esta_ordenada = lambda l: True if l == sorted(l) else False

print(esta_ordenada([1,2,4]))