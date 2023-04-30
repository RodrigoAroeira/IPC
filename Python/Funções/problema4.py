def calcula_valor(preço, litros, tipo):
    if tipo == "A".lower():
        if litros <= 20:
            desconto = 3/100
        else:
            desconto = 5/100
    elif tipo == "G".lower():
        if litros <= 20:
            desconto = 4/100
        else:
            desconto = 6/100
    valor = preço * litros
    valor_final = valor - (valor * desconto)
    return valor_final