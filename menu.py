class Nodo:
    def __init__(self, info):
        self.Info = info
        self.sig = None

# Clase Lista
class Lista:
    def __init__(self, *elem):
        self.__primero = None
        self.__ultimo = None
        self.__ant_actual = None

        for i in elem:
            self.insertar_ultimo(i)

    def insertar_inicio(self, *elem):
        for i in elem:
            nodo = Nodo(i)
            if (self.__primero != None):
                nodo.sig = self.__primero
            else:
                self.__ultimo = nodo

            self.__primero = nodo

    def insertar_ultimo(self, *elem):
        for i in elem:
            nodo = Nodo(i)
            if (self.__ultimo != None):
                self.__ultimo.sig = nodo
                self.__ant_actual = self.__ultimo
            else:
                self.__primero = nodo

            self.__ultimo = nodo

    def elimina_primero(self):
        if (self.__primero == None):
            return

        nodo = self.__primero
        self.__primero = nodo.sig
        del nodo

    def elimina_ultimo(self):
        if (self.__primero == None):
            return

        nodo = self.__primero
        if nodo == self.__ultimo:
            self.__primero = self.__ultimo = None
            del nodo
            return

        while nodo.sig != self.__ultimo:
            nodo = nodo.sig

        nodo.sig = None
        del self.__ultimo
        self.__ultimo = nodo

    def mostrar(self):
        nodo = self.__primero
        while nodo != None:
            print(nodo.Info)
            nodo = nodo.sig
        print()

# Función para mostrar el menú
def menu():
    print("Menú:")
    print("1. Listar los elementos")
    print("2. Agregar")
    print("3. Eliminar el último")
    print("4. Eliminar el primero")
    print("5. Insertar al inicio")
    print("6. Insertar al final")
    print("0. Salir")

# Función principal
def main():
    lista = Lista()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Elementos de la lista:")
            lista.mostrar()
        elif opcion == "2":
            elemento = input("Ingrese el elemento a agregar: ")
            lista.insertar_ultimo(elemento)
            print("Elemento agregado correctamente.")
        elif opcion == "3":
            lista.elimina_ultimo()
            print("Último elemento eliminado correctamente.")
        elif opcion == "4":
            lista.elimina_primero()
            print("Primer elemento eliminado correctamente.")
        elif opcion == "5":
            elemento = input("Ingrese el elemento a insertar al inicio: ")
            lista.insertar_inicio(elemento)
            print("Elemento insertado al inicio correctamente.")
        elif opcion == "6":
            elemento = input("Ingrese el elemento a insertar al final: ")
            lista.insertar_ultimo(elemento)
            print("Elemento insertado al final correctamente.")
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
