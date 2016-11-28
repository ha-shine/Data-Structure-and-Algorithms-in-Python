# Parentheses are symbols used in mathematical expressions '(())'
# Balanced parentheses means that each opening parentheses has a corresponding closing one
# (((()))) is a balanced parentheses but ())))) or ((((())) are not
from stack import Stack

def solve(question):
    x = Stack()
    for char in question:
        if char == "(":
            x.push(char)
        else:
            if x.isEmpty():
                return False
            elif char == ")":
                x.pop()
    if x.isEmpty():
        return True
    else:
        return False

def main():
    print("(()) : %s" % solve("(())"))
    print("((()) : %s" % solve("((())"))
    print("())) : %s" % solve("((())"))

if __name__ == "__main__":
    main()