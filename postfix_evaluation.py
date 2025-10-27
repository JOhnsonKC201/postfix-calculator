import math
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# Evaluate a Simple Postfix Expression
def postfix_eval(postfix_expr):
    stack = Stack()
    postfix_str = postfix_expr.split()
    str_list = [postfix_str]

    for x in str_list[0]:
        if x.isdigit():
            stack.push(int(x))
        elif x == "sqrt":
            if stack.size() < 1:
                raise ValueError
            a = stack.pop()
            if a < 0:
                raise ValueError
            stack.push(math.sqrt(a))
        elif x in "+-*/^%":
            if stack.size() < 2:
                raise ValueError
            a = stack.pop()
            b = stack.pop()
            if x == "+":
                stack.push(b + a)
            elif x == "-":
                stack.push(b - a)
            elif x == "*":
                stack.push(b * a)
            elif x == "/":
                stack.push(b / a)
            elif x == "%":
                stack.push(b % a)
            elif x == "^":
                stack.push(b ** a)
        else:
            raise ValueError

    if stack.size() != 1:
        raise ValueError

    return stack.pop() 

print(postfix_eval("3 4 + 2 *")) # Output: 14

# Extend the postfix_eval function to handle multi-digit numbers in the postfix expression
print(postfix_eval("12 4 + 2 *"))  # Output: 32

# Support for More Operators and Functions
print(postfix_eval("3 4 + 2 ^")) # Output: 49 (i.e., (3 + 4) ^ 2) 
print(postfix_eval("5 1 2 + 4 * + 3 -")) # Output: 14 (Regular operation) 
print(postfix_eval("9 sqrt 2 ^")) # Output: 9.0 (sqrt(9) ^ 2) print