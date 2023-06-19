def incluir_aluno(path, nome, listanotas):
    alunos = {}
    if any(notas < 0 or notas > 25 for notas in listanotas):
        return False
    else:
        alunos[nome] = listanotas
        av1, av2, av3, av4 = listanotas    
    with open(path, 'a') as arquivo:
        for aluno, _ in alunos.items():
            arquivo.write(f'{aluno},{av1},{av2},{av3},{av4}\n') 
    return True

notas = [10, 10, 10, 25]
print(incluir_aluno(r"C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\Avaliações\Avaliação 3\Refeito\notas.txt", "Fezes", notas))