import unittest

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#TC O(1) | SC O(1)
def reverse(x):
    org = x
    x = abs(x)
    res = int(str(x)[::-1])
    if org < 0:
        res *= -1
    if res < -(1 << 31) or res > (1 << 31) - 1:
        return 0
    return res

class Test(unittest.TestCase):
    test_cases = [
        (1234, 4321),
        (-1234, -4321),
        (1234236467, 0)
    ]
    functions = [reverse]
    def test_reverse(self):
        for function in self.functions:
            for a, expected in self.test_cases:
                result = function(a)
                assert result == expected

if __name__ == '__main__':
    unittest.main()