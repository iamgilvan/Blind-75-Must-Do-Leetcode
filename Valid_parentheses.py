import unittest

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
    def test_two_sum(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()