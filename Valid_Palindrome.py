import unittest

def isPalindrome(s: str) -> bool:
    s = ''.join([x.lower() for x in s if x.isalnum()])
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s: str) -> bool:
    s = ''.join([x.lower() for x in s if x.isalnum()])
    return s == s[::-1]

class Test(unittest.TestCase):
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car",False),
        (" ", True)
    ]
    functions = [valid_palindrome, isPalindrome]
    def test_two_sum(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()