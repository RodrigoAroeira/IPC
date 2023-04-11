def num_div():
    div = 0
    n = int(input("Insira o valor de o último número do intervalo: "))
    for i in range(3, n+1):
        if i % 3 == 0:
            div += 1
    print(f"Há {div} divisores de 3 no intervalo [3, {n}] ")
    return div

num_div()
