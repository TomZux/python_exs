from BaseMenu import MenuBase
import tkinter as tk
from Loans import Loan

class MenuLoans(MenuBase):

    def __init__(self, parent):
        self.loans_managment = Loan(self)
        super().__init__(parent, "Gestione Categorie", "lightblue")

    def add_buttons(self):
        tk.Button(self, text="Aggiungi Prestito", command=self.loans_managment.add_loan, bg="lightgreen", width=20, height=2, font="Italic").pack(pady=20)
        tk.Button(self, text="Rimuovi Prestito",command=self.loans_managment.remove_loan,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Verifica Lista Prestiti",command=self.loans_managment.view_loans,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Aggiorna Prestito",command=self.loans_managment.update_loan,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)