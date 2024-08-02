import string
import random
length = input("Quanti caratteri vuoi nella tua password? Inserisci un numero: ")
number = input("Vuoi che la tua password contenga numeri? (y/n): ")
symbol = input("Vuoi che la tua password contenga simboli? (y/n): ")

def generapassword(length, number, symbol):
    lista_caratteri = []

    if number.lower() == "si":
        lista_caratteri += list(string.digits)
    if symbol.lower() == "si":
        lista_caratteri += ["?", "!", ",", "@", "%", "~", "`", "_", "&", "£", "$"]
    lista_caratteri += list(string.ascii_letters)
    if not lista_caratteri:
        raise ValueError("Deve essere selezionata almeno una categoria di caratteri")
    
    password = ''.join(random.choice(lista_caratteri) for _ in range(int(length)))
    return password
try:
    password = generapassword(length, number, symbol)
    print(f"La tua password generata è: {password}")
except ValueError as e:
    print(e)
