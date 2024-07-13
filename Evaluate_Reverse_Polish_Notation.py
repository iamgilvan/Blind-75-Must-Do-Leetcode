import unittest
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.

#TC O(n)
#TS O(n)
def evaluate_Reverse_Polish_Notation(arr):
    stack = []
    for token in arr:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(token))
    return stack.pop()

class Test(unittest.TestCase):
    test_cases = [
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 3)
    ]
    functions = [evaluate_Reverse_Polish_Notation]
    def Evaluate_Reverse_Polish_Notation(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()