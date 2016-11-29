class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        size = 0
        while current != None:
            size += 1
            current = current.getNext()

        return size

    def search(self, item):
        current = self.head
        while current != None:
            if current == item:
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous = None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())