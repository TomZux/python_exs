from Veicolo import Veicolo

class Moto(Veicolo):
    #attributi/proprietà del figlio
    tempi: int
    #Costruttore
    def __init__(self, marca, anno, cilindrata,tempi):
        super().__init__(marca, anno, cilindrata)
        self.tempi = tempi
    # Metodo toString
    def toString(self):
        scheda = super().toString() + f""",con motore {str(self.tempi)} tempi """
        return scheda