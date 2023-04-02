def getfloat(msg):
    return float(input(msg))   

v0 = getfloat("Digite o valor da velocidade: ") 
acel = getfloat("Digite o valor da aceleração:")
tempo = getfloat ("Digite o valor do tempo: ")

vfinal = v0 + acel*tempo
dist = v0*tempo + 1/2*acel*tempo**2
