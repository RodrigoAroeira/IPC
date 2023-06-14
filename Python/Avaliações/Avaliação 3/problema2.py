def incluir_aluno(path, nome, nota):
    with open(path, 'a') as arquivo:
        arquivo.write(f'{nome} {nota}\n')