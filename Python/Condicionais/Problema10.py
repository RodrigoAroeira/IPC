dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

bissexto = ( ano % 400 == 0 ) or ( ano % 4 == 0 and ano % 100 != 0 )

if mes == 2:
    if bissexto:
        diasmes = 29
    else:
        diasmes = 28
elif mes in [4, 6, 9, 11]:
    diasmes = 30
else:
    diasmes = 31

if dia < 1 or dia > diasmes or mes < 1 or mes > 12:
    print("Data inválida")
else:
    print ("Data válida")
    