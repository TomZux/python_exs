from Prodotti import Prodotti
from Alimentari import Alimentari
from NonAlimentari import NonAlimentari
from ListaSpesa import ListaSpesa

def main():
    
    spesa = ListaSpesa()

    user_card = input("Benvenuto! Hai la nostra carta fedeltà? S/N: ")

    if user_card.lower() in ['si','sì','s']:
        spesa.carta_fedeltà = True
    else:
        print("Prosegui senza i nostri fantastici sconti")

   
    while True:

        print(f"""Ecco le scelte a tua disposizione: 
                    1) Aggiungi articoli allo scontrino
                    2) Verifica l'importo totale
                    3) Annulla ed esci      
                """)
        
        user_choice = input("Prego, inserire la scelta: ")
        
        if user_choice == "1":
            spesa.aggiungiArticoli()
        elif user_choice == "2":
            print(spesa.totaleScontrino())
        elif user_choice == "3":
            print(spesa.annullaSpesa())
            break
        else:
            print("Attieniti alle scelte consentite")

        for item in spesa.lista_della_spesa:
            if isinstance(item, Alimentari) and spesa.carta_fedeltà:
                spesa.scontrino += item.applicaSconto()
                # print(item.toString())
            elif isinstance(item, NonAlimentari) and spesa.carta_fedeltà:
                spesa.scontrino += item.applicaSconto()
                # print(item.toString())
            elif isinstance(item, Prodotti) and spesa.carta_fedeltà:
                spesa.scontrino += item.applicaSconto()
                # print(item.toString())
            if isinstance(item, Alimentari) and spesa.carta_fedeltà == False:
                spesa.scontrino += item.prezzo
                # print(item.toString())
            elif isinstance(item, NonAlimentari) and spesa.carta_fedeltà == False:
                spesa.scontrino += item.prezzo
                # print(item.toString())
            elif isinstance(item, Prodotti) and spesa.carta_fedeltà == False:
                spesa.scontrino += item.prezzo
                # print(item.toString())

        goForward = input("Desideri proseguire? S/N: ")
        if goForward.lower() in ['s','si','sì']:
            print("Prosegui pure")
        else:
            print("Arrivederci!")
            break


if __name__ == "__main__":
    main()