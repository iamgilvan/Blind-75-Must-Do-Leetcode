import unittest
import math

#TC O(n log n)
#TS O(1)
def missingNumber(nums) -> int:
    nums.sort()
    for i in range(len(nums)):
        if i not in nums:
            return i
    else:
        return i + 1

class Test(unittest.TestCase):
    test_cases = [
        ([3,0,1], 2),
        ([0,1], 2),
        ([9,6,4,2,3,5,7,0,1], 8)
    ]
    functions = [missingNumber]
    def test_isAnagram(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()