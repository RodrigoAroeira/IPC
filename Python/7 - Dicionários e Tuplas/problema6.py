UNIDADES = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8:
"VIII", 9: "IX"}

DEZENAS = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX",
8: "LXXX", 9: "XC"}

CENTENAS = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7:
"DCC", 8: "DCCC", 9: "CM"}

num = [*int(input())].reverse()

if len(num) ==1:
    print(UNIDADES[(num[0])])
elif len(num) == 2:
    print(DEZENAS[(num[0])]+UNIDADES[(num[1])])
else:
    print(CENTENAS[(num[0])]+DEZENAS[(num[1])]+UNIDADES[(num[2])])

