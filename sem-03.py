# Node of a Single Linked List
class Node:
    # Constructor
    def __init__(self):
        self.data = None
        self.next = None

    # Method for setting the data
    def setData(self, data):
        self.data = data

    # Method for getting the data
    def getData(self):
        return self.data

    # Method for setting the pointer
    def setNext(self, next):
        self.next = next

    # Method for getting the data of the next node
    def getNext(self):
        if self.hasNext():
            return self.next.getData()
        else:
            return None

    # Return true if the node points to another node
    def hasNext(self):
        return self.next is not None

node0 = Node()
node0.setData(0)

node1 = Node()
node1.setData(10)

node2 = Node()
node2.setData(20)

node3 = Node()
node3.setData(30)

node4 = Node()
node4.setData(40)


node0.setNext(node1)
node1.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)


print("node1 data -->", node1.getData())
print("node1 next -->", node1.getNext())
print("node2 data -->", node2.getData())
print("node2 next -->", node2.getNext())
print("node0 next -->", node0.getNext())
print("node4 next -->", node4.getNext())
print("lista: [",node0.getData(),node1.getData(),node2.getData(),node3.getData(),node4.getData(),node4.getNext(),"]")