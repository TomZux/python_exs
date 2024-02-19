from BaseMenu import MenuBase
import tkinter as tk
from Books import Book

class MenuBooks(MenuBase):
    def __init__(self, parent):
        self.books_managment = Book(self)
        super().__init__(parent, "Gestione Libri", "lightblue")
        

    def add_buttons(self):
        tk.Button(self, text="Aggiungi Libro", command=self.books_managment.add_book, bg="lightgreen", width=20, height=2, font="Italic").pack(pady=20)
        tk.Button(self, text="Rimuovi Libro",command=self.books_managment.remove_book,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Verifica Lista Libri",command=self.books_managment.read_books,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
        tk.Button(self, text="Aggiorna Libro",command=self.books_managment.update_book,bg="lightgreen",width=20, height=2,font="Italic").pack(pady=20)
