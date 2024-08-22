class Studente:
    def __init__(self,nome,cognome,eta):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
    
    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def getEta(self):
        return self.__eta
    def toString(self):
        return f'{self.__nome} - {self.__cognome} - {self.__eta}'