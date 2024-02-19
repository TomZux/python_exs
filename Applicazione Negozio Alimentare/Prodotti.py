class Prodotti():
    # attributi
    codice_a_barre: str
    descrizione: str
    prezzo: float
    # costruttore
    def __init__(self,codice_a_barre,descrizione,prezzo):
        self.codice_a_barre = codice_a_barre
        self.descrizione = descrizione
        self.prezzo = prezzo
    # Metodi per prendere gli attributi

    def getCodiceABarre(self):
        return self.codice_a_barre
     
    def getDescrizione(self):
        return self.descrizione

    def getPrezzo(self):
        return self.descrizione
    
    # Metodo toString

    def toString(self):
        scheda = f"""Inserito il prodotto: {self.descrizione}, con codice {self.codice_a_barre}, prezzo:
        {self.prezzo} euro  """
        return scheda

    # Metodo Sconto

    def applicaSconto(self):
        self.prezzo = self.prezzo - (self.prezzo*5/100)
        return self.prezzo