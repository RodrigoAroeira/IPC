from math import sqrt

num = float(input("Digite um número: "))

if num >= 0:
    print (f"Resultado: {sqrt(num):.3f}")
else:
    print ("Número inválido")