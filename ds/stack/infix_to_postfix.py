# Infix notation   : https://en.wikipedia.org/wiki/Infix_notation
# Postfix notation : https://en.wikipedia.org/wiki/Reverse_Polish_notation
from stack import Stack

def solve(infix):
    opstack = Stack()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    result = ""
    for token in infix:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result += token
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            toptoken = opstack.pop()
            while toptoken != "(":
                result += toptoken
                toptoken = opstack.pop()
        else:
            while not opstack.isEmpty() and (prec[opstack.peek()] >= prec[token]):
                result += opstack.pop()
            opstack.push(token)
    while not opstack.isEmpty():
        result += opstack.pop()
    return result

def main():
    print("A*B+C*D = %s" % solve("A*B+C*D"))
    print("(A+B)*C-(D-E)*(F+G) = %s" % solve("(A+B)*C-(D-E)*(F+G)"))

if __name__ == "__main__":
    main()