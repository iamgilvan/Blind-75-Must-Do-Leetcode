import unittest

#TC O(n)
#TS O(n)
def evaluate_Reverse_Polish_Notation(arr):
    stack = []
    for token in arr:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            stack.append(stack.pop() - stack.pop())
        elif token == "/":
            stack.append(stack.pop() / stack.pop())
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