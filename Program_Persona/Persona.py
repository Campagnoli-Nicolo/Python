class Persona:
    def __init__(self,nome,cognome,eta):
        self.nome = nome
        self.__cognome = cognome
        self.__eta = eta

    def setCognome(self,cognome):
        self.__cognome = cognome

    def setEta(self,eta):
        self.__eta = eta

    def getCognome(self):
        return self.__cognome
    
    def getEta(self):
        return self.__eta

    def toStringa(self):
        return "Nome: ",self.nome," Cognome: ", self.__cognome," Eta: ",self.__eta

def Aggiungi(lista):
    nome = input("Inserisci il nome ")
    cognome = input("Inserisci il cognome ")
    eta = input("Inserisci l'eta ")
    lista.append(Persona(nome,cognome,eta))

def Visualizza(lista):
    print("\n")
    for Persona in lista:
        print(Persona.nome,Persona.getCognome(),Persona.getEta())

    print("\n")        
