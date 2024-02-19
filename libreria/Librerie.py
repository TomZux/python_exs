from Clienti import Cliente

class Libreria():
    # attributo
    lista_clienti: list
    codici_clienti: set
    # costruttore
    def __init__(self):
        self.lista_clienti = []
        self.codici_clienti = set()
    # Metodo aggiungi cliente
    def addCustomer(self):
        acquirente: Cliente
        y = True
        while y:
            try:
                print("Inserisci il codice cliente")
                acquirente = Cliente(input("Codice ID: "))

                if acquirente.codice in self.codici_clienti:
                    raise Exception("Codice già presente a database. Non sono possibili duplicati\n")
                else:
                    self.codici_clienti.add(acquirente.codice)
                    self.lista_clienti.append(acquirente)
                    print("Codice cliente aggiunto a database\n")

                add_again = input("Vuoi inserire altri clienti? S/N: ")

                if add_again.lower() in ["sì",'si','s','yes','y']:
                    print("Prosegui nelle tue attività")
                else:
                    print("Arrivederci!")
                    y = False

            except Exception as e:
                print(e)
    # Metodo rimuovi cliente
    def removeCustomer(self):

        k= True
        while k:
            try:

                if len(self.lista_clienti) == 0:
                    print("Non sono presenti clienti a database. Operazione non consentita\n")
                    k = False
                else:
                    user_need = input("Inserisci il codice cliente da rimuovere: ")

                    if user_need in self.codici_clienti:
                        self.codici_clienti.remove(user_need)
                        for cliente in self.lista_clienti:
                            if cliente.getCodice() == user_need:
                                self.lista_clienti.remove(cliente)
                                print(f"Cliente, codice {user_need} rimosso con successo\n")
                    else:
                        print(f"Codice {user_need} non trovato")

                delete_again = input("Vuoi eliminare altri codici cliente? S/N: ")

                if delete_again.lower() in ["sì",'si','s','yes','y']:
                    print("Prosegui nelle tue attività")
                else:
                    print("Arrivederci!")
                    k = False
            
            except Exception as e:
                print(e)
    # Metodo spesa cliente
    def customerCharge(self):
        
        while True:
            try:

                if len(self.lista_clienti) == 0:
                    print("Non sono presenti clienti a database. Operazione non consentita\n")
                    return

                customer_id = input("Inserisci codice cliente: ")

                if customer_id not in self.codici_clienti:
                    raise Exception("Codice cliente errato. Ritenta o aggiungi cliente\n")
                    
                euro_charge = int(input("Inserisci spesa in euro: "))
                cents_charge = int(input("Inserisci spesa in centesimi: "))

                if euro_charge < 0 or cents_charge < 0:
                    raise Exception("I numeri inseriti devono essere positivi\n")

                for cliente in self.lista_clienti:
                    if cliente.getCodice() == customer_id:
                        cliente.spesaEuro += euro_charge
                        cliente.spesaCentesimi += cents_charge
                        if cliente.spesaCentesimi >= 100:
                            cliente.spesaEuro += cliente.spesaCentesimi // 100
                            cliente.spesaCentesimi %= 100

                        print(f"Il cliente {customer_id}, ha una spesa in euro di {cliente.spesaEuro}, centesimi {cliente.spesaCentesimi}\n")

                charge_again = input("Vuoi aggiornare altre spese per cliente? S/N: ")
                if charge_again.lower() in ["sì",'si','s','yes','y']:
                    print("Prosegui nelle tue attività")
                else:
                    print("Arrivederci!")
                    break
            except ValueError:
                print("Input non valido, inserire solo numeri interi\n")
            except Exception as e:
                print(e)

    # Metodo premio
    def customerAward(self,award):

        if len(self.lista_clienti) == 0:
                raise Exception("Non sono presenti clienti a database. Premio non applicabile\n")

        self.award = award

        clienti_premiati = []

        for cliente in self.lista_clienti:
            if cliente.getSpesaEuro() >= award:
                clienti_premiati.append(cliente)
                cliente.spesaEuro = 0
                cliente.spesaCentesimi = 0
        
        print(f"I seguenti fedeli clienti hanno la spesa azzerata: ")

        for i in clienti_premiati:
            print(i.getCodice())


    # Metodo rimuovi lista
    def removeCustomersList(self,lista_da_cancellare:list):

        if len(lista_da_cancellare) == 0:
            raise Exception("Database vuoto, popolarlo")
        
        user_last_warning = input("Sei sicuro di volere svuotare il DB? S/N ")
        if user_last_warning.lower() in ["si","sì","s"]:
            lista_da_cancellare.clear()
            print(f"Il DB ora è vuoto. Clienti pari a {len(lista_da_cancellare)}")
        else:
            print("Torno al menù")
            return
    
    # Metodo statistico - spesa media cliente
    def customersStats(self):
        totale: float
        try:

            if len(self.lista_clienti) == 0:
                raise Exception("Non sono presenti clienti a database. Media statistica non effettuabile\n")
            
            print(f"Son presenti a database nr {len(self.lista_clienti)} clienti.")

            totale = 0.0
            for cliente in self.lista_clienti:
                totale += cliente.getSpesaEuro() + cliente.getSpesaCentesimi() / 100
                
            print(f"La media delle spese è pari a {totale / len(self.lista_clienti)} euro")

        except Exception as e:
            print(e)
