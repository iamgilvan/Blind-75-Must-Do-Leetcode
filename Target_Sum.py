from collections import Counter, defaultdict
import heapq
from typing import List
import unittest

# Time complexity: O(2^n)
# Space complexity: O(n)

def FindTargetSumWays(nums, target):
    def backtrack(i, total):
        if i ==len(nums):
                return  total == target

        return (backtrack(i + 1, total + nums[i]) +
                    backtrack(i + 1, total - nums[i]))
    return backtrack(0, 0)


# Time complexity: O(n∗t)
# Space complexity: O(t)

def findTargetSumWays_dp(nums: List[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    for num in nums:
        next_dp = defaultdict(int)
        for total, count in dp.items():
            next_dp[total + num] += count
            next_dp[total - num] += count
        dp = next_dp

    return dp[target]
class Test(unittest.TestCase):
    test_cases = [
        ([1,1,1,1,1], 3, 5),
        ([1], 1, 1),
    ]
    functions = [FindTargetSumWays, findTargetSumWays_dp]
    def test_FindTargetSumWays(self):
        for function in self.functions:
            for nums, k, expected in self.test_cases:
                result = function(nums, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()