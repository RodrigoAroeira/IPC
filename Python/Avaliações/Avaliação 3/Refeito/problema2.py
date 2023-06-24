def incluir_aluno(path, nome, listanotas, var=0):
    alunos = {}
    if any(notas < 0 or notas > 25 for notas in listanotas):
        return False
    else:
        alunos[nome] = listanotas
        av1, av2, av3, av4 = listanotas    
    with open(path, 'a') as arquivo:
        if var == 1:
            arquivo.truncate(0) # limpar arquivo para motivos de teste
            arquivo.close()
        try:
            for aluno, _ in alunos.items():
                arquivo.write(f'{aluno},{av1},{av2},{av3},{av4}\n')
        except ValueError:
            from os import system as s; s('cls') # limpar terminal do windows
            print('Arquivo limpo.'); exit()
    return True

caminho = 'C:\\Users\\Rodrigo\\OneDrive - Universidade Federal de Minas Gerais\
\\Documentos\\Programação\\IPC\\Python\\Avaliações\\Avaliação 3\\Refeito\\notas.txt'
nome = 'Fezes'
notas = [0, 0, 10, 25]
var = 1
print(incluir_aluno(caminho, nome, notas, var))