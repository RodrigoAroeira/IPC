def seq_maior_produto(lista):
    if type(lista) != list:
        lista = [int(i) for i in str(lista)]
    maiorProd = 0
    nums = None
    for i in range(len(lista)):
        if lista[i]*lista[i+1]*lista[i+2] > maiorProd:
            maiorProd = lista[i]*lista[i+1]*lista[i+2]
            nums = (lista[i],lista[i+1],lista[i+2])
        if i == len(lista) - 3: break
    return nums 


lista = 876476848733959008

print(seq_maior_produto(lista))
