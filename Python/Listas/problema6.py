def tamanho_maior_string(lista):
    if lista != []:
        return len(max(lista), key=len)
    else: 
        return 0