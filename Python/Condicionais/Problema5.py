import math

num = float(input("Digite um número: "))

if num >= 0:
    print (f"Resultado: {math.sqrt(num):.3f}")
else:
    print ("Número inválido")