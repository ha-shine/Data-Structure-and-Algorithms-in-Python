class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def put(self, key, data):
        hashvalue = self.hash(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key, data):
        hashvalue = self.hash(key, len(self.slots))
        data = None
        start = hashvalue
        while self.slots[hashvalue] != None:
            if self.slots[hashvalue] == key:
                return data
            else:
                hashvalue = self.rehash(hashvalue, len(self.slots))
                if hashvalue == start:
                    return None
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)