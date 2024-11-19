class CinemaHall: 
    def __init__(self):
        self.seats_list=[
            [0,0,1,0,0,0], 
            [0,0,1,0,0,0,0]
            ]
        

    def mostrar_submenu(self):
        print("\nSubmenú:")
        print("1. Opción A")
        print("2. Opción B")
        print("3. Regresar al menú principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("Has seleccionado Opción A")
        elif opcion == "2":
            print("Has seleccionado Opción B")
        elif opcion == "3":
            return False  # Regresar al menú principal
        else:
            print("Opción no válida. Intenta de nuevo.")
        
        return True  # Continuar en el submenú  


    def seat_validation(self, seat:str)-> bool:
        if len(seat) != 2:
            return False
        
        row = int(seat[0]) - 1 
        col = ord(seat[1].upper()) -ord("A")  

        if row < 0 or row >= len(self.seats_list):
            return False 
        if col < 0 or col >= len(self.seats_list):
            return False 
        
        return True

    def find_seat(self,seat:str):
        
        if not self.seat_validation(seat):
            return f"El asiento {seat} no es valido"
        
        row = int(seat[0]) - 1 
        col = ord(seat[1].upper()) -ord("A")  

        if self.seats_list[row][col] == 0:
            return f"EL asiento {seat} esta libre."
        else:
            return f"El asiento {seat} esta ocupado"

    def add_seat(self, answer: str, row_index: int = 1):
        
        if answer.lower() == "no":
            return "No se ha agregado ningún asiento a la sala."
        
        if answer.lower() == "yes":
            # Validar que el índice de fila proporcionado es válido
            if 0 <= row_index < len(self.seats_list):
                self.seats_list[row_index].append(9)
                print(f"Estado actual de los asientos: {self.seats_list}")
                return f"Se ha agregado el asiento en la fila {row_index + 1}."
            else:
                return "Índice de fila inválido. No se puede agregar el asiento."
        
        return "Respuesta inválida. Por favor, responda con 'yes' o 'no'."

    def seat_reservation(self, seat: str):
        
        if not self.seat_validation(seat):
            return "Asiento no disponible"       

        row = int(seat[0]) - 1 
        col = ord(seat[1].upper()) -ord("A")  

       
        # Verificar si el asiento está disponible
        if self.seats_list[row][col] == 0:
            self.seats_list[row][col] = 1  # Reservar el asiento
            return f"El asiento {seat} ha sido reservado exitosamente."
        else:
            return f"El asiento {seat} ya está ocupado."

    def canceled_seat(self, seat: str):
        pass

