# https://en.wikipedia.org/wiki/Hot_potato_(game)
from queue import Queue

def play(nameList, num):
    q = Queue()
    for x in nameList:
        q.enqueue(x)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

def main():
    print("%s" % play(["Bill", "Brad", "Jane", "John", "Lindsay", "Joyce"], 7))

if __name__ == "__main__":
    main()