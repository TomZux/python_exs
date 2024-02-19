import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

class Category():

    def __init__(self,parent):
        self.parent = parent
        self.db = mysql.connector.connect(
            host="localhost",    
            user="root",    
            password="",
            database="nuova_biblioteca" 
        )
        self.cursor = self.db.cursor()

    def add_category(self):
        self.window = tk.Toplevel(self.parent)
        self.window.title("Inserisci Categoria")
        self.window.geometry("300x200")
        self.window.grab_set()
        self.window.transient(self.parent)

        label_name = tk.Label(self.window, text="Nome Categoria: ")
        self.entry_name = tk.Entry(self.window)

        label_description = tk.Label(self.window, text="Descrizione Categoria: ")
        self.entry_description = tk.Entry(self.window)

        label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        
        label_description.grid(row=1, column=0)
        self.entry_description.grid(row=1, column=1)

        button_add = tk.Button(self.window, text="Aggiungi Categoria", command=self.add_category_to_db,background="green")
        button_add.grid(row=5,column=1,pady=2)

        button_exit = tk.Button(self.window, text="Esci dalla sessione", command=self.window.destroy,background="red")
        button_exit.grid(row=6,column=1,pady=2)

        self.window.wait_window() # grazie Fernanda!!!!! <3 

    
    def add_category_to_db(self):
        name = self.entry_name.get()
        description = self.entry_description.get()

        query = "INSERT INTO Categorie (NOME_CATEGORIA,DESCRIZIONE_CATEGORIA) VALUES (%s, %s)"
        values = (name,description)

        self.cursor.execute(query,values)
        self.db.commit()
        messagebox.showinfo("Successo", "Categoria aggiunta con successo")
        self.parent.deiconify()
        self.window.destroy()


    def remove_category(self):
        self.remove_window = tk.Toplevel(self.parent)
        self.remove_window.title("Rimuovi Categoria")
        self.remove_window.geometry("300x200")
        self.remove_window.grab_set()
        self.remove_window.transient(self.parent)

        label_id = tk.Label(self.remove_window, text="ID Categoria: ")
        self.entry_id = tk.Entry(self.remove_window)

        label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)

        button_remove = tk.Button(self.remove_window, text="Rimuovi Categoria", command=self.remove_category_from_db, background="red")
        button_remove.grid(row=1, column=1, pady=2)

        button_exit = tk.Button(self.remove_window, text="Esci", command=self.remove_window.destroy, background="green")
        button_exit.grid(row=2, column=1, pady=2)

    def remove_category_from_db(self):
        category_id = self.entry_id.get()

        check_query = "SELECT COUNT(*) FROM Categorie WHERE ID = %s"
        self.cursor.execute(check_query, (category_id,))
        if self.cursor.fetchone()[0] == 0:
            messagebox.showerror("Errore", "Categoria non trovata.")
            return

        if messagebox.askyesno("Conferma", "Sei sicuro di voler rimuovere questa categoria?"):
            delete_query = "DELETE FROM Categorie WHERE ID = %s"
            try:
                self.cursor.execute(delete_query, (category_id,))
                self.db.commit()
                messagebox.showinfo("Successo", "Categoria rimossa con successo")
            except Exception as e:
                messagebox.showerror("Errore", f"Si è verificato un errore durante la rimozione della categoria: {e}")
            finally:
                if self.remove_window:
                    self.remove_window.destroy()
        else:
            messagebox.showinfo("Annullato", "Operazione di rimozione annullata")

    def read_categories(self):
        
        view_window = tk.Toplevel(self.parent)
        view_window.title("Visualizza Categorie")
        view_window.geometry("600x400")

        tree = ttk.Treeview(view_window, columns=('ID Categoria','Nome Categoria', 'Descrizione Categoria'), show='headings')

        tree.heading('ID Categoria', text='ID Categoria')
        tree.heading('Nome Categoria', text='Nome Categoria')
        tree.heading('Descrizione Categoria', text='Descrizione Categoria')

        cursor = self.cursor
        query = "SELECT ID,NOME_CATEGORIA,DESCRIZIONE_CATEGORIA FROM Categorie"
        cursor.execute(query)
        risultati = cursor.fetchall()

        for row in risultati:
            tree.insert('', 'end', values=row)

        tree.pack(expand=True, fill='both')

        close_button = tk.Button(view_window, text="Chiudi", command=view_window.destroy)
        close_button.pack(side='bottom')

    def update_category(self):
        update_window = tk.Toplevel(self.parent)
        update_window.title("Aggiorna Categoria")
        update_window.geometry("300x200")
        update_window.grab_set()
        update_window.transient(self.parent)

        label_id = tk.Label(update_window, text="ID Categoria: ")
        entry_id = tk.Entry(update_window)
        label_id.grid(row=0, column=0)
        entry_id.grid(row=0, column=1)

        label_name = tk.Label(update_window, text="Nome Categoria: ")
        entry_name = tk.Entry(update_window)

        label_description = tk.Label(update_window, text="Descrizione Categoria: ")
        entry_description = tk.Entry(update_window)

        label_name.grid(row=1, column=0)
        entry_name.grid(row=1, column=1)

        label_description.grid(row=2, column=0)
        entry_description.grid(row=2, column=1)

        def perform_update():
            category_id = entry_id.get()
            updated_name = entry_name.get()
            updated_description = entry_description.get()

            query = "UPDATE Categorie SET NOME_CATEGORIA = %s, DESCRIZIONE_CATEGORIA = %s WHERE ID = %s"
            values = (updated_name, updated_description, category_id)

            try:
                self.cursor.execute(query, values)
                self.db.commit()
                messagebox.showinfo("Successo", "Categoria aggiornata con successo")
                update_window.destroy()
            except Exception as e:
                messagebox.showerror("Errore", f"Si è verificato un errore durante l'aggiornamento: {e}")
            
        update_button = tk.Button(update_window, text="Aggiorna", command=perform_update)
        update_button.grid(row=3, column=1, pady=2)

   





    