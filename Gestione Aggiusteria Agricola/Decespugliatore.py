from Apparecchio import Apparecchio

class Decespugliatore(Apparecchio):
    #attributi/proprietà
    ae: bool
    # Costruttore
    def __init__(self, id, marca,ae):
        super().__init__(id, marca)
        self.ae = ae
    # Metodo toString
    def __str__(self) -> str:
        return super().__str__() + f""", dotato di accensione elettronica {self.ae}"""
    # Metodo lavorazioni
    def lavorazioni(self):
        scheda = super().lavorazioni() | {"sostituzione filo": 15,
                                            "sostituzione batteria":20}
        return scheda