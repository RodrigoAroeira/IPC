# def tamanho_maior_string(lista):
#     if lista != []:
#         return len(max(lista))
#     else: 
#         return 0
    

def tamanho_maior_string(lista):
    listalen = [len(i) for i in lista]
    return max(listalen) if lista != [] else 0