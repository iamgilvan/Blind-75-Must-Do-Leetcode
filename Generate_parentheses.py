import unittest

#TC O(2^n)
#TS O(n)
def generate_parentheses(n):
    #n x 2 parenthesis numbers in result

    #only add open parenthesis if open < n
    #only add a closing paranthesis if closed < open
    # valid iif open == closed == n

    stack = []
    result = []
    def backtrack(openN, closeN):
        if openN == closeN == n:
            result.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()
    backtrack(0,0)
    return result

class Test(unittest.TestCase):
    test_cases = [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1,["()"]),
    ]
    functions = [generate_parentheses]
    def test_generate_parentheses(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()