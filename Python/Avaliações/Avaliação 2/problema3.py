# interseção de listas
def intersecao(lista1, lista2, intersect = []):
  [intersect.append(i) if i in lista2 else 0 for i in lista1]
  # for i in range(len(intersect)):
    # intersect[i] = int(intersect[i])
  return sorted(intersect) if intersect else 0
  #  return sorted(list(set(lista1) & set(lista2))) sugestão do copilot