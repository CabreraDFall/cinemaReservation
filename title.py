# title.py
import tkinter as tk

class Title:
  def agregar_texto(self, texto, font=("Arial", 12), color="white"):
        """Método para agregar texto en la ventana."""
        label = tk.Label(self.root, text=texto, font=font, fg=color, bg=self.root["bg"])
        label.pack(pady=20)  # Empaqueta el texto con un poco de espacio
