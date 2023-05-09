# ip = input().split(".")

# for i in ip:
#     if int(i) < 0 or int(i) > 255:
#         print("IP inválido")
#         quit()
#         # valido = False
#         # break

# print("IP válido")

# # if valido == False:
# #     print("IP inválido")
# # else:
# #     print("IP válido")

print("Inválido" if any([1 if int(i) not in range(256) else 0 for i in input().split(".")]) else "Válido")