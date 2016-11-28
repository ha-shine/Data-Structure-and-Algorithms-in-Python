# Same idea as balanced_parentheses.py with additional symbols
from stack import Stack

def solve(question):
    x = Stack()
    for char in question:
        if char in "([{":
            x.push(char)
        else:
            if x.isEmpty():
                return False
            elif char == ")" and x.peek() == "(":
                x.pop()
            elif char == "]" and x.peek() == "[":
                x.pop()
            elif char == "}" and x.peek() == "{":
                x.pop()
            else:
                return False
    if x.isEmpty():
        return True
    else:
        return False

def main():
    print("{{[[(())]]}} : %s" % solve("{{[[(())]]}}"))
    print("{{[[(())]] : %s" % solve("{{[[(())]]"))
    print("[(())]]}} : %s" % solve("[(())]]}}"))

if __name__ == "__main__":
    main()