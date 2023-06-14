def incluir_aluno(path, nome, listanotas):
    tamanho = len(listanotas)
    alunos = {}
    for nota in listanotas:
        if any(notas < 0 or notas > 25 for notas in listanotas):
            pass
        elif all(notas >= 0 and notas <= 25 for notas in listanotas):
            alunos[nome] = listanotas
    with open(path, 'a') as arquivo:
        for aluno, notas in alunos.items():
            for av1, av2, av3, av4 in notas:
            arquivo.write(f'{aluno},{av1},{av2},{av3},{av4}\n')
