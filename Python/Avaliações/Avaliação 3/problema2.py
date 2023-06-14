def incluir_aluno(path, nome, listanotas):
    tamanho = len(listanotas)
    alunos = {}
    for nota in listanotas:
        if any(notas < 0 or notas > 25 for notas in listanotas) == True:
            return False
        elif all(notas >= 0 and notas <= 25 for notas in listanotas) == True:
            alunos[nome] = listanotas
            av1, av2, av3, av4 = listanotas    
    with open(path, 'a') as arquivo:
        for aluno, notas in alunos.items():
            arquivo.write(f'{aluno},{av1},{av2},{av3},{av4}\n')

incluir_aluno(r"C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\Avaliações\Avaliação 3\notas.txt", 'Rodrigo', [10, 100, 1, 2])
