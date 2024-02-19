from BaseMenu import MenuBase
import tkinter as tk
from Categories import Category

class MenuCategories(MenuBase):

    def __init__(self, parent):
        self.categories_managment = Category(self)
        super().__init__(parent, "Gestione Categorie", "lightblue")

    def add_buttons(self):
        tk.Button(self, text="Aggiungi Categoria", command=self.categories_managment.add_category, bg="lightgreen", width=20, height=2, font="Italic").pack(pady=20)
        tk.Button(self, text="Rimuovi Categoria",command=self.categories_managment.remove_category,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Verifica Lista Categorie",command=self.categories_managment.read_categories,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Aggiorna Categoria",command=self.categories_managment.update_category,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)