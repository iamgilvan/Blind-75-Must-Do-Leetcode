import unittest

#TC O(n)
#TS O(1)
def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

class Test(unittest.TestCase):
    test_cases = [
        ([0,1,0,3,2,3], 4),
        ([10,9,2,5,3,7,101,18], 4),
        ([7,7,7,7,7,7,7], 1)
    ]
    functions = [lengthOfLIS]
    def test_length_of_lis(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()