import unittest

# Time complexity: O(2^n+m)
# Space complexity: O(n+m)

def isInterleave_recursive(s1: str, s2: str, s3: str) -> bool:
    dp = {}
    def dfs(i, j):
        if i == len(s1) and j == len(s2):
            return True
        if (i, j) in dp:
            return dp[(i, j)]

        if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
            return True
        if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
            return True
        dp[(i, j)] = False
        return False
    return dfs(0,0)

# Time complexity: O(n.m)
# Space complexity: O(n.m)
def isInterleave_dp( s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True
    for i in range(len(s1), -1 , -1):
        for j in range(len(s2), -1 , -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][ j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][ j + 1]:
                dp[i][j] = True
    return dp[0][0]
class Test(unittest.TestCase):
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca","aadbbbaccc", False),
        ("", "", "", True),
    ]
    functions = [isInterleave_recursive, isInterleave_dp]
    def test_isInterleave(self):
        for function in self.functions:
            for s1, s2, s3, expected in self.test_cases:
                result = function(s1, s2, s3)
                assert result == expected

if __name__ == '__main__':
    unittest.main()