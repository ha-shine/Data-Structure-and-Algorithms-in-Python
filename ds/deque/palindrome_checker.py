# https://en.wikipedia.org/wiki/Palindrome
from deque import Deque

def solve(word):
    d = Deque()

    for char in word:
        if char == " ":
            pass
        else:
            d.addRear(char)

    while d.size() > 1:
        front = d.removeFront()
        rear = d.removeRear()
        if front != rear:
            return False
    return True

def main():
    print("dasfasdif : %s" % solve("dasfasdif"))
    print("madam : %s" % solve("madam"))

if __name__ == "__main__":
    main()