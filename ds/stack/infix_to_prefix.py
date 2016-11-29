# Infix notation  : https://en.wikipedia.org/wiki/Infix_notation
# Prefix notation : https://en.wikipedia.org/wiki/Polish_notation
from stack import Stack

def solve(infix):
    opstack = Stack()
    tokenstack = Stack()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    result = ""
    for token in infix:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if tokenstack.isEmpty():
                tokenstack.push(token)
            else:
                result = tokenstack.pop() + token + result
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            toptoken = opstack.pop()
            while toptoken != "(":
                result = toptoken + result
                toptoken = opstack.pop()
        else:
            while not opstack.isEmpty() and (prec[opstack.peek()] >= prec[token]):
                result = opstack.pop() + result
            opstack.push(token)
    while not opstack.isEmpty():
        result = opstack.pop() + result
    return result

def main():
    print("A*B+C*D = %s" % solve("A*B+C*D"))
    print("(A+B)*C-(D-E)*(F+G) = %s" % solve("(A+B)*C-(D-E)*(F+G)"))

if __name__ == "__main__":
    main()