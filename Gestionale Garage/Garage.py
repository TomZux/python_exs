

from Auto import Auto
from Furgone import Furgone
from Moto import Moto
from Veicolo import Veicolo


class Garage():
    # attributi
    posti_parcheggio_liberi = int
    parcheggio = list[Veicolo]
    # Costruttore
    def __init__(self):
        self.posti_parcheggio_liberi = 15
        self.parcheggio = []
        for i in range(0,self.posti_parcheggio_liberi):
            self.parcheggio.append(None)
    
    def newVehicle(self):
        veicolo: Veicolo
        while True: 
            try:

                if self.posti_parcheggio_liberi == 0:
                    print("Posti esauriti")
                    break

                enter_user = input("Quale veicolo sta entrando? A= Auto, M= Moto, F= Furgone: ")
                if enter_user.lower() == "a":
                    veicolo = Auto(input("Marca: "),input("Anno: "),input("Cilindrata: "), input("Porte: "), input("Alimentazione: "))
                elif enter_user.lower() == "m": 
                    veicolo = Moto(input("Marca: "),input("Anno: "),input("Cilindrata: "), input("Tempi: "))
                elif enter_user.lower() == "f":
                    veicolo = Furgone(input("Marca: "),input("Anno: "),input("Cilindrata: "), input("Capacità: "))
                else:
                    print("Attieniti al menù!")
                
                posto = self.postoLibero()
                if posto != -1:
                    self.parcheggio[posto] = veicolo
                    print(f"Il veicolo è parcheggiato al posto nr {posto}")
                else:
                    print("Posti esauriti")

                self.posti_parcheggio_liberi -= 1

                continua_inserire = input("Entrano altri veicoli? ")
                if continua_inserire.lower() in ["si","sì","s"]:
                    print("Continuiamo!")
                else:
                    print("Continua nel menù")
                    break 
            except Exception as e:
                print(e)

    def postoLibero(self):
        posto = -1
        for i in range(0,len(self.parcheggio)):
            if self.parcheggio[i] == None:
                posto = i
                break
        return posto      

    def parkingPlace(self, posto):
        if 0 <= posto < len(self.parcheggio):
            veicolo = self.parcheggio[posto] 
            if veicolo != None:
                self.parcheggio[posto] = None
                self.posti_parcheggio_liberi += 1
                print(f"""Rimuovo il veicolo""" + veicolo.toString() + f""" dal posto {posto}""")
            else:
                print("Il posto specificato è vuoto.")
        else:
            print("Il posto specificato non è valido.")


    def currentSituation(self):
        situazione_parcheggio = f"""
        Nel parcheggio sono disponibili nr {self.posti_parcheggio_liberi} posti liberi
        e nr {self.postoLibero()} occupati.
        """
        print(situazione_parcheggio)



def main():
    
    garage = Garage()
    
    while True:
            try:
                print(f"""
                    Scegli fra le seguenti opzioni:
                    1) Inserisci un nuovo veicolo
                    2) Estrazione dal garage del veicolo che occupa un determinato posto
                    3) Stampa della situazione corrente dei posti nel garage veicolo
                    4) Esci
                    """)
                user_choice = input("Fai la tua scelta: ")

                if user_choice == '1':
                    garage.newVehicle()
                elif user_choice == '2':
                    user_entry = int(input("Inserisci nr posteggio: "))
                    garage.parkingPlace(user_entry)
                elif user_choice == '3':
                    garage.currentSituation()
                elif user_choice == '4':
                    print("Arrivederci!")
                    break
                else:
                    print("Attieniti al menù!")
                
                goForward = input("Vuoi proseguire? ")
                if goForward.lower() in ["s","si","sì"]:
                    print("Continuiamo!")
                else:
                    print("Arrivederci!")
                    break
            except:
                print("Contattare l'assistenza")

    
if __name__ == "__main__":
    main()

