compra = float(input("Digite o valor da compra: "))

print(f"Valor com desconto: {compra*0.9:.2f}")
print(f"Valor da parcela: {compra/6:.2f}")
print(f"Comissão do vendedor(à vista): {0.05*compra*0.9:.2f}")
print(f"Comissão do vendedor(parcelado): {0.05*compra:.2f}")
