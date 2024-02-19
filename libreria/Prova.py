from Clienti import Cliente
from Librerie import Libreria

def main():
    
    libreria_coop = Libreria()
    print("Benvenuto nel menù di scelta")
    x = True
    while x:
        try:
            print(f"""Hai a disposizione le seguenti opzioni:
                      1) aggiungi cliente
                      2) rimuovi cliente
                      3) aggiorna spesa cliente
                      4) premio fedeltà(azzera spesa corrente)
                      5) azzera lista clienti
                      6) spesa media per cliente
                      7) esci
                      Digita il numero corrispondente (1/2/3 ecc.)""")
            
            user_choice = input("Fai la tua scelta: ")
            
            if user_choice.lower() == "1":
                libreria_coop.addCustomer()
            elif user_choice.lower() == "2":
                libreria_coop.removeCustomer()
            elif user_choice.lower() == "3":
                libreria_coop.customerCharge()
            elif user_choice.lower() == "4":
                premio = int(input("Inserisci la soglia premio: "))
                libreria_coop.customerAward(premio)
            elif user_choice.lower() == "5":
                libreria_coop.removeCustomersList(libreria_coop.lista_clienti)
            elif user_choice.lower() == "6":
                libreria_coop.customersStats()
            elif user_choice.lower() == "7":
                print("Arrivederci!")
                exit()
            else:
                raise Exception("Attieniti alle opzioni indicate!")
            
            still_going = input("Hai altre operazioni da eseguire? S/N: ")
            if still_going.lower() in ["sì",'si','s','yes','y']:
                print("Prosegui nelle tue attività")
            else:
                print("Arrivederci!")
                x = False

        except ValueError:
            print("Inserire soglie premio in numeri interi")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()