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
print(f"Novo salario: {novo:.2f}")