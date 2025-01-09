from copy import deepcopy
import unittest

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# -Starting with any positive integer, replace the number by the sum of the squares of its digits.
# -Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# -Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Time complexity O(log n) Space complexity O(log n)
def happy_number(n):
    seen = set()
    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return True


class Test(unittest.TestCase):
    test_cases = [
        (19,True),
        (2, False),
        (100, True),
        (101, False),
    ]
    functions = [happy_number]
    def test_happy_number(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()