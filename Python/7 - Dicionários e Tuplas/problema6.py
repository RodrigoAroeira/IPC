unidades = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8:
"VIII", 9: "IX"}

dezenas = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX",
8: "LXXX", 9: "XC"}

centenas = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7:
"DCC", 8: "DCCC", 9: "CM"}

num = [*(input())]
num = list(map(int, num))

if len(num) == 1:
    print(unidades[(num[0])])
elif len(num) == 2:
    print(dezenas[(num[0])]+unidades[(num[1])])
else:
    print(centenas[(num[0])]+dezenas[(num[1])]+unidades[(num[2])])

