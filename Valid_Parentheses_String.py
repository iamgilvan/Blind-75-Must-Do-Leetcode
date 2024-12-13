import unittest
# You are given a string s which contains only three types of characters: '(', ')' and '*'.

# Return true if s is valid, otherwise return false.

# A string is valid if it follows all of the following rules:

# Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# Every right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".

#TC O(n)
#TS O(1)
def valid_parentheses_string(s) -> bool:
    left = []
    star = []
    for i, ch in enumerate(s):
        if ch == '(':
            left.append(i)
        elif ch == '*':
            star.append(i)
        else:
            if not left and not star:
                return False
            if left:
                left.pop()
            else:
                star.pop()
    while left and star:
        if left.pop() > star.pop():
            return False
    return not left

class Test(unittest.TestCase):
    test_cases = [
        ("()", True),
        ("(*)",True),
        ("(*))", True)
    ]
    functions = [valid_parentheses_string]
    def test_valid_parentheses_string(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()