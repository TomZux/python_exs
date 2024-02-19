class Cliente():
    # attributi
    codice: str
    spesaEuro: int
    spesaCentesimi: int
    # Costruttore
    def __init__(self,codice):
        self.codice = codice
        self.spesaEuro = 0
        self.spesaCentesimi = 0
    # Metodi Get attributi

    def getCodice(self):
        return self.codice
    
    def getSpesaEuro(self):
        return self.spesaEuro
    
    def getSpesaCentesimi(self):
        return self.spesaCentesimi
    
    def toString(self):
        scheda = f"""
        Il cliente, codice {self.codice}, spesa pari a {self.spesaEuro} euro, nr {self.spesaCentesimi} centesimi
        """
        return scheda