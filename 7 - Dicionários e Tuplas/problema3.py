from  operator import itemgetter
alunos = {}

while True:
    nome = input()
    if nome == '':
        break
    nota = input().split()
    med = sum([float(i) for i in nota]) / len(nota)
    alunos[nome] = med

alunos_dict = alunos.copy()
print(alunos)
# alunos = sorted(alunos.items(), key = itemgetter(1), reverse = True)
alunos = sorted(alunos.items(), key = lambda item: item[1], reverse = True)

for aluno, media in alunos:
    print(f'{aluno} - {media:.2f}')