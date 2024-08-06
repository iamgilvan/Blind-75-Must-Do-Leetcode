import collections
from functools import cmp_to_key
import unittest

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.
#TC O(n log n)
#TS O(1)
def largest_number(nums):
    for i, n in enumerate(nums):
        nums[i] = str (n)

    def compare(n1, n2):
        if n1 + n2 > n2 + n1: return -1
        else: return 1
    nums = sorted(nums, key=cmp_to_key(compare))
    return str(int("".join(nums)))

class Test(unittest.TestCase):
    test_cases = [
        ([10,2], "210"),
        ([3,30,34,5,9], "9534330"),
    ]
    functions = [largest_number]
    def test_largest_number(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()