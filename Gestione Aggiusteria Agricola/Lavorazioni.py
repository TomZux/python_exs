from Apparecchio import Apparecchio
from Decespugliatore import Decespugliatore
from Motozappa import Motozappa
from Tosaerba import Tosaerba
from Aggiusteria import Aggiusteria

def main():
    
    aggiusteria = Aggiusteria()

    while True:
        try:
            print(f"""
                    Scegli fra le seguenti opzioni:
                    1) Inserisci un nuovo apparecchio da riparare
                    2) Uscita apparecchio riparato
                    3) Aggiunta lavorazioni all'apparecchio da riparare
                    4) Costo totale lavorazioni per apparecchio
                    5) Lista riparazioni per apparecchio
                    6) Uscita dal menù
                    """)
            user_choice = input("Fai la tua scelta: ")

            if user_choice == "1":
                aggiusteria.newApparatus()
            elif user_choice == "2":
                user_space = int(input("Inserisci lo spazio riparazione: "))
                aggiusteria.uscitaApparecchioRiparato(user_space)
            elif user_choice == "3":
                user_space = int(input("Inserisci lo spazio riparazione: "))
                aggiusteria.aggiunta_lavorazioni(user_space)
            elif user_choice == "4":
                user_space = int(input("Inserisci lo spazio riparazione: "))
                aggiusteria.totaleLavorazioni(user_space)
            elif user_choice == "5":
                user_space = int(input("Inserisci lo spazio riparazione: "))
                aggiusteria.riparazioniPerApparecchio(user_space)
            elif user_choice == "6":
                print("Arrivederci!")
                break
            else:
                print("Prego, attenersi alle possibilità indicate")
            
            continuare = input("Vuoi proseguire? ")
            if continuare.lower() in ["s","si","sì"]:
                print("Continuiamo!")
            else:
                print("Arrivederci!")
                break


        except Exception as e:
            print(e)










if __name__ == "__main__":
    main()