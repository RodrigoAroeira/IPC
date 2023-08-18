rna = {
    'UUU': 'Phe',
    'CUU': 'Leu',
    'UUA': 'Leu',
    'AAG': 'Lisina',
    'UCU': 'Ser',
    'UAU': 'Tyr',
    'CAA': 'Gln',
}


# Entrada: UUUUUAUCU
# Saída: Cadeia de Aminoácidos: Phe-Leu-Ser
entrada = input("Entrada: ")
saida = "Cadeia de Aminoácidos: "

for i in range(0, len(entrada), 3):
    if entrada[i:i+3] in rna:
        saida += rna[entrada[i:i+3]] + "-"

print(saida[:-1])