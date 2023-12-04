import math
import unittest

#TC O(n)
#TS O(1)
def maximum_product_subarray(arr):
    max_p = max(arr)
    curMin, curMax = 1, 1

    for n in arr:
        if n == 0:
            curMin = curMax = 1
            continue
        tmp = curMax * n
        curMax = max(n* curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        max_p = max(max_p, curMax)

    return max_p


class Test(unittest.TestCase):
    test_cases = [
        ([2,3,-2,4],  6),
        ([-2,0,-1],  0),
        ([-1,-1],  1)
    ]
    functions = [maximum_product_subarray]
    def test_maximum_product_subarray(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()