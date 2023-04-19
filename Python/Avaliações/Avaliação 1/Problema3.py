num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
op = input("Digite a operação: ")

if op == 'a':
    print(num1 + num2)
elif op =='s':
    print(num1 - num2)
elif op == 'm':
    print(num1 * num2)
elif op == 'p':
    print(num1 ** num2)
elif op == 'd':
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Erro, divisão por 0!")
else:
    print("Operação inválida!")
    