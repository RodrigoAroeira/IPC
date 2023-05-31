def compactar_strings(s1, s2):    
    l1 = [x for x in s1]
    l2 = [x for x in s2]
    l3 = []

    ts1 = len(s1)
    ts2 = len(s2)
    c = 0

    while True:
        if ts1 < ts2:
            l1.append('')
            ts1 = len(l1)
        elif ts2 < ts1:
            l2.append('')
            ts2 = len(l2)
        if ts1 == ts2:
            break
        
    for l in l1:
        l3.append([l1[c], l2[c]])
        c += 1
    return l3

def intercalar_strings(s1, s2):
    ns = ''
    l = compactar_strings(s1, s2)
    for x in l:
        ns += ''.join(x)
    return ns

print(compactar_strings("Tpo", "oCder"))
print(intercalar_strings("Tpo", "oCder")) # output deve ser TopCoder
