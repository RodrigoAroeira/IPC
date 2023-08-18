lista = []

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Nota inválida")
else:
    lista.append(nota1)
    lista.append(nota2)
    media = sum(lista) / len(lista)
    print(f"Média: {media:.2f}")
