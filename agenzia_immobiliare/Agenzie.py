from Case import Casa

class Agenzia():
    # attributo
    _immobili_gestiti = dict()
    _codici_immobili = set()
    # Costruttore
    def __init__(self):
        self._immobili_gestiti = dict()
        self._codici_immobili = set()
    # Metodo di creazione e aggiunta Casa 

    def createHome(self):
        immobile: Casa
        k = True
        while k:
            try:
                immobile = Casa(self.randomCode(), float(input("Prezzo di vendita: ").strip()), int(input("Numeri vani: ").strip()),
                            self.booleanInput("Sta in un condomio? S/N: "), self.booleanInput("Ha il garage? S/N: "),
                            self.booleanInput("Ha l'ascensore? S/N: "))
                
                self._codici_immobili.add(immobile._codice)
                self._immobili_gestiti[immobile._codice] = immobile
                # aggiungi eccezione
                if self.goForward():
                    print("Prosegui pure!")
                else:
                    print("Arrivederci!")
                    k = False
            
            except ValueError:
                print("Il prezzo di vendita e i vani sono valori numerici interi")
            except Exception as e:
                print(e)
    
    # Metodo di creazione binario

    def createBinary(self):
        import pickle
        try:
            
            with open('file_binario.bin','ab') as file_binario:
                for codice, immobile in self._immobili_gestiti.items():
                    pickle.dump((codice,immobile),file_binario)
            
            print("File generato con successo!")
        
        except Exception as e:
            print(e)

    # Metodo stampa a schermo catalogo

    def stampHomeCatalog(self):
        try:
            
            print("Stampa degli immobili a catalogo: ")
            for immobile in self._immobili_gestiti.values():
                print(str(immobile))
        
        except Exception as e:
            print(e)
            
        

    # Metodo ricerca case per range di prezzo 

    def searchHomeForRange(self,range1:int,range2:int):
        
        try:
                #filter? 

                counter = 0
                for immobile in self._immobili_gestiti.values():
                    if range1 <= immobile.getPrice() <= range2:
                        print(str(immobile))
                        counter += 1
                
                if counter == 0:
                    print("Edifici non presenti per intervallo di prezzo specificato")

        except Exception as e:
            print(e)

    def goForward(self):
        user_choice = input("Vuoi proseguire? S/N: ")

        if user_choice in ['si','sì','s']:
            return True
        else:
            return False

    def randomCode(self):
        import string
        import random
        
        N = 8
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))       
        return str(res)
    
    def booleanInput(self,request):
        while True:
            user_input = input(request).strip().lower()
            if user_input == 'si':
                return True
            elif user_input == 'no':
                return False
            else:
                print("Risposta non valida, si accetta solo si o no.")


