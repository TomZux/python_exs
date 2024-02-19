from Prodotti import Prodotti

class NonAlimentari(Prodotti):
    # attributo
    materiale: str
    # Costruttore
    def __init__(self, codice_a_barre, descrizione, prezzo, materiale):
        super().__init__(codice_a_barre, descrizione, prezzo)
        self.materiale = materiale
    # metodo toString
    def toString(self):
        return super().toString() + f", realizzato in {self.materiale}"
    
    def getMateriale(self):
        return self.materiale
    # metodo sconto

    def applicaSconto(self):
        if self.materiale in ['carta','cartone','vetro']:
            self.prezzo = self.prezzo - (self.prezzo * 10/100)
            return self.prezzo
        else:
            return super().applicaSconto()
            