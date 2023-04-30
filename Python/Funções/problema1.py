def pagamento(salario):
    if salario <= 280:
        novo = salario * 1.2
    elif salario <= 700:
        novo = salario * 1.15
    elif salario <= 1500:
        novo = salario * 1.1
    else:
        novo = salario * 1.05
    return novo


# salario = float(input("Digite o valor do salário: "))

# print(pagamento(salario))