import unittest

#TC: (n^2)
#TS : O(n)
def word_break(s, wordDict):
    wordDict = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for end in range(1, n + 1):
        for start in range(end):
            if dp[start] and s[start:end] in wordDict:
                dp[end] = True
                break
    return dp[n]

class Test(unittest.TestCase):
    test_cases = [
        ("applepenapple", ["apple","pen"], True),
        ("leetcode",["leet","code"], True),
        ("catsandog", ["cats","dog","sand","and","cat"], False),
        ("bb", ["a","b","bbb","bbbb"], True)
    ]
    functions = [word_break]
    def test_valid_palindrome(self):
        for function in self.functions:
            for s, wordDict, expected in self.test_cases:
                result = function(s, wordDict)
                assert result == expected

if __name__ == '__main__':
    unittest.main()