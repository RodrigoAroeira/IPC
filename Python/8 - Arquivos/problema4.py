# encontra a data mais recente em um arquivo de datas
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

