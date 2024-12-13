import unittest
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

#TC O(n)
#TS O(1)
def valid_parentheses(s):
    stack = []  # Cria uma pilha vazia para armazenar os parênteses

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)  # Empilha o parêntese de abertura
        elif char == ')' or char == ']' or char == '}':
            if not stack:
                return False  # Se a pilha estiver vazia e encontrarmos um parêntese de fechamento, não é válido
            top = stack.pop()  # Desempilha o parêntese do topo da pilha
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False  # Se os tipos de parênteses não coincidirem, não é válido

    return len(stack) == 0

class Test(unittest.TestCase):
    test_cases = [
        ("()", True),
        ("()[]{}",True),
        ("(]", False),
        ("{[]}", True)
    ]
    functions = [valid_parentheses]
    def test_valid_parentheses(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()