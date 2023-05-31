def compactar_strings(s1,s2):
    lp = []
    if len(s1) < len(s2):
        while len(s1) < len(s2):
            s1 += " "
    elif len(s2) < len(s1):
        while len(s2) < len(s1):
            s2 += " "
    for i in range(len(s1)):
        lp.append(s1[i]); lp.append(s2[i])
        for x in lp:
            if x == " ":
                lp.remove(x)
                lp.append("")
    return lp

def intercalar_strings(s1,s2):
    ns = "".join(compactar_strings(s1,s2))
    return ns

print(compactar_strings("Tpo", "oCder"))
print(intercalar_strings("Tpo", "oCder")) # output deve ser TopCoder
