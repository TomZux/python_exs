from Agenzie import Agenzia
from Case import Casa


def main():
    
    tecnocasa = Agenzia()
    
    print("Benvenuto nel menù di scelta, ecco le opzioni disponibili: ")
    x = True
    while x:
        try:
            menù = input("""
                            1) Aggiungi immobile
                            2) Salva su file binario tutti gli immobili gestiti
                            3) Stampa a schermo il catalogo immobili gestiti
                            4) Ricerca immobili per intervallo di prezzo
                            5) Esci
                            Fai la tua scelta, digita 1 oppure 2, eccetera: """)
            
            if menù == "1":
                tecnocasa.createHome()
            elif menù == "2":
                
                if len(tecnocasa._immobili_gestiti) == 0:
                        raise Exception("Non ci sono immobili in gestione. Aggiungi prima edifici.")
                
                tecnocasa.createBinary()

            elif menù == "3":

                if len(tecnocasa._immobili_gestiti) == 0:
                        raise Exception("Non ci sono immobili in gestione. Aggiungi prima edifici.")
                
                tecnocasa.stampHomeCatalog()

            elif menù == "4":
                try:
                    
                    if len(tecnocasa._immobili_gestiti) == 0:
                        raise Exception("Non ci sono immobili in gestione. Aggiungi prima edifici.")

                    first_num = int(input("Inserisci il prezzo minimo: ").strip())
                    last_num = int(input("Inserisci il prezzo massimo: ").strip())

                    if first_num >= last_num:
                        raise Exception("Il prezzo minimo non può essere maggiore o uguale del prezzo massimo")
                    
                    tecnocasa.searchHomeForRange(first_num,last_num)

                except ValueError:
                    raise Exception("Input non valido.")
                except Exception as e:
                    print(e)

            elif menù == "5":
                print("Arrivederci!")
                exit()
            else:
                raise Exception("Rispetta il menù indicato. Scelta non valida.")


        except Exception as e:
            print(e)




if __name__ == "__main__":
    main()