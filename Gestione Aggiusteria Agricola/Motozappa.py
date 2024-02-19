from Apparecchio import Apparecchio

class Motozappa(Apparecchio):
    # attributi/proprietà
    nruote: int
    #Costruttore
    def __init__(self, id, marca,nruote):
        super().__init__(id, marca)
        self.nruote = nruote
    # Metodo toString
    def __str__(self) -> str:
        return super().__str__() + f""", dotato di nr {self.nruote} ruote"""
    # Metodo lavorazioni
    def lavorazioni(self):
        scheda = super().lavorazioni() | {"cambio candela":15,
                                             "cambio tappo": 5,
                                             "affilatura":35}
        return scheda