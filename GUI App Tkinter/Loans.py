import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

class Loan():

    def __init__(self,parent):
        self.parent = parent
        self.db = mysql.connector.connect(
            host="localhost",    
            user="root",    
            password="",
            database="nuova_biblioteca" 
        )
        self.cursor = self.db.cursor()

    def add_loan(self):
        self.window = tk.Toplevel(self.parent)
        self.window.title("Inserisci Prestito")
        self.window.geometry("300x200")
        self.window.grab_set()
        self.window.transient(self.parent)

        label_user_id = tk.Label(self.window, text="Utente ID: ")
        self.entry_user_id = tk.Entry(self.window)

        label_book_id = tk.Label(self.window, text="Libro ID: ")
        self.entry_book_id = tk.Entry(self.window)

        label_loan_date = tk.Label(self.window,text="Inizio Prestito: ")
        self.entry_loan_date = tk.Entry(self.window)

        label_return_date = tk.Label(self.window,text="Termine Prestito: ")
        self.entry_return_date = tk.Entry(self.window)

        label_status = tk.Label(self.window,text="Stato: ")
        self.entry_status= tk.Entry(self.window)

        label_user_id.grid(row=0, column=0)
        self.entry_user_id.grid(row=0, column=1)
        
        label_book_id.grid(row=1, column=0)
        self.entry_book_id.grid(row=1, column=1)
        
        label_loan_date.grid(row=2, column=0)
        self.entry_loan_date.grid(row=2, column=1)
        
        label_return_date.grid(row=3, column=0)
        self.entry_return_date.grid(row=3, column=1)
        
        label_status.grid(row=4, column=0)
        self.entry_status.grid(row=4, column=1)

        button_add = tk.Button(self.window, text="Aggiungi Libro", command=self.add_loan_to_db,background="green")
        button_add.grid(row=5,column=1,pady=2)

        button_exit = tk.Button(self.window, text="Esci dalla sessione", command=self.window.destroy,background="red")
        button_exit.grid(row=6,column=1,pady=2)

    def add_loan_to_db(self):
        user_id = self.entry_user_id.get()
        book_id = self.entry_book_id.get()
        loan_start = self.entry_loan_date.get()
        loan_end = self.entry_return_date.get()
        status = self.entry_status.get()

        query = "INSERT INTO Prestiti (UTENTE_ID,LIBRO_ID,DATA_PRESTITO,DATA_RESTITUZIONE,STATO) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id,book_id,loan_start,loan_end,status)

        self.cursor.execute(query,values)
        self.db.commit()
        messagebox.showinfo("Successo", "Prestito aggiunto con successo")
        self.parent.deiconify()
        self.window.destroy()

    def remove_loan(self):
        self.remove_window = tk.Toplevel(self.parent)
        self.remove_window.title("Rimuovi Prestito")
        self.remove_window.geometry("300x200")
        self.remove_window.grab_set()
        self.remove_window.transient(self.parent)

        label_id = tk.Label(self.remove_window, text="ID Prestito: ")
        self.entry_id = tk.Entry(self.remove_window)

        label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)

        button_remove = tk.Button(self.remove_window, text="Rimuovi prestito", command=self.remove_loan_from_db, background="red")
        button_remove.grid(row=1, column=1, pady=2)

        button_exit = tk.Button(self.remove_window, text="Esci", command=self.remove_window.destroy, background="green")
        button_exit.grid(row=2, column=1, pady=2)

    def remove_loan_from_db(self):
        loan_id = self.entry_id.get()

        check_query = "SELECT COUNT(*) FROM Prestiti WHERE ID = %s"
        self.cursor.execute(check_query, (loan_id,))
        if self.cursor.fetchone()[0] == 0:
            messagebox.showerror("Errore", "Prestito non trovato.")
            return

        if messagebox.askyesno("Conferma", "Sei sicuro di voler rimuovere questa prestito?"):
            delete_query = "DELETE FROM Prestiti WHERE ID = %s"
            try:
                self.cursor.execute(delete_query, (loan_id,))
                self.db.commit()
                messagebox.showinfo("Successo", "Prestito rimosso con successo")
            except Exception as e:
                messagebox.showerror("Errore", f"Si è verificato un errore durante la rimozione del prestito: {e}")
            finally:
                if self.remove_window:
                    self.remove_window.destroy()
        else:
            messagebox.showinfo("Annullato", "Operazione di rimozione annullata")


    def view_loans(self):

        view_window = tk.Toplevel(self.parent)
        view_window.title("Visualizza Prestiti")
        view_window.geometry("800x600")

        tree = ttk.Treeview(view_window, columns=('ID Prestito','UtenteID', 'LibroID','Data Inizio Prestito','Data Fine Prestito',
                                                  'Stato'), show='headings')

        tree.heading('ID Prestito', text='ID Prestito')
        tree.heading('UtenteID', text='UtenteID')
        tree.heading('LibroID', text='LibroID')
        tree.heading('Data Inizio Prestito', text='Data Inizio Prestito')
        tree.heading('Data Fine Prestito', text='Data Fine Prestito')
        tree.heading('Stato', text='Stato')


        cursor = self.cursor
        query = "SELECT ID,UTENTE_ID,LIBRO_ID,DATA_PRESTITO,DATA_RESTITUZIONE,STATO FROM Prestiti"
        cursor.execute(query)
        risultati = cursor.fetchall()

        for row in risultati:
            tree.insert('', 'end', values=row)

        tree.pack(expand=True, fill='both')

        close_button = tk.Button(view_window, text="Chiudi", command=view_window.destroy)
        close_button.pack(side='bottom')

    def update_loan(self):
        pass

    