
from Veicolo import Veicolo

class Auto(Veicolo):
    #attributi/proprietà del figlio
    porte: int
    alimentazione: str
    # Costruttore
    def __init__(self, marca, anno, cilindrata,porte,alimentazione):
        super().__init__(marca, anno, cilindrata)
        self.porte = porte
        self.alimentazione = alimentazione
    # Metodo toString
    def toString(self):
     scheda = super().toString() + f""",con alimentazione {self.alimentazione} e nr {str(self.porte)} porte"""
     return scheda
                       