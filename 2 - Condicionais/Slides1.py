nota1 = float(input("Entre com a nota 1:"))
nota2 = float(input("Entre com a nota 2:"))
nota3 = float(input("Entre com a nota 3:"))
nota4 = float(input("Entre com a nota 4:"))

med = (nota1 + nota2 + nota3 + nota4)/4

print (med)
if med >= 60:
    print ("Aprovado!")

else:
    print ("Reprovado!")