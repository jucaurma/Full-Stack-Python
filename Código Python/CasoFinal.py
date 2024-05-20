class Tarea:
    def __init__(self, descripcion):
        """Inicializa una nueva tarea con la descripción dada y la marca como pendiente."""
        self.descripcion = descripcion
        self.completada = False

    def __str__(self):
        """Retorna una representación en cadena de la tarea, mostrando su estado."""
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class ListaDeTareas:
    def __init__(self):
        """Inicializa una lista vacía de tareas."""
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea a la lista."""
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print("Tarea agregada exitosamente.")

    def marcar_completada(self, indice):
        """Marca una tarea como completada dado su índice."""
        try:
            self.tareas[indice].completada = True
            print("Tarea marcada como completada.")
        except IndexError:
            print("Error: Índice de tarea no válido.")

    def mostrar_tareas(self):
        """Muestra todas las tareas, numeradas y con su estado."""
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, indice):
        """Elimina una tarea de la lista dado su índice."""
        try:
            del self.tareas[indice]
            print("Tarea eliminada exitosamente.")
        except IndexError:
            print("Error: Índice de tarea no válido.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nGestor de Tareas Pendientes")
    print("1. Agregar nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    lista_de_tareas = ListaDeTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                indice = int(input("Ingrese el índice de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_completada(indice)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == "3":
            lista_de_tareas.mostrar_tareas()
        elif opcion == "4":
            try:
                indice = int(input("Ingrese el índice de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(indice)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
