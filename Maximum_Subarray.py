import unittest
import sys
# Given an integer array nums, find the
# subarray
# with the largest sum, and return its sum.
# Time complexity  O(n) | space complexity O(1).
def maximum_subarray(array):
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0
    all_smaller_0 = all(i < 0 for i in array)
    for element in array:
        max_ending_here += element
        if max_ending_here < 0 and not all_smaller_0:
            max_ending_here = 0

        max_so_far = max(max_ending_here, max_so_far, element)

    return max_so_far

def maximum_subarray_ii(nums):
    res = nums[0]
    total = 0

    for n in nums:
        if total < 0:
            total = 0
        total += n
        res = max(res, total)

    return res

class Test(unittest.TestCase):
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4],6),
        ([1], 1),
        ([-2,-1], -1),
        ([5,4,-1,7,8], 23),
        ([-1], -1),
    ]
    functions = [maximum_subarray]
    def test_maximum_subarray_ii(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()