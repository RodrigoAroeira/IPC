htot = int(input("Entre com as horas: "))
taxa = float(input("Entre com o valor por hora: "))

if htot <= 40:
    hregular = htot
    hextra = 0
else:
    hregular = 40
    hextra = htot - 40

pag = hregular * taxa + (hextra * taxa * 1.5)

print (f"Pagamento: R${pag:.2f}")
