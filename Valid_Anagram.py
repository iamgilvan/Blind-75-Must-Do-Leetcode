import unittest
import math

#TC O(n log n)
#TS O(1)
def isAnagram(s: str, t: str) -> bool:
    return ''.join(sorted(s)) == ''.join(sorted(t))

class Test(unittest.TestCase):
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]
    functions = [isAnagram]
    def test_isAnagram(self):
        for function in self.functions:
            for t, s , expected in self.test_cases:
                result = function(s, t)
                assert result == expected

if __name__ == '__main__':
    unittest.main()