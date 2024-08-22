from Studente import *

registro = []

def Aggiungi():
    ctrl = False
    err = False
    nome = input("Inserisci il nome dell'alunno da mettere sul registro: ")
    cognome = input("Inserisci il cognome dell'alunno: ")
    
    while not err:
        try:
            eta = int(input("Inserisci l'eta dell'alunno: "))
            err = True
        except Exception:
            print("ERRORE,Devi inserire un numero per l'eta\n")
            err = False

    for studente in registro:
        if nome == studente.getNome() and cognome == studente.getCognome():
            print("Il ragazzo che vuoi inserire è già stato inserito")
            ctrl = True

    if not ctrl: 
        registro.append(Studente(nome,cognome,eta))

def Visualizza():
    for studente in registro:
        print(studente.toString())

def Rimuovi():
    t_nome = input("Inserisci il nome dell'alunno da rimuovere: ")
    t_cognome = input("Inserisci il cognome dell'alunno da rimuovere: ")
    ctrl = False

    for studente in registro:
        if t_nome == studente.getNome() and t_cognome == studente.getCognome():
            registro.remove(studente)
            ctrl = True
            print("Il ragazzo è stato rimosso con successo")
            break
    if not ctrl:
        print("Il ragazzo che stai cercando di rimuovere non è all'interno del registro")

def Cerca():
    ctrl = False
    temp = input("Inserisci il nome dell'alunno da cercare: ")

    for studente in registro:
        if temp == studente.getNome():
            print(studente.toString())
            ctrl = True
            
    if not ctrl:
        print("Il ragazzo che stai cercando non è all'interno del registro")

def Media():
    somma = 0
    c = 0
    for studente in registro:
        somma += studente.getEta()
        c +=1
    
    media = somma/c
    print ("La media degli anni di tutti gli studenti è ",media)


def RimuoviIndex():
    i = int(input("Inserisci l'indice dello studente da rimuovere: "))
    del registro[i]

def Menu():
    opz = 0
    
    while opz != 6:
        print("\n")
        print("1) Inserisci uno studente")
        print("2) Visualizza registro")
        print("3) Rimuovi studente")
        print("4) Media studenti")
        print("5) Cerca studente")
        print("6) Esci")
        opz = int(input())

        if opz == 1:
            Aggiungi()
        elif opz == 2:
            Visualizza()
        elif opz == 3:
            RimuoviIndex()
        elif opz == 4:
            Media()
        elif opz == 5:
            Cerca()