import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

class Book():

    def __init__(self,parent):
        self.parent = parent
        self.db = mysql.connector.connect(
            host="localhost",    
            user="root",    
            password="",
            database="nuova_biblioteca" 
        )
        self.cursor = self.db.cursor()

    
    def add_book(self):
        self.window = tk.Toplevel(self.parent)
        self.window.title("Inserisci Libro")
        self.window.geometry("300x200")
        self.window.grab_set()
        self.window.transient(self.parent)

        label_title = tk.Label(self.window, text="Titolo: ")
        self.entry_title = tk.Entry(self.window)

        label_author = tk.Label(self.window, text="Autore: ")
        self.entry_author = tk.Entry(self.window)

        label_isbn = tk.Label(self.window,text="ISBN: ")
        self.entry_isbn = tk.Entry(self.window)

        label_year = tk.Label(self.window,text="Anno di pubblicazione: ")
        self.entry_year = tk.Entry(self.window)

        label_amount = tk.Label(self.window,text="Quantità disponibile: ")
        self.entry_amount= tk.Entry(self.window)

        label_category_id = tk.Label(self.window,text="ID Categoria: ")
        self.entry_category_id= tk.Entry(self.window)

        label_title.grid(row=0, column=0)
        self.entry_title.grid(row=0, column=1)
        
        label_author.grid(row=1, column=0)
        self.entry_author.grid(row=1, column=1)
        
        label_isbn.grid(row=2, column=0)
        self.entry_isbn.grid(row=2, column=1)
        
        label_year.grid(row=3, column=0)
        self.entry_year.grid(row=3, column=1)
        
        label_amount.grid(row=4, column=0)
        self.entry_amount.grid(row=4, column=1)

        label_category_id.grid(row=5, column=0)
        self.entry_category_id.grid(row=5,column=1)

        button_add = tk.Button(self.window, text="Aggiungi Libro", command=self.add_book_to_db,background="green")
        button_add.grid(row=6,column=1,pady=2)

        button_exit = tk.Button(self.window, text="Esci dalla sessione", command=self.window.destroy,background="red")
        button_exit.grid(row=7,column=1,pady=2)

    def add_book_to_db(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        isbn = self.entry_isbn.get()
        year = self.entry_year.get()
        amount = self.entry_amount.get()
        category_id = self.entry_category_id.get()

        query = "INSERT INTO Libri (TITOLO_LIBRO,AUTORE_LIBRO,ISBN,ANNO_PUBBLICAZIONE,QUANTITA_DISPONIBILE,CATEGORIA_ID) VALUES (%s, %s, %s, %s, %s,%s)"
        values = (title,author,isbn,year,amount,category_id)

        self.cursor.execute(query,values)
        self.db.commit()
        messagebox.showinfo("Successo", "Libro aggiunto con successo")
        self.parent.deiconify()
        self.window.destroy()

    def remove_book(self):
        self.remove_window = tk.Toplevel(self.parent)
        self.remove_window.title("Rimuovi Libro")
        self.remove_window.geometry("300x200")
        self.remove_window.grab_set()
        self.remove_window.transient(self.parent)

        label_id = tk.Label(self.remove_window, text="ID Libro: ")
        self.entry_id = tk.Entry(self.remove_window)

        label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)

        button_remove = tk.Button(self.remove_window, text="Rimuovi Libro", command=self.remove_book_from_db, background="red")
        button_remove.grid(row=1, column=1, pady=2)

        button_exit = tk.Button(self.remove_window, text="Esci", command=self.remove_window.destroy, background="green")
        button_exit.grid(row=2, column=1, pady=2)

    def remove_book_from_db(self):
        book_id = self.entry_id.get()

        check_query = "SELECT COUNT(*) FROM Libri WHERE ID = %s"
        self.cursor.execute(check_query, (book_id,))
        if self.cursor.fetchone()[0] == 0:
            messagebox.showerror("Errore", "Libro non trovato.")
            return

        if messagebox.askyesno("Conferma", "Sei sicuro di voler rimuovere questo Libro?"):
            delete_query = "DELETE FROM Libri WHERE ID = %s"
            try:
                self.cursor.execute(delete_query, (book_id,))
                self.db.commit()
                messagebox.showinfo("Successo", "Libro rimosso con successo")
            except Exception as e:
                messagebox.showerror("Errore", f"Si è verificato un errore durante la rimozione del Libro: {e}")
            finally:
                if self.remove_window:
                    self.remove_window.destroy()
        else:
            messagebox.showinfo("Annullato", "Operazione di rimozione annullata")


    def read_books(self):
        
        view_window = tk.Toplevel(self.parent)
        view_window.title("Visualizza Libri")
        view_window.geometry("800x600")

        tree = ttk.Treeview(view_window, columns=('ID Libro','Titolo Libro', 'Autore Libro','ISBN','Anno di pubblicazione',
                                                  'Quantità disponibile'), show='headings')

        tree.heading('ID Libro', text='ID Libro')
        tree.heading('Titolo Libro', text='Titolo Libro')
        tree.heading('Autore Libro', text='Autore Libro')
        tree.heading('ISBN', text='ISBN')
        tree.heading('Anno di pubblicazione', text='Anno di pubblicazione')
        tree.heading('Quantità disponibile', text='Quantità disponibile')


        cursor = self.cursor
        query = "SELECT ID,TITOLO_LIBRO,AUTORE_LIBRO,ISBN,ANNO_PUBBLICAZIONE,QUANTITA_DISPONIBILE FROM Libri"
        cursor.execute(query)
        risultati = cursor.fetchall()

        for row in risultati:
            tree.insert('', 'end', values=row)

        tree.pack(expand=True, fill='both')

        close_button = tk.Button(view_window, text="Chiudi", command=view_window.destroy)
        close_button.pack(side='bottom')

    def update_book(self):
        update_window = tk.Toplevel(self.parent)
        update_window.title("Aggiorna Libro")
        update_window.geometry("300x200")
        update_window.grab_set()
        update_window.transient(self.parent)

        label_id = tk.Label(update_window, text="ID Libro: ")
        entry_id = tk.Entry(update_window)
        label_id.grid(row=0, column=0)
        entry_id.grid(row=0, column=1)

        label_title = tk.Label(update_window, text="Titolo Libro: ")
        entry_title = tk.Entry(update_window)

        label_author = tk.Label(update_window, text="Autore Libro: ")
        entry_author = tk.Entry(update_window)

        label_isbn = tk.Label(update_window, text="ISBN: ")
        entry_isbn = tk.Entry(update_window)

        label_year = tk.Label(update_window, text="Anno di pubblicazione: ")
        entry_year = tk.Entry(update_window)

        label_amount = tk.Label(update_window, text="Quantità disponibile: ")
        entry_amount = tk.Entry(update_window)

        label_category_id = tk.Label(update_window, text="ID Categoria: ")
        entry_category_id = tk.Entry(update_window)

        label_title.grid(row=1, column=0)
        entry_title.grid(row=1, column=1)

        label_author.grid(row=2, column=0)
        entry_author.grid(row=2, column=1)

        label_isbn.grid(row=3, column= 0)
        entry_isbn.grid(row=3, column=1)

        label_year.grid(row=4, column= 0)
        entry_year.grid(row=4, column=1)

        label_amount.grid(row=5, column=0)
        entry_amount.grid(row=5, column=1)

        label_category_id.grid(row=6, column=0)
        entry_category_id.grid(row=6, column=1)

        def perform_update():
            book_id = entry_id.get()
            updated_title = entry_title.get()
            updated_author = entry_author.get()
            updated_isbn = entry_isbn.get()
            updated_year = entry_year.get()
            updated_amount = entry_amount.get()
            updated_category = entry_category_id.get()

            query = "UPDATE Libri SET TITOLO_LIBRO = %s, AUTORE_LIBRO = %s, \
                    ISBN = %s, ANNO_PUBBLICAZIONE = %s, QUANTITA_DISPONIBILE = %s, CATEGORIA_ID = %s \
                    WHERE ID = %s"
            values = (updated_title, updated_author, updated_isbn, updated_year, updated_amount, updated_category, book_id)

            try:
                self.cursor.execute(query, values)
                self.db.commit()
                messagebox.showinfo("Successo", "Libro aggiornato con successo")
                update_window.destroy()
            except Exception as e:
                messagebox.showerror("Errore", f"Si è verificato un errore durante l'aggiornamento: {e}")
            
        update_button = tk.Button(update_window, text="Aggiorna", command=perform_update)
        update_button.grid(row=7, column=1, pady=2)

