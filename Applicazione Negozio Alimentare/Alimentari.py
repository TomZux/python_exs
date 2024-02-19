from Prodotti import Prodotti
from datetime import datetime

class Alimentari(Prodotti):
    # attributo
    dataScadenza: datetime
    # costruttore
    def __init__(self, codice_a_barre, descrizione, prezzo, dataScadenza):
        super().__init__(codice_a_barre, descrizione, prezzo)
        self.dataScadenza = dataScadenza
    # metodo toString
    def toString(self):
        return super().toString() + f", scadenza {self.dataScadenza}"

    def getDataScadenza(self):
        return self.dataScadenza
    # metodo sconto
    def applicaSconto(self):
        if self.getDifference():
            self.prezzo = self.prezzo - (self.prezzo * 20/100)
            return self.prezzo
        else:
            return super().applicaSconto()
    # metodo getDifference
    
    def getDifference(self):
        oggi = datetime.now()
        secondDate = datetime.strptime(self.dataScadenza,"%d/%m/%Y")
        diff = (secondDate - oggi).days
        if diff <= 10:
            return True
        else:
            return False
