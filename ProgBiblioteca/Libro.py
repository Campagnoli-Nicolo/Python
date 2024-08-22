class Libro:
    def __init__(self,titolo,autore,anno,prestito = False):
        self.__titolo = titolo
        self.__autore = autore
        self.__anno = anno
        self.__prestito = prestito
    
    def getTitolo(self):
        return self.__titolo
    def getAutore(self):
        return self.__autore
    def getAnno(self):
        return self.__anno
    def getPrestito(self):
        return self.__prestito
    def setPrestito(self,prestito):
        self.__prestito = prestito
    def toString(self):
        return f'{self.__titolo} - {self.__autore} - {self.__anno} - {self.__prestito}'