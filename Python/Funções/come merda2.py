from unidecode import unidecode
def come_merda():
    while True:
        frase = input("Você está bem? Sim ou não: ")
        if unidecode(frase.lower()) == 'nao':
            print("Vontade de come merda.")
            break
        else:
            continue

input ("Pressione enter para sofrer.")
come_merda()

