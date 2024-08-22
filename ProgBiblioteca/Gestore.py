from Libro import *
biblioteca = []

def Aggiungi():

    titolo = input("Inserisci il titolo del libro che vuoi aggiungere: ")
    autore = input("Inserisci l'autore del libro: ")
    err = False
    ctrl = False

    for libro in biblioteca:
        if titolo == libro.getTitolo() and autore == libro.getAutore():
            print("Il libro che stai cercando di inserire è già stato inserito")
            ctrl = True

    while not err:
        try:
            anno = int(input("Inserisci l'anno del libro: "))
            err = True
        except Exception:
            print("Errore,L'anno di pubblicazione deve essere un numero")
            err = False
    
    prestito = False
    if not ctrl:
        biblioteca.append(Libro(titolo,autore,anno,prestito))

def Visualizza():
    for libro in biblioteca:
        print(libro.toString())

def CercaTitolo():
    ctrl = False
    titolo = input("Inserisci il titolo del libro che vuoi trovare: ")
    for libro in biblioteca:
        if titolo == libro.getTitolo():
            print(libro.toString())
            ctrl = True
            break
    
    if not ctrl:
        print("Il libro che stai cercando non è stato trovato")

def CercaAutore():
    autore = input("Inserisci l'autore del libro che vuoi trovare: ")
    ctrl = False
    for libro in biblioteca:
        if autore == libro.getAutore():
            print(libro.toString())
            ctrl = True

    if not ctrl:
        print("Libri scritti da questo autore non trovati")

def Prestito():
    temp = input("Inserisci il titolo del libro che vuoi prendere in prestito: ")
    ctrl = False
    for libro in biblioteca:
        if libro.getTitolo() == temp and not libro.getPrestito():
            libro.setPrestito(True)
            print(temp," ti è stato prestato ricordati di riportarlo")
            ctrl = True
    
    if  not ctrl:
        print("Il libro che vuoi prendere in prestito è già assegnato a quialcun'altro oppure non c'è")

def Restituzione():
    temp = input("Inserisci il titolo del libro che vuoi restituire: ")
    ctrl = False
    for libro in biblioteca:
        if libro.getTitolo() == temp and libro.getPrestito():
            libro.setPrestito(False)
            print(temp," è stato restituito correttamente")
            ctrl = True
    
    if ctrl == False:
        print("Il libro che vuoi restituire non è presente o non è stato ancora prestato")

def Rimuovi():
    ctrl = False
    temp = input("Inserisci il nome del libro che vuoi rimuovere dalla biblioteca: ")
    for libro in biblioteca:
        if temp == libro.getTitolo():
            biblioteca.remove(libro)
            ctrl = True

    if not ctrl:
        print("Il libro che stai cercando di rimuovere non è presente")

def Menu():
    opz = 0
    while opz != 8:
        ctrl = False
        print("\n")
        print("1) Aggiungi libro")
        print("2) Visualizza")
        print("3) Cerca per titolo")
        print("4) Cerca per autore")
        print("5) Prendi in prestito")
        print("6) Restituisci")
        print("7) Rimuovi libro")
        print("8) Esci")
        
        while not ctrl:
            try:
                opz = int(input())
                ctrl = True
            except Exception:
                ctrl = False
                print("ERRORE, Inserisci un numero intero\n")

        if opz == 1:
            Aggiungi()
        elif opz == 2:
            Visualizza()
        elif opz == 3:
            CercaTitolo()
        elif opz == 4:
            CercaAutore()
        elif opz == 5:
            Prestito()
        elif opz == 6:
            Restituzione()
        elif opz == 7:
            Rimuovi()