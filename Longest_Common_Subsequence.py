import unittest

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#     For example, "ace" is a subsequence of "abcde".

# A common subsequence of two strings is a subsequence that is common to both strings.

#TC O(m * n)
#TS O(m * n)
def longestCommonSubsequence(text1, text2):
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j],dp[i][j + 1])
    return dp[0][0]
# Time complexity: O(2^m+n)
# Space complexity: O(m+n)
def longest_common_subsequence(text1, text2):
    def dfs(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + dfs(i + 1, j + 1)
        return max(dfs(i, j + 1), dfs(i + 1, j))
    return dfs(0,0)

class Test(unittest.TestCase):
    test_cases = [
        ("abcde", "ace",  3),
        ("abc", "abc", 3),
        ("abc", "def", 0)
    ]
    functions = [longestCommonSubsequence, longest_common_subsequence]
    def test_longest_common_subsequence(self):
        for function in self.functions:
            for s1, s2, expected in self.test_cases:
                result = function(s1, s2)
                assert result == expected

if __name__ == '__main__':
    unittest.main()