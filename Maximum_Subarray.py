from collections import defaultdict
from queue import Queue
import unittest
import sys
from collections import deque

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

class Test(unittest.TestCase):
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4],6),
        ([1], 1),
        ([-2,-1], -1),
        ([5,4,-1,7,8], 23),
        ([-1], -1),
    ]
    functions = [maximum_subarray]
    def test_group_anagram(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()