# encontra a data mais recente em um arquivo de datas
monthlen = [31,28,31,30,31,30,31,31,30,31,30,31]

with open(r"C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\8 - Arquivos\datas.txt", "r") as arquivo:
    maior_dia = md =   0
    maior_mes = mmes = 0
    maior_ano = my =   0
    for linha in arquivo:
        dd, mm, yy = linha.strip().split("/")
        if int(yy) > int(my):
            md = dd
            mmes = mm
            my = yy
        elif int(yy) == int(my):
            if int(mm) > int(mmes):
                md = dd
                mmes = mm
                my = yy
            elif int(mm) == int(mmes):
                if int(dd) > int(md):
                    md = dd
                    mmes = mm
                    my = yy
    
    print("/".join([md, mmes, my]))

with open(r"C:\Users\Rodrigo\OneDrive - Universidade Federal de Minas Gerais\Documentos\Programação\IPC\Python\8 - Arquivos\datas.txt", "r") as arquivo:
    dates = [line.strip().split("/") for line in arquivo]
    most_recent = max(dates, key=lambda date: (int(date[2]), int(date[1]), int(date[0])))
    print("/".join(most_recent))