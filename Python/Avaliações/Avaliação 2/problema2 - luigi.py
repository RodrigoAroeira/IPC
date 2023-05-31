def esta_ordenada(xs):
    return xs == sorted(xs) # não era pra ser feito assim pq ele esqueceu de botar no enunciado

def esta_ordenada(xs):
    for i in range(len(xs)):
        if xs[i] > xs[i+1]:
            return False
    return True