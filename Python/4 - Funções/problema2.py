def pagamento(valor, horas):
    bruto = valor * horas
    if bruto <= 900:
        ir = 0
    elif bruto <= 1500:
        ir = 5/100
    elif bruto <= 2500:
        ir = 10/100
    else:
        ir = 20/100
    liquido = bruto - (bruto * ir)
    return liquido
        