class Apparecchio():
    # attributi/proprietà
    # numero ordine lavorazione
    id: int
    # costo totale riparazione
    costo: int
    # marca apparecchio
    marca: str
    # lista lavorazioni
    lista_lavorazioni: list
    # Costruttore
    def __init__(self,id,marca):
        self.id = id
        self.marca = marca
        self.costo = 0
        self.lista_lavorazioni = []
    
    # Metodo toString
    def __str__(self) -> str:
        scheda = f"""
        Codice identificativo {self.id}, Marca {self.marca}
        """
        return scheda

    # Metodo lavorazioni
    def lavorazioni(self):
        lavorazioni_apparecchio =   {'manutenzione':40,
                                        'riparazione':50,
                                        'rettifica':30}
        return lavorazioni_apparecchio
        # while True: 
        #     try:
        #         user_add = input("Inserisci la lavorazione: ")
        #         if user_add.lower() in lavorazioni_apparecchio.keys():
        #             self.costo += lavorazioni_apparecchio[user_add]
        #         else:
        #             return("La lavorazione non è presente nel listino")

                # proseguire = input("Vuoi aggiungere altre lavorazioni? ")
                # if proseguire.lower() in ["s","si","sì"]:
                #     print("Continuiamo!")
                # else:
                #     print("Arrivederci!")
                #     break
        
        #     except Exception as e:
        #         print(e)

        # Metodo per la lista delle lavorazioni? 
        