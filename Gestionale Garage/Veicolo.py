class Veicolo():
    # attributi/proprietà
    marca: str
    anno: int
    cilindrata: int
    # Costruttore 
    def __init__(self,marca,anno,cilindrata):
        self.marca = marca
        self.anno = anno
        self.cilindrata = cilindrata
    # Metodo toString
    def toString(self):
        scheda = f"""
        Il veicolo: Marca {self.marca}, anno di produzione {str(self.anno)}, cilindrata {str(self.cilindrata)} cc
        """
        return scheda
                                                     