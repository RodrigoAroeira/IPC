from unidecode import unidecode
def come_merda():
    while True:
        frase = input("Você está bem? Sim ou não: ")
        if unidecode(frase) == 'nao':
            print("Vontade de come merda.")
            break
        else:
            continue

def main():
    input ("Pressione enter para sofrer.")
    come_merda()

main()