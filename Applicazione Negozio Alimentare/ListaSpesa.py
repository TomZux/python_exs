from Prodotti import Prodotti
from Alimentari import Alimentari
from NonAlimentari import NonAlimentari
from datetime import datetime

class ListaSpesa():
    # attributi
    lista_della_spesa: list
    scontrino: float
    carta_fedeltà: bool
    # Costruttore
    def __init__(self):
        self.lista_della_spesa = [Prodotti]
        self.scontrino = 0
        self.carta_fedeltà = False
    # metodo aggiunta articoli spesa
    def aggiungiArticoli(self):
        while True:
            prodotto: Prodotti
            try:
                enter_user = input("Che prodotto stai aggiungendo? A = alimentare, N = non alimentare, P = prodotto generico: ")
                if enter_user.lower() == "a":
                    prodotto = Alimentari(input("Barcode: "),input("Descrizione: "),float(input("Prezzo: ")),input("Data di scadenza: "))
                elif enter_user.lower() == "n":
                    prodotto = NonAlimentari(input("Barcode: "),input("Descrizione: "),float(input("Prezzo: ")),input("Materiale: "))
                elif enter_user.lower() == "p":
                    prodotto = Prodotti(input("Barcode: "),input("Descrizione: "),float(input("Prezzo: ")))
                else:
                    print("Attieniti al menù")

                self.lista_della_spesa.append(prodotto)

                goForward = input("Desideri inserire altri articoli? S/N: ")
                if goForward.lower() in ['s','si','sì']:
                    print("Prosegui pure")
                else:
                    print("Arrivederci!")
                    break

            except Exception as e:
                print(e)
    
    # metodo totale articoli
    
    def totaleScontrino(self):
        return (f"Il totale è pari a {self.scontrino} euro")
    
    # metodo annulla ed esci

    def annullaSpesa(self):
        self.scontrino = 0
        return("Spesa annullata, arrivederci")