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

class OrderedList:

    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        while current != None and current.getData() <= item:
            if current.getData == item:
                return True
            else:
                current = current.getNext()

        return False

    def add(self, item):
        current = self.head
        previous = None
        while current != None and current.getData < item:
            previous = current
            current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)