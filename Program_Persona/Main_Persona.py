from Persona import *

lista = []
opz = 0
while(opz != 3):
    print("Menu di scelta")
    print("--------------")
    print("1) per inserire una persona nella lista ")
    print("2) per visualizzare le persone nella lista ")
    print("3) per uscire dal Programma ")
    print("--------------------------------------------")
    opz = int(input())

    match opz:
        case 1:
            Aggiungi(lista)
        case 2:
            Visualizza(lista)
            
