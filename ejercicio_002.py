# Nodo de una lista enlazada simple
class Nodo:

    # Constructor para inicializar un nodo con datos y un puntero siguiente
    def __init__(self):
        self.data = None  # Dato almacenado en el nodo
        self.next = None  # Puntero al siguiente nodo en la lista

    # Método para establecer el dato del nodo
    def setData(self, data):
        self.data = data

    # Método para obtener el dato del nodo
    def getData(self):
        return self.data

    # Método para establecer el siguiente puntero del nodo
    def setNext(self, next):
        self.next = next

    # Método para obtener el siguiente puntero del nodo
    def getNext(self):
        return self.next


# Lista enlazada simple
class LinkedList:

    # Constructor para inicializar una lista enlazada vacía
    def __init__(self):
        self.head = None  # Cabeza de la lista (nodo inicial)
        self.length = 0  # Longitud actual de la lista

    # Método para imprimir los elementos de la lista enlazada
    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end=" -> ")
            node = node.next
        print("NULL")  # Indica el final de la lista

    # Método para insertar un elemento al inicio de la lista
    def insertAtBegin(self, data):
        new_node = Nodo()
        new_node.setData(data)

        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        if self.length == 0:
            self.head = new_node
        else:
            # El nuevo nodo apunta al nodo anterior (cabeza actual)
            new_node.setNext(self.head)
            # El nuevo nodo se convierte en la nueva cabeza
            self.head = new_node

        self.length += 1  # Actualizar la longitud de la lista

# Crear una lista enlazada con los datos 10, 20, 30, 40
lista = LinkedList()
lista.insertAtBegin(40)
lista.insertAtBegin(30)
lista.insertAtBegin(20)
lista.insertAtBegin(10)

# Imprimir la lista enlazada
lista.print()




