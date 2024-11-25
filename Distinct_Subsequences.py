import unittest

# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

#TC O(m * n)
#TS O(m * n)
def num_distinct(s: str, t: str) -> int:
    cache = {}
    def dfs(i, j):
        if j == len(t): return 1
        if i == len(s): return 0

        if (i, j) in cache:
            return cache[(i,j)]
        if s[i] == t[j]:
            cache[(i,j)] = dfs(i + 1, j + 1) +  dfs(i + 1, j)
        else:
            cache[(i,j)] = dfs(i + 1, j)
        return cache[(i,j)]
    return dfs(0,0)

# Time complexity: O(m * n)
# Space complexity: O(n)
def num_distinct_dp(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(m - 1, -1, -1):
        prev = 1
        for j in range(n - 1, -1, -1):
            res = dp[j]
            if s[i] == t[j]:
                res += prev
            prev = dp[j]
            dp[j] = res
    return dp[0]

class Test(unittest.TestCase):
    test_cases = [
        ("rabbbit", "rabbit",  3),
        ("babgbag", "bag", 5),
    ]
    functions = [num_distinct, num_distinct_dp]
    def test_num_distinct(self):
        for function in self.functions:
            for s1, s2, expected in self.test_cases:
                result = function(s1, s2)
                assert result == expected

if __name__ == '__main__':
    unittest.main()