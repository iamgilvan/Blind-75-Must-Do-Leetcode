import unittest

# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

#TC O(n^3)
#TS O(n^2)
def burst_balloons(nums) -> int:
    nums = [1] + nums + [1]
    cache = {}
    def dfs(l,r):
        if l > r:
            return 0
        if (l,r) in cache:
            return cache[(l,r)]
        cache [(l,r)] = 0
        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1]
            coins += dfs(l, i - 1) + dfs(i + 1, r)
            cache[(l,r)] = max(cache[(l,r)], coins)
        return cache[(l,r)]
    return dfs(1, len(nums) - 2)

#TC O(n * 2^n)
#TS O(n * 2^n)
def burst_balloons_recursion(nums) -> int:
    nums = [1] + nums + [1]
    def dfs(nums):
        if len(nums) == 2:
            return 0
        maxCoins = 0
        for i in range(1, len(nums) - 1):
            coins = nums[i - 1] * nums[i] * nums[i + 1]
            coins += dfs(nums[:i] + nums[i + 1:])
            maxCoins = max(maxCoins, coins)
        return maxCoins
    return dfs(nums)

class Test(unittest.TestCase):
    test_cases = [
        ([3,1,5,8],  167),
        ([1,5], 10),
    ]
    functions = [burst_balloons, burst_balloons_recursion]
    def test_burst_balloons(self):
        for function in self.functions:
            for nums, expected in self.test_cases:
                result = function(nums)
                assert result == expected

if __name__ == '__main__':
    unittest.main()