# titulo.py

import tkinter as tk

def set_title( window, titulo):
    title_label = tk.Label( text=titulo, font=("Poppins", 22), fg="white", bg="black") 
    title_label.pack(side="top")
