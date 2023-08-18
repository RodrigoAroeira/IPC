compra = float(input("Digite o valor da compra: "))

valor_desconto = 0.9*compra
valor_parcela = compra/6
comissao_vista = 0.05*compra*0.9
comissao_parc = 0.05*compra

print(f"Valor com desconto: {valor_desconto:.2f}")
print(f"Valor da parcela: {valor_parcela:.2f}")
print(f"Comissão do vendedor(à vista): {comissao_vista:.2f}")
print(f"Comissão do vendedor(parcelado): {comissao_parc:.2f}")
