# Importamos la clase CinemaHall desde el archivo cinema_hall.py
from cinema_hall import CinemaHall

class Menu:
    def __init__(self):
        self.cinema = CinemaHall()  # Crear una instancia de CinemaHall

    def menu_list(self):
        while True:
            print("\nMenú Principal:")
            print("1. Ir al Submenú del Cine")
            print("2. Salir")
            
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                # Llamar al submenú del cine
                if not self.cinema.mostrar_submenu():
                    continue  # Si el submenú regresa, volvemos al menú principal
            elif opcion == "2":
                print("Saliendo del programa...")
                break  # Salir del programa
            else:
                print("Opción no válida. Intenta de nuevo.")