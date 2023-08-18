salario = float(input("Digite o valor do salário: "))


if salario <= 280:
    novo = salario * 1.2
elif salario <= 700:
    novo = salario * 1.15
elif salario <= 1500:
    novo = salario * 1.1
else:
    novo = salario * 1.05

print(f"Valor do aumento: {novo-salario:.2f}")
print(f"Novo salário: {novo:.2f}")


#código feito pelo chat gpt

# salario = float(input("Digite o salário atual do colaborador: "))

# faixas_salariais = {
#     280: 0.2,
#     700: 0.15,
#     1500: 0.1,
# }

# porcentagem_aumento = 0.05

# for faixa, porcentagem in faixas_salariais.items():
#     if salario <= faixa:
#         porcentagem_aumento = porcentagem
#         break

# aumento = salario * porcentagem_aumento
# novo_salario = salario + aumento

# print(f"O valor do aumento foi de R$ {aumento:.2f}.")
# print(f"O novo salário é de R$ {novo_salario:.2f}.")
