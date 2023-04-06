produto = float(input("Digite o valor do produto: "))
estado = input("Digite o estado: ")

lista = {
    "MG": 1.07,
    "SP": 1.12,
    "RJ": 1.15,
    "MS": 1.08
}

taxa = lista.get(estado)

if taxa:
    print(f"Valor final: {produto*taxa:.2f}")
else:
    print("Estado inválido")
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(f"pr: {produto}, s: {estado}")

# for state, taxa in lista.items():

#     if estado == state:
#         print(f"Valor final: {produto*taxa:.2f}")
#     else:
#         print("Estado inválido")
#     break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#código antigo

# if estado == ("MG"):
#     print(f"Valor final: {produto*1.07:.2f}")
# elif estado == ("SP"):
#     print(f"Valor final: {produto*1.12:.2f}")
# elif estado == ("RJ"):
#     print(f"Valor final: {produto*1.15:.2f}")
# elif estado == ("MS"):
#     print(f"Valor final: {produto*1.08:.2f}")
# else:
#     print("Estado inválido")

