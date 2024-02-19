import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

class User():

    def __init__(self,parent):
        self.parent = parent
        self.db = mysql.connector.connect(
            host="localhost",    
            user="root",    
            password="",
            database="nuova_biblioteca" 
        )
        self.cursor = self.db.cursor()

    def add_user(self):
        self.window = tk.Toplevel(self.parent)
        self.window.title("Inserisci Utente")
        self.window.geometry("300x200")
        self.window.grab_set()
        self.window.transient(self.parent)

        label_name = tk.Label(self.window, text="Nome Utente: ")
        self.entry_name = tk.Entry(self.window)

        label_surname = tk.Label(self.window, text="Cognome Utente: ")
        self.entry_surname = tk.Entry(self.window)

        label_address = tk.Label(self.window,text="Indirizzo Utente: ")
        self.entry_address = tk.Entry(self.window)

        label_email = tk.Label(self.window,text="Email Utente: ")
        self.entry_email = tk.Entry(self.window)

        label_phone = tk.Label(self.window,text="Cellulare Utente: ")
        self.entry_phone= tk.Entry(self.window)

        label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        
        label_surname.grid(row=1, column=0)
        self.entry_surname.grid(row=1, column=1)
        
        label_address.grid(row=2, column=0)
        self.entry_address.grid(row=2, column=1)
        
        label_email.grid(row=3, column=0)
        self.entry_email.grid(row=3, column=1)
        
        label_phone.grid(row=4, column=0)
        self.entry_phone.grid(row=4, column=1)

        button_add = tk.Button(self.window, text="Aggiungi Utente", command=self.add_user_to_db,background="green")
        button_add.grid(row=5,column=1,pady=2)

        button_exit = tk.Button(self.window, text="Esci dalla sessione", command=self.window.destroy,background="red")
        button_exit.grid(row=6,column=1,pady=2)
    
    def add_user_to_db(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        address = self.entry_address.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        query = "INSERT INTO Utenti (NOME_UTENTE,COGNOME_UTENTE,INDIRIZZO_UTENTE,EMAIL_UTENTE,CELLULARE_UTENTE) VALUES (%s, %s, %s, %s, %s)"
        values = (name,surname,address,email,phone)

        self.cursor.execute(query,values)
        self.db.commit()
        messagebox.showinfo("Successo", "Utente aggiunto con successo")
        self.parent.deiconify()
        self.window.destroy()

    def remove_user(self):
        self.remove_window = tk.Toplevel(self.parent)
        self.remove_window.title("Rimuovi Utente")
        self.remove_window.geometry("300x200")
        self.remove_window.grab_set()
        self.remove_window.transient(self.parent)

        label_id = tk.Label(self.remove_window, text="ID Utente: ")
        self.entry_id = tk.Entry(self.remove_window)

        label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)

        button_remove = tk.Button(self.remove_window, text="Rimuovi Utente", command=self.remove_user_from_db, background="red")
        button_remove.grid(row=1, column=1, pady=2)

        button_exit = tk.Button(self.remove_window, text="Esci", command=self.remove_window.destroy, background="green")
        button_exit.grid(row=2, column=1, pady=2)

    def remove_user_from_db(self):
        user_id = self.entry_id.get()

        check_query = "SELECT COUNT(*) FROM Utenti WHERE ID = %s"
        self.cursor.execute(check_query, (user_id,))
        if self.cursor.fetchone()[0] == 0:
            messagebox.showerror("Errore", "Utente non trovato.")
            return

        if messagebox.askyesno("Conferma", "Sei sicuro di voler rimuovere questo Utente?"):
            delete_query = "DELETE FROM Utenti WHERE ID = %s"
            try:
                self.cursor.execute(delete_query, (user_id,))
                self.db.commit()
                messagebox.showinfo("Successo", "Utente rimosso con successo")
            except Exception as e:
                messagebox.showerror("Errore", f"Si è verificato un errore durante la rimozione del Utente: {e}")
            finally:
                if self.remove_window:
                    self.remove_window.destroy()
        else:
            messagebox.showinfo("Annullato", "Operazione di rimozione annullata")
            

    def view_users(self):
        
        view_window = tk.Toplevel(self.parent)
        view_window.title("Visualizza Utenti")
        view_window.geometry("800x600")

        tree = ttk.Treeview(view_window, columns=('ID Utente','Nome', 'Cognome','Indirizzo','Email',
                                                  'Cellulare'), show='headings')

        tree.heading('ID Utente',text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Cognome', text='Cognome')
        tree.heading('Indirizzo', text='Indirizzo')
        tree.heading('Email', text='Email')
        tree.heading('Cellulare', text='Cellulare')


        cursor = self.cursor
        query = "SELECT ID,NOME_UTENTE, COGNOME_UTENTE,INDIRIZZO_UTENTE,EMAIL_UTENTE,CELLULARE_UTENTE FROM Utenti"
        cursor.execute(query)
        risultati = cursor.fetchall()

        for row in risultati:
            tree.insert('', 'end', values=row)

        tree.pack(expand=True, fill='both')

        close_button = tk.Button(view_window, text="Chiudi", command=view_window.destroy)
        close_button.pack(side='bottom')

    
    def update_user(self):
        update_window = tk.Toplevel(self.parent)
        update_window.title("Aggiorna Utente")
        update_window.geometry("300x200")
        update_window.grab_set()
        update_window.transient(self.parent)

        label_id = tk.Label(update_window, text="ID Utente: ")
        entry_id = tk.Entry(update_window)
        label_id.grid(row=0, column=0)
        entry_id.grid(row=0, column=1)

        label_name = tk.Label(update_window, text="Nome Utente: ")
        entry_name = tk.Entry(update_window)

        label_surname = tk.Label(update_window, text="Cognome Utente: ")
        entry_surname = tk.Entry(update_window)

        label_address = tk.Label(update_window, text="Indirizzo: ")
        entry_address = tk.Entry(update_window)

        label_email = tk.Label(update_window, text="Email: ")
        entry_email = tk.Entry(update_window)

        label_phone = tk.Label(update_window, text="Cellulare: ")
        entry_phone = tk.Entry(update_window)

        label_name.grid(row=1, column=0)
        entry_name.grid(row=1, column=1)

        label_surname.grid(row=2, column=0)
        entry_surname.grid(row=2, column=1)

        label_address.grid(row=3, column= 0)
        entry_address.grid(row=3, column=1)

        label_email.grid(row=4, column= 0)
        entry_email.grid(row=4, column=1)

        label_phone.grid(row=5, column=0)
        entry_phone.grid(row=5, column=1)

        def perform_update():
            user_id = entry_id.get()
            updated_name = entry_name.get()
            updated_surname = entry_surname.get()
            updated_address = entry_address.get()
            updated_email = entry_email.get()
            updated_phone = entry_phone.get()

            query = "UPDATE Utenti SET NOME_UTENTE = %s, COGNOME_UTENTE = %s, \
                    INDIRIZZO_UTENTE = %s, EMAIL_UTENTE = %s, CELLULARE_UTENTE = %s \
                     WHERE ID = %s"
            values = (updated_name, updated_surname, updated_address, updated_email, updated_phone, user_id)

            try:
                self.cursor.execute(query, values)
                self.db.commit()
                messagebox.showinfo("Successo", "Utente aggiornato con successo")
                update_window.destroy()
            except Exception as e:
                messagebox.showerror("Errore", f"Si è verificato un errore durante l'aggiornamento: {e}")
            
        update_button = tk.Button(update_window, text="Aggiorna", command=perform_update)
        update_button.grid(row=6, column=1, pady=2)

    