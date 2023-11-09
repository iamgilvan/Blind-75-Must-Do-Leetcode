import unittest

def decode_ways(s):
    dp = { len(s) : 1}
    # loop from the end to the beginning
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            dp[i] += dp[i + 2]
    return dp[0]

class Test(unittest.TestCase):
    test_cases = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ]
    functions = [decode_ways,]
    def test_group_anagram(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()