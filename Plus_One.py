from collections import Counter
import heapq
import unittest

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#TC O(n)
#SC O(1)
def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
    ]
    functions = [plus_one]
    def test_plus_one(self):
        for function in self.functions:
            for d, expected in self.test_cases:
                result = function(d)
                assert result == expected

if __name__ == '__main__':
    unittest.main()