num = int(input())

with open("C:\\Users\Rodrigo\\OneDrive - Universidade Federal de Minas Gerais\Documentos\\Programação\\IPC\\Python\8 - Arquivos\\texto.txt", "r") as arquivo:
    for linha in arquivo:
        for palavra in linha.split():
            if len(palavra) >= num:
                print(palavra)
