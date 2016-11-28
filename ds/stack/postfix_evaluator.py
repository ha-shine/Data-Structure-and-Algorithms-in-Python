# Postfix notation : https://en.wikipedia.org/wiki/Reverse_Polish_notation
from stack import Stack

def solve(postfix):
    opstack = Stack()
    for char in postfix:
        if char in "0123456789":
            opstack.push(int(char))
        else:
            op2 = opstack.pop()
            op1 = opstack.pop()
            result = evaluate(op1, op2, char)
            opstack.push(result)
    return opstack.pop()

def evaluate(op1, op2, operator):
    if operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    elif operator == "+":
        return op1 + op2
    else:
        return op1 - op2

def main():
    print("78+32+/ = %d" % solve("78+32+/"))

if __name__ == "__main__":
    main()