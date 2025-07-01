import unittest

#TC: O(logN)
#TS : O(1)
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False  # negativos nunca são palíndromos
    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num
#TC: O(logN/2)
#TS : O(1)
def isPalindrome_half(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # Para número com número ímpar de dígitos, ignoramos o do meio: reversed_half // 10
    return x == reversed_half or x == reversed_half // 10


class Test(unittest.TestCase):
    test_cases = [
        (121, True),
        (10,False),
        (-121, False)
    ]
    functions = [isPalindrome, isPalindrome_half]
    def test_palindrome_number(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()