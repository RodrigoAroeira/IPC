def intersecao(a,b,):
  c = []
  for x in a:
    if x in b and x not in c:
      c.append(x)
  return c

def intersecao(a,b):
  return [x for x in a if x in b]