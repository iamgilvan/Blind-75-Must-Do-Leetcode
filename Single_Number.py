from collections import Counter
from typing import List
import unittest

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

#TC O(n) / SC O(1)
def singleNumber(nums: List[int]) -> int:
    my_dict = Counter(nums)
    for key, value in my_dict.items():
        if value == 1:
            return key
    return None

def single_number(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res = num ^ res
    return res

class Test(unittest.TestCase):
    test_cases = [
        ([2,2,1], 1),
        ([4,1,2,1,2], 4),
        ([1], 1),
    ]
    functions = [single_number]
    def test_single_number(self):
        for function in self.functions:
            for  n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()