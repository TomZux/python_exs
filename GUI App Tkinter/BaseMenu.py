import tkinter as tk
from tkinter import messagebox

class MenuBase(tk.Toplevel):
    def __init__(self, parent, title, bg_color):
        super().__init__(parent)
        self.title(title)
        self.geometry("500x550")
        self.configure(bg=bg_color)
        self.grab_set()
        self.resizable(False, False)

        self.add_buttons()

        tk.Button(self, text="Ritorna al menù", command=self.close_window, bg="white", width=18, height=2, font="Italic").pack(pady=20)


    def add_buttons(self):
        pass
    
    def close_window(self):
        user_input = messagebox.askyesno("ATTENZIONE!","Sei sicuro di volere uscire? ")
        if user_input:
            self.destroy()
