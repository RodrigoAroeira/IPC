v0 = float(input("Digite o valor da velocidade: "))
acel = float(input("Digite o valor da aceleração: "))
tempo = float(input("Digite o valor do tempo: "))

vfinal = v0 + acel*tempo
dist = v0*tempo + 1/2*acel*tempo**2

print(f"Velocidade final: {vfinal:.2f}")
print(f"Distância percorrida: {dist:.2f}")
