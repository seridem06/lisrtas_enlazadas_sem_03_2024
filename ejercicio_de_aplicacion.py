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
            if self.__primero != None:
                nodo.sig = self.__primero
            else:
                self.__ultimo = nodo
            self.__primero = nodo

    def insertar_ultimo(self, *elem):
        for i in elem:
            nodo = Nodo(i)
            if self.__ultimo != None:
                self.__ultimo.sig = nodo
                self.__ant_actual = self.__ultimo
            else:
                self.__primero = nodo
            self.__ultimo = nodo

    def elimina_primero(self):
        if self.__primero == None:
            return
        nodo = self.__primero
        self.__primero = nodo.sig
        if self.__primero == None:
            self.__ultimo = None
        del nodo

    def __add__(self, list2):
        list3 = Lista()
        nodo = self.__primero
        while nodo != None:
            list3.insertar_ultimo(nodo.Info)
            nodo = nodo.sig
        nodo = list2.__primero
        while nodo != None:
            list3.insertar_ultimo(nodo.Info)
            nodo = nodo.sig
        return list3

    def info_anterior(self):
        if self.__primero == None or self.__ant_actual == None:
            return
        return self.__ant_actual.Info

    def eliminar_elem(self, elem):
        while self.__primero != None and self.__primero.Info == elem:
            temp = self.__primero
            self.__primero = temp.sig
            del temp
            if self.__primero == None:
                self.__ultimo = None

        nodo = self.__primero
        while nodo != None:
            while nodo.sig != None and nodo.sig.Info == elem:
                temp = nodo.sig
                if temp == self.__ultimo:
                    self.__ultimo = nodo
                nodo.sig = temp.sig
                del temp
            nodo = nodo.sig

    def sig(self):
        if self.__primero == None:
            return
        if self.__ant_actual == None:
            self.__ant_actual = self.__primero
            return
        actual = self.__ant_actual.sig
        if actual.sig != None:
            self.__ant_actual = actual

    def elimina_actual(self):
        if self.__primero == None:
            return
        if self.__ant_actual == None:
            temp = self.__primero
            self.__primero = temp.sig
            if self.__primero == None:
                self.__ultimo = None
            del temp
        else:
            temp = self.__ant_actual.sig
            self.__ant_actual.sig = temp.sig
            if temp == self.__ultimo:
                self.__ultimo = self.__ant_actual
            del temp

    def cons(self):
        if self.__primero == None:
            return
        if self.__ant_actual == None:
            return self.__primero.Info
        return self.__ant_actual.sig.Info

    def inicio(self):
        self.__ant_actual = None

    def actual_es_ultimo(self):
        if self.__ant_actual != None:
            if self.__ant_actual.sig == self.__ultimo:
                return True
        return False

    def mostrar(self):
        nodo = self.__primero
        while nodo != None:
            print(nodo.Info)
            nodo = nodo.sig

def menu():
    lista = Lista()
    while True:
        print("\nMenú de operaciones:")
        print("1. Listar los elementos")
        print("2. Agregar")
        print("3. Eliminar el último")
        print("4. Eliminar el primero")
        print("5. Insertar al inicio")
        print("6. Insertar al final")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            lista.mostrar()
        elif opcion == "2":
            elem = input("Ingrese los elementos a agregar separados por espacios: ").split()
            lista.insertar_ultimo(*elem)
        elif opcion == "3":
            lista.elimina_primero()
        elif opcion == "4":
            lista.elimina_primero()
        elif opcion == "5":
            elem = input("Ingrese los elementos a insertar al inicio separados por espacios: ").split()
            lista.insertar_inicio(*elem)
        elif opcion == "6":
            elem = input("Ingrese los elementos a insertar al final separados por espacios: ").split()
            lista.insertar_ultimo(*elem)
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()