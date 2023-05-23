# def tamanho_maior_string(lista):
#     if lista != []:
#         return len(max(lista))
#     else: 
#         return 0
    

def tamanho_maior_string(lista):
    return max(map(len,lista))
    # listalen = [len(i) for i in lista]
    # return max(listalen) if lista else 0

lista = ['asdasd', 'sdadsadas', 'asda']

print(tamanho_maior_string(lista))