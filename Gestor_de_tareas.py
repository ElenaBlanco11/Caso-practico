# Definimos la clase Tarea
class Tarea:
    def __init__(self, descripcion):
        # Constructor que inicializa una tarea con una descripción y establece el estado de completada como "False", es decir, está pendiente.
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        # Cambia el estado de la tarea de pendiente a completada(True)
        self.completada = True

    def __str__(self):
        # Retona una cadena con la descripción de la tarea y su estado (Completada o Pendiente)
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

# Definimos la clase ListaDeTareas
class ListaDeTareas:
    def __init__(self):
        # Inicializa una lista vacía de tareas.
        self.tareas = []

    def agregar_tarea(self, descripcion):
        # Agrega una nueva tarea a la lista
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_completada(self, posicion):
        try:
            # Marca una tarea como completada dada su posición en la lista
            self.tareas[posicion].marcar_completada()
        except IndexError:
            # Maneja el error si la posición no existe o no es válida
            print("Error: La posición ingresada no existe en la lista de tareas.")

    def mostrar_tareas(self):
        # Muestra todas las tareas con sus estados
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        try:
            # Elimina una tarea dada su posición en la lista
            del self.tareas[posicion]
        except IndexError:
            # Maneja el error si la posición no existe
            print("Error: La posición ingresada no existe en la lista de tareas.")

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("\nOpciones:")
    print("1. Agregar una nueva tarea")
    print("2. Marcar una tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar una tarea")
    print("5. Salir")

# Función que toma la opción seleccionada y ejecuta la acción correspondiente llamando a otras funciones
def manejar_opcion(opcion, lista_de_tareas):

    if opcion == 1:
        descripcion = input("Ingrese la descripción de la nueva tarea: ")
        lista_de_tareas.agregar_tarea(descripcion)
    elif opcion == 2:
        marcar_tarea_completada(lista_de_tareas)
    elif opcion == 3:
        lista_de_tareas.mostrar_tareas(lista_de_tareas)
    elif opcion == 4:
        eliminar_tarea(lista_de_tareas)
    elif opcion == 5:
        print("Saliendo del programa.")
        return False
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
    return True
    
def marcar_tarea_completada(lista_de_tareas):
    # Función que pide al usuario la posición de la tarea que quiere marcar como completada y lo hace
    try:
        posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
        lista_de_tareas.marcar_completada(posicion)
    except ValueError:
        print("Error: Por favor ingrese un número valido.")


def eliminar_tarea(lista_de_tareas):
    # Función que pide al usuario la posición de la tarea que quiere eliminar y lo hace.
    try:
        posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
        lista_de_tareas.eliminar_tarea(posicion)
    except ValueError:
        print("Error: Por favor ingrese un número válido.")


def main():
    # Función que controla el flujo del programa, muestra el menú, pide al usuario que elija una opción y la maneja.
    lista_de_tareas = ListaDeTareas()
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if not manejar_opcion(opcion, lista_de_tareas):
                break
        except ValueError:
            print("Error: Por favor ingrese un número válido.")


if __name__ == "__main__":
    # Indica que se llame a la función main, si el archivo se ejecuta directamente.
    main()



