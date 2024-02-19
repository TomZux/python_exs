from Veicolo import Veicolo

class Furgone(Veicolo):
    #attributi/proprietà del figlio
    capacità: int
    #Costruttore
    def __init__(self, marca, anno, cilindrata,capacità):
        super().__init__(marca, anno, cilindrata)
        self.capacità = capacità
    # Metodo toString
    def toString(self):
        scheda = super().toString() + f""",con capacità {str(self.capacità)} tonnellate"""
        return scheda