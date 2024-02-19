from Apparecchio import Apparecchio
from Decespugliatore import Decespugliatore
from Motozappa import Motozappa
from Tosaerba import Tosaerba


class Aggiusteria():
    # attributi
    spazi_riparazione: int
    officina: list[Apparecchio]
    # Costruttore
    def __init__(self):
        self.spazi_riparazione = 10
        self.officina = []
        for i in range(0,self.spazi_riparazione):
            self.officina.append(None)
    # Metodo per inserimento nuovo Apparecchio da riparare
    def newApparatus(self):
        apparatus: Apparecchio
        while True:
            try:

                enter_user = input("Quale veicolo sta entrando? D= Decespugliatore, M= Motozappa, T= Tosaerba: ")
                if enter_user.lower() == "d":
                    apparatus = Decespugliatore(input("ID: "),input("Marca: "),input("AE: ") )
                elif enter_user.lower() == "m":
                    apparatus = Motozappa(input("ID: "),input("Marca: "), input("Numero ruote: "))
                elif enter_user.lower() == "t":
                    apparatus = Tosaerba(input("ID: "),input("Marca: "), input("Numero ruote: "))
                else:
                    print("Attieniti alle opzioni indicate!")

                spazio = self.spazioRiparazioneLbero()
                if spazio != -1:
                    self.officina[spazio] = apparatus
                    print(f"L'apparecchio è nello spazio nr {spazio}")
                else:
                    print(f"Spazi riparazione esauriti")

                altre_riparazioni = input("Entrano altri apparecchi? ")
                if altre_riparazioni.lower() in ["si","sì","s"]:
                    print("Prego, proseguire nell'inserimento")
                else:
                    print("Continua nel menù")
                    break

            except Exception as e:
                print(e)
    
    # Metodo per uno spazio libero di riparazione
    def spazioRiparazioneLbero(self):
        spazio = -1
        for i in range(0,len(self.officina)):
            if self.officina[i] == None:
                spazio = i
                break
        return spazio
    
    # Metodo per uscita Apparecchio riparato
    def uscitaApparecchioRiparato(self,spazio):
        if 0 <= spazio < len(self.spazi_riparazione):
            apparatus = self.officina[spazio]
            if apparatus != None:
                self.officina[spazio] = None
                print(f""" Tolto l'apparecchio """ + apparatus.toString() + f""" dallo spazio {spazio}""")
            else:
                print("Lo spazio indicato è vuoto")
        else:
            print("Lo spazio indicato non è valido")

    # Metodo per aggiunta lavorazioni 

    def aggiunta_lavorazioni(self,spazio):
        apparatus: Apparecchio
        lista_di_lavori = []
        while True:
            try:
                if self.officina[spazio] == None:
                    print("Non è presente un apparecchio nello spazio indicato")
                # elif self.officina.count(None) == 10:
                #     print("Non ci sono apparecchi da riparare!")
                else:
                    apparatus = self.officina[spazio]
                    print(f"Sono possibili le seguenti lavorazioni: {apparatus.lavorazioni()}")
                    user_add = input("Quale lavorazione eseguire? ")
                    if user_add.lower() in apparatus.lavorazioni().keys():
                        # self.costo += apparatus.lavorazioni[user_add]
                        apparatus.costo += apparatus.lavorazioni().get(user_add)
                        lista_di_lavori.append((user_add,apparatus.lavorazioni().get(user_add)))
                    else:
                        print("Lavorazione non presente nel listino")
                    
                    # print(apparatus.costo)
                    # print(lista_di_lavori)
                    # print(apparatus.lista_lavorazioni)
                    
                    proseguire = input("Vuoi aggiungere altre lavorazioni? ")
                    if proseguire.lower() in ["s","si","sì"]:
                        print("Continuiamo!")
                    else:
                        print("Continua nel menù!")
                        apparatus.lista_lavorazioni.insert(0,lista_di_lavori)
                        break

            except Exception as e:
                print(e)

    # Metodo per costo totale lavorazioni

    def totaleLavorazioni(self,spazio):
        apparatus: Apparecchio

        try:
            if self.officina[spazio] == None:
                print("Non è presente un apparecchio nello spazio indicato")
                    
            else:
                apparatus = self.officina[spazio]
                print(f"Il costo della riparazione è pari a {apparatus.costo} euro")
        except Exception as e:
            print(e)

    # Metodo per lista lavorazione 

    def riparazioniPerApparecchio(self,spazio):
        apparatus: Apparecchio
        try:

            if self.officina[spazio] == None:
                print("Non è presente un apparecchio nello spazio indicato")
            else:
                apparatus = self.officina[spazio]
                # print(f"Lista delle lavorazioni effettuate: {apparatus.lista_lavorazioni}")
                print("Lavorazioni eseguite: ")
                for i in apparatus.lista_lavorazioni:
                    for j in i:
                        print(f"{j[0], j[1]}")
                
        except Exception as e:
            print(e)
