# Clase Nodo y Clase Lista (sin cambios)

def listar_elementos(lista):
    """Listar los elementos de la lista"""
    lista.mostrar()

def agregar_elemento(lista):
    """Agregar un elemento al final de la lista"""
    elemento = input("Ingrese el elemento a agregar: ")
    lista.insertar_ultimo(elemento)

def eliminar_ultimo(lista):
    """Eliminar el último elemento de la lista"""
    lista.inicio()
    while not lista.actual_es_ultimo():
        lista.sig()
    lista.elimina_actual()

def eliminar_primero(lista):
    """Eliminar el primer elemento de la lista"""
    lista.elimina_primero()

def insertar_inicio(lista):
    """Insertar un elemento al inicio de la lista"""
    elemento = input("Ingrese el elemento a insertar al inicio: ")
    lista.insertar_inicio(elemento)

def insertar_final(lista):
    """Insertar un elemento al final de la lista"""
    elemento = input("Ingrese el elemento a insertar al final: ")
    lista.insertar_ultimo(elemento)

def salir():
    """Salir del programa"""
    print("Saliendo del programa...")

def menu(opciones):
    lista = Lista()

    while True:
        print("\nMenú de operaciones:")
        for key, value in opciones.items():
            print(f"{key}. {value.__doc__}")

        opcion = input("Ingrese una opción: ")

        if opcion in opciones:
            operacion = opciones[opcion]
            if operacion != salir:
                operacion(lista)
            else:
                operacion()
                break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú
opciones = {
    "1": listar_elementos,
    "2": agregar_elemento,
    "3": eliminar_ultimo,
    "4": eliminar_primero,
    "5": insertar_inicio,
    "6": insertar_final,
    "7": salir
}

menu(opciones)