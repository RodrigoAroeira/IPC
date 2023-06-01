with open(r"C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\8 - Arquivos\notas.txt", "r") as arquivo:
    aluno = {}
    for linha in arquivo:
        nome, n1, n2, n3, n4 = linha.split()
        aluno.get(nome, 0)
        aluno[nome] = (float(n1) + float(n2) + float(n3) + float(n4)) / 4

    [print(f"{nome} - Média: {aluno[nome]:.2f}") for nome in aluno if aluno[nome] >= 60]