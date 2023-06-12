try:
    with open("datas.txt", "r") as a:
        for linha in a: print(linha)
except FileNotFoundError:
    raise FileNotFoundError("Arquivo não encontrado")
    with open(r"C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\8 - Arquivos\datas.txt", "r") as a:
        for linha in a: print(linha)