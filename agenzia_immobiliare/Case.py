class Casa():
    # attributi
    _codice: str
    _prezzo_vendita: float
    _numero_vani: int
    _is_condo: bool
    _has_garage: bool
    _has_elevator: bool
    # Costruttore
    def __init__(self,codice,prezzo_vendita,numero_vani,is_condo,has_garage,has_elevator):
        self._codice = codice
        self._prezzo_vendita = prezzo_vendita
        self._numero_vani = numero_vani
        self._is_condo = is_condo
        self._has_garage = has_garage
        self._has_elevator = has_elevator
    # Metodi Getter e Setter

    def getCode(self):
        return self._codice

    def getPrice(self):
        return self._prezzo_vendita

    def getRooms(self):
        return self._numero_vani
    
    def getCondo(self):
        if self._is_condo == True:
            return 'si'
        elif self._is_condo == False:
            return 'no'

    def getGarage(self):
        if self._has_garage == True:
            return 'si'
        elif self._has_garage == False:
            return 'no'
    
    def getElevator(self):
        if self._has_elevator== True:
            return 'si'
        elif self._has_elevator == False:
            return 'no'
    
    def setPrice(self,new_price:float):
        try: 
            if new_price >= 0 and new_price != self._prezzo_vendita:
                self._prezzo_vendita = new_price
            else:
                return("Il prezzo di vendita non può essere negativo ")
            return self._prezzo_vendita
        except ValueError:
            return("Inserire un numero!")
        except Exception as e:
            return(e)
    
    def __str__(self)->str:
        return f"""Immobile codice {self._codice}, prezzo {self._prezzo_vendita},
        numero vani {self._numero_vani}. Si tratta di condominio: {self.getCondo()}.
        Ha il garage: {self.getGarage()}. Ha l'ascensore: {self.getElevator()}
        """
    