segundos = int(input("Digite o valor do tempo em segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = segundos % 60

print(f"Valor convertido: {horas} h {minutos} min {segundos}s")
