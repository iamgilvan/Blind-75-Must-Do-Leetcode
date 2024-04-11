import unittest

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

class Test(unittest.TestCase):
    test_cases = [
        ("abcde", "ace",  3),
        ("abc", "abc", 3),
        ("abc", "def", 0)
    ]
    functions = [longestCommonSubsequence]
    def test_longest_common_subsequence(self):
        for function in self.functions:
            for s1, s2, expected in self.test_cases:
                result = function(s1, s2)
                assert result == expected

if __name__ == '__main__':
    unittest.main()