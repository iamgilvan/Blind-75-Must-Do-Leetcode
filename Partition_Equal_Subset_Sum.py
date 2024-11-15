from typing import List
import unittest

#TC O(n * target)
#TS O(n * target)
def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False
    target = sum(nums) // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[-1]

class Test(unittest.TestCase):
    test_cases = [
        ([1,5,11,5], True),
        ([1,2,3,5], False),
        ([2,2,1,1], True),
    ]
    functions = [canPartition]
    def test_can_partition(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()