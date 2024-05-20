from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_limite):
        """Inicializa una nueva tarea con la descripción dada, prioridad, fecha de creación y fecha límite."""
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_limite = fecha_limite
        self.completada = False

    def __str__(self):
        """Retorna una representación en cadena de la tarea, mostrando su estado y detalles."""
        estado = "Completada" if self.completada else "Pendiente"
        return (f"{self.descripcion} - {estado}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Fecha de creación: {self.fecha_creacion}\n"
                f"Fecha límite: {self.fecha_limite}")

class ListaDeTareas:
    def __init__(self):
        """Inicializa una lista vacía de tareas."""
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad, fecha_limite):
        """Agrega una nueva tarea a la lista."""
        tarea = Tarea(descripcion, prioridad, fecha_limite)
        self.tareas.append(tarea)
        print("Tarea agregada exitosamente.")

    def marcar_completada(self, indice):
        """Marca una tarea como completada dado su índice."""
        try:
            self.tareas[indice].completada = True
            print("Tarea marcada como completada.")
        except IndexError:
            print("Error: Índice de tarea no válido.")

    def cambiar_prioridad(self, indice, nueva_prioridad):
        """Cambia la prioridad de una tarea dada su posición en la lista."""
        try:
            self.tareas[indice].prioridad = nueva_prioridad
            print("Prioridad de la tarea actualizada exitosamente.")
        except IndexError:
            print("Error: Índice de tarea no válido.")

    def cambiar_fecha_limite(self, indice, nueva_fecha_limite):
        """Cambia la fecha límite de una tarea dada su posición en la lista."""
        try:
            self.tareas[indice].fecha_limite = nueva_fecha_limite
            print("Fecha límite de la tarea actualizada exitosamente.")
        except IndexError:
            print("Error: Índice de tarea no válido.")

    def mostrar_tareas(self):
        """Muestra todas las tareas, numeradas y con su estado."""
        if not self.tareas:
            print("No hay tareas en la lista.")
            return

        # Ordenar las tareas por prioridad
        prioridades = {'alta': 1, 'media': 2, 'baja': 3}
        tareas_ordenadas = sorted(self.tareas, key=lambda x: (prioridades[x.prioridad], x.fecha_limite))

        print("Tareas ordenadas por prioridad:")
        for i, tarea in enumerate(tareas_ordenadas):
            print(f"{i}. {tarea}\n")

        # Mostrar las tareas próximas a la fecha límite y las que la han pasado
        hoy = datetime.now().strftime("%Y-%m-%d")
        proximas_tareas = [tarea for tarea in tareas_ordenadas if tarea.fecha_limite <= hoy]

        if proximas_tareas:
            print("Tareas próximas a la fecha límite o pasadas:")
            for i, tarea in enumerate(proximas_tareas):
                print(f"{i}. {tarea}\n")
        else:
            print("No hay tareas próximas a la fecha límite o que la hayan pasado.")

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
    print("3. Cambiar prioridad de una tarea")
    print("4. Cambiar fecha límite de una tarea")
    print("5. Mostrar todas las tareas")
    print("6. Eliminar tarea")
    print("7. Salir")

def validar_prioridad(prioridad):
    """Verifica que la prioridad sea válida (alta, media, baja)."""
    if prioridad.lower() not in ["alta", "media", "baja"]:
        raise ValueError("Prioridad no válida. Debe ser 'alta', 'media' o 'baja'.")

def validar_fecha_limite(fecha_limite):
    """Verifica que la fecha límite esté en el formato correcto (YYYY-MM-DD)."""
    try:
        datetime.strptime(fecha_limite, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Formato de fecha no válido. Debe ser 'YYYY-MM-DD'.")

def main():
    lista_de_tareas = ListaDeTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = input("Ingrese la prioridad de la tarea (alta, media, baja): ")
            fecha_limite = input("Ingrese la fecha límite de la tarea (formato: YYYY-MM-DD): ")
            try:
                validar_prioridad(prioridad)
                validar_fecha_limite(fecha_limite)
                lista_de_tareas.agregar_tarea(descripcion, prioridad, fecha_limite)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            try:
                indice = int(input("Ingrese el índice de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_completada(indice)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
            except IndexError:
                print("Error: Índice de tarea no válido.")
        elif opcion == "3":
            try:
                indice = int(input("Ingrese el índice de la tarea a cambiar la prioridad: "))
                nueva_prioridad = input("Ingrese la nueva prioridad de la tarea (alta, media, baja): ")
                validar_prioridad(nueva_prioridad)
                lista_de_tareas.cambiar_prioridad(indice, nueva_prioridad)
            except ValueError as e:
                print(f"Error: {e}")
            except IndexError:
                print("Error: Índice de tarea no válido.")
        elif opcion == "4":
            try:
                indice = int(input("Ingrese el índice de la tarea a cambiar la fecha límite: "))
                nueva_fecha_limite = input("Ingrese la nueva fecha límite de la tarea (formato: YYYY-MM-DD): ")
                validar_fecha_limite(nueva_fecha_limite)
                lista_de_tareas.cambiar_fecha_limite(indice, nueva_fecha_limite)
            except ValueError as e:
                print(f"Error: {e}")
            except IndexError:
                print("Error: Índice de tarea no válido.")
        elif opcion == "5":
            lista_de_tareas.mostrar_tareas()
        elif opcion == "6":
            try:
                indice = int(input("Ingrese el índice de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(indice)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
            except IndexError:
                print("Error: Índice de tarea no válido.")
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
