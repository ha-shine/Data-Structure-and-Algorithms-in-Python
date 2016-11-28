# Converting decimal numbers to binary using stacks
from stack import Stack

def solve(number):
    x = Stack()
    while number > 0:
        x.push(number % 2)
        number = number // 2
    result = ""
    while not x.isEmpty():
        result += "%d" % x.pop()
    return result

def main():
    print("1000 = 0b%s" % solve(1000))
    print("15 = 0b%s" % solve(15))
    print("84 = 0b%s" % solve(84))
    print("0 = 0b%s" % solve(0))


if __name__ == "__main__":
    main()