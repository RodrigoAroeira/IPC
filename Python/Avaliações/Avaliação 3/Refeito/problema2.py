def incluir_aluno(path, nome, listanotas, a=0):
    alunos = {}
    if any(notas < 0 or notas > 25 for notas in listanotas):
        return False
    else:
        alunos[nome] = listanotas
        av1, av2, av3, av4 = listanotas    
    with open(path, 'a') as arquivo:
        if a == 1:
            arquivo.truncate(0)
            arquivo.close()
        try:
            for aluno, _ in alunos.items():
                arquivo.write(f'{aluno},{av1},{av2},{av3},{av4}\n')
        except: 
            from os import system as s; s('cls')
            exit()
    return True

a = 1

notas = [0, 0, 10, 25]
print(incluir_aluno(r"C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\Avaliações\Avaliação 3\Refeito\notas.txt", "Fezes", notas, a))