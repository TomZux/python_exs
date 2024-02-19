import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from BooksMenu import MenuBooks
from UsersMenu import MenuUsers
from CategoriesMenu import MenuCategories
from LoansMenu import MenuLoans

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestione Biblioteca")
        self.geometry("500x550")
        self.configure(bg="cyan")
        self.resizable(False,False)

        tk.Button(self, text="Menù Libri", command=self.open_menu_books,bg="orange",width=20, height=2,font="Helvetica").pack(pady=20)
        tk.Button(self, text="Menù Utenti", command=self.open_menu_users,bg="orange",width=20, height=2,font="Helvetica").pack(pady=20)
        tk.Button(self, text="Menù Categorie", command=self.open_menu_categories,bg="orange",width=20, height=2,font="Helvetica").pack(pady=20)
        tk.Button(self, text="Menù Prestiti", command=self.open_menu_loans,bg="orange",width=20, height=2,font="Helvetica").pack(pady=20)
        tk.Button(self,text="Esci dal programma",command=self.close_window,bg="white",width=18, height=2,font="Helvetica").pack(pady=20)


    def open_menu_books(self):
        books_window = MenuBooks(self)
        books_window.protocol("WM_DELETE_WINDOW", self.window_close)

    def open_menu_users(self):
        books_window = MenuUsers(self)
        books_window.protocol("WM_DELETE_WINDOW", self.window_close)

    def open_menu_categories(self):
        books_window = MenuCategories(self)
        books_window.protocol("WM_DELETE_WINDOW", self.window_close)

    def open_menu_loans(self):
        books_window = MenuLoans(self)
        books_window.protocol("WM_DELETE_WINDOW", self.window_close)

    def window_close(self):
        self.deiconify()

    def close_window(self):
        user_input = messagebox.askyesno("ATTENZIONE!","Sei sicuro di volere uscire? ")
        if user_input:
            self.destroy()


app = MainWindow()
app.mainloop()
