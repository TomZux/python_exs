from BaseMenu import MenuBase
import tkinter as tk
from Users import User

class MenuUsers(MenuBase):
    def __init__(self, parent):
        self.users_managment = User(self)
        super().__init__(parent, "Gestione Utenti", "lightblue")
    
    def add_buttons(self):
        tk.Button(self, text="Aggiungi Utente", command=self.users_managment.add_user, bg="lightgreen", width=20, height=2, font="Italic").pack(pady=20)
        tk.Button(self, text="Rimuovi Utente",command=self.users_managment.remove_user,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Verifica Lista Utenti",command=self.users_managment.view_users,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Aggiorna Utente",command=self.users_managment.update_user,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        