def produto_escalar(u, v):
    resultado = 0
    for i in range(len(u)):
        resultado += float(u[i]) * float(v[i])
    return (resultado)