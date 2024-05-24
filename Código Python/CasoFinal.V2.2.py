from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_limite):
        """Inicializa una nueva tarea con una descripción, una prioridad, la fecha de creación, una fecha límite y por defecto sin completar"""
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_limite = fecha_limite
        self.completada = False

    def __str__(self):
        """Devuelve la tarea, mostrando su estado y detalles."""
        estado = "Completada" if self.completada else "Pendiente"
        return (f"{self.descripcion} - {estado}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Fecha de creación: {self.fecha_creacion}\n"
                f"Fecha límite: {self.fecha_limite}")

class ListaDeTareas:
    def __init__(self):
        """Inicializa una lista de tareas vacía."""
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad, fecha_limite):
        """Agrega una nueva tarea a la lista."""
        tarea = Tarea(descripcion, prioridad, fecha_limite)
        self.tareas.append(tarea)
        print("\n >> Tarea agregada con éxito. << \n")

    def marcar_completada(self, indice):
        """Marca una tarea como completada a partir de su índice."""
        try:
            self.tareas[indice].completada = True
            print("\n >> Tarea marcada como completada. << \n")
        except IndexError:
            print("\n ---> Error: Índice de tarea no válido!!! \n")

    def cambiar_prioridad(self, indice, nueva_prioridad):
        """Cambia la prioridad de una tarea a partir de su índice."""
        try:
            self.tareas[indice].prioridad = nueva_prioridad
            print("\n >> Prioridad actualizada con éxito. << \n")
        except IndexError:
            print("\n ---> Error: Índice de tarea no válido!!! \n")

    def cambiar_fecha_limite(self, indice, nueva_fecha_limite):
        """Cambia la fecha límite de una tarea a partir de su índice."""
        try:
            self.tareas[indice].fecha_limite = nueva_fecha_limite
            print("\n >> Fecha límite de la tarea actualizada con éxito. << \n")
        except IndexError:
            print("\n ---> Error: Índice de tarea no válido!!! \n")

    def mostrar_tareas(self):
        """Muestra todas las tareas, numeradas y con su estado."""
        if not self.tareas:
            print("\n >> No tiene tareas en la lista. << \n")
            return
        
        """Clasifica las tareas en pendientes, pendientes próximas a expirar o expiradas y completadas"""
        hoy = datetime.now().strftime("%Y-%m-%d")
        pendientes = [tarea for tarea in self.tareas if not tarea.completada and tarea.fecha_limite > hoy]
        proximas_o_pasadas = [tarea for tarea in self.tareas if not tarea.completada and tarea.fecha_limite <= hoy]
        completadas = [tarea for tarea in self.tareas if tarea.completada]

        print("\nTareas pendientes ordenadas por prioridad:\n==========================================\n")
        if pendientes:
            prioridades = {'alta': 1, 'media': 2, 'baja': 3}
            pendientes_ordenadas = sorted(pendientes, key=lambda x: (prioridades[x.prioridad], x.fecha_limite))
            for tarea in pendientes_ordenadas:
                indice = self.tareas.index(tarea)
                print(f"{indice}. {tarea}\n")
        else:
            print("\n >> No tiene tareas pendientes. << \n")

        print("\nTareas próximas a la fecha límite o expiradas:\n==============================================\n")
        if proximas_o_pasadas:
            for tarea in proximas_o_pasadas:
                indice = self.tareas.index(tarea)
                print(f"{indice}. {tarea}\n")
        else:
            print("\n >> No tiene tareas próximas a la fecha límite o que hayan expirado. << \n")

        print("\n Tareas completadas:\n===================\n")
        if completadas:
            for tarea in completadas:
                indice = self.tareas.index(tarea)
                print(f"{indice}. {tarea}\n")
        else:
            print("\n >> No tiene tareas completadas. << \n")

    def eliminar_tarea(self, indice):
        """Elimina una tarea de la lista dado su índice."""
        try:
            del self.tareas[indice]
            print("\n >> Tarea eliminada con éxito. << \n")
        except IndexError:
            print("\n ---> Error: Índice de tarea no válido!!! \n")

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
        raise ValueError("\n ---> Prioridad no válida. Debe ser 'alta', 'media' o 'baja'. \n")

def validar_fecha_limite(fecha_limite):
    """Verifica que la fecha límite esté en el formato correcto (YYYY-MM-DD)."""
    try:
        datetime.strptime(fecha_limite, "%Y-%m-%d")
    except ValueError:
        raise ValueError("\n ---> Formato de fecha no válido. Debe ser 'YYYY-MM-DD'. \n")

def main():
    lista_de_tareas = ListaDeTareas()
    
    while True:
        mostrar_menu()
        opcion = input("\n >> Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("\nPor favor, ingrese la descripción de la tarea: ")
            prioridad = input("Por favor, ingrese la prioridad de la tarea (alta, media, baja): ")
            fecha_limite = input("Por favir, ingrese la fecha límite de la tarea (formato: YYYY-MM-DD): ")
            try:
                validar_prioridad(prioridad)
                validar_fecha_limite(fecha_limite)
                lista_de_tareas.agregar_tarea(descripcion, prioridad, fecha_limite)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "2":
            try:
                indice = int(input("\nPor favor, ingrese el índice de la tarea a marcar como completada: "))
                lista_de_tareas.marcar_completada(indice)
            except ValueError:
                print("\n ---> Error: Por favor, ingrese un número válido. \n")
            except IndexError:
                print("\n ---> Error: Índice de tarea no válido. \n")
        elif opcion == "3":
            try:
                indice = int(input("\nPor favor, ingrese el índice de la tarea a cambiar la prioridad: "))
                nueva_prioridad = input("\n Por favor, ingrese la nueva prioridad de la tarea (alta, media, baja): ")
                validar_prioridad(nueva_prioridad)
                lista_de_tareas.cambiar_prioridad(indice, nueva_prioridad)
            except ValueError as e:
                print(f"Error: {e}")
            except IndexError:
                print("\n ---> Error: Índice de tarea no válido. \n")
        elif opcion == "4":
            try:
                indice = int(input("\n Por favor, ingrese el índice de la tarea a cambiar la fecha límite: "))
                nueva_fecha_limite = input("\n Por favor, ingrese la nueva fecha límite de la tarea (formato: YYYY-MM-DD): ")
                validar_fecha_limite(nueva_fecha_limite)
                lista_de_tareas.cambiar_fecha_limite(indice, nueva_fecha_limite)
            except ValueError as e:
                print(f"Error: {e}")
            except IndexError:
                print("\n ---> Error: Índice de tarea no válido. \n")
        elif opcion == "5":
            lista_de_tareas.mostrar_tareas()
        elif opcion == "6":
            try:
                indice = int(input("\n Por favor, ingrese el índice de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(indice)
            except ValueError:
                print("\n ---> Error: Por favor, ingrese un número válido. \n")
            except IndexError:
                print("\n ---> Error: Índice de tarea no válido. \n")
        elif opcion == "7":
            print("\n >> Ha salido del programa")
            break
        else:
            print(" \n ---> Opción no válida. Por favor, intente nuevamente. \n")

if __name__ == "__main__":
    main()
