# main.py

from utils.window import create_viewport
from compontents.title import set_title

def main(titulo, tab_name):
    # Crear la ventana principal
    import tkinter as tk
    window = tk.Tk()
   
    # Llamar a la función para crear la vista
    create_viewport(window, tab_name)
    # Llamar a la función para establecer el título
    set_title(window, titulo)
    # Iniciar el bucle de la aplicación
    window.mainloop()

# Ejemplo de uso
if __name__ == "__main__":
    main("Mi Aplicación", "tabname")
