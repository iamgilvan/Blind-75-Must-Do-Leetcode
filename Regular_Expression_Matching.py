import re
import unittest

# You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

# Return true if the pattern matches the entire input string, otherwise return false.

#     '.' Matches any single character
#     '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

#TC O(2^m + n)
#TS O(m + n)
def is_match(s, p) -> bool:

    def dfs(si, pi):
        if pi == len(p):
            return si == len(s)
        match = si < len(s) and (s[si] == p[pi] or p[pi] == ".")

        if (pi + 1) < len(p) and p[pi + 1] == "*":
            return (dfs(si, pi + 2) or # don't use *
                    (match and dfs(si + 1, pi)))
        if match:
            return dfs(si + 1, pi + 1)
        return False
    return dfs(0,0)

#TC O(m * n)
#TS O(m * n)
def is_match_dp(s, p) -> bool:
    cache = {}
    def dfs(si, pi):
        if pi == len(p):
            return si == len(s)

        if (si, pi) in cache:
            return cache[(si,pi)]

        match = si < len(s) and (s[si] == p[pi] or p[pi] == ".")

        if (pi + 1) < len(p) and p[pi + 1] == "*":
            cache[(si,pi)] = (dfs(si, pi + 2) or # don't use *
                    (match and dfs(si + 1, pi)))
            return cache[(si,pi)]
        if match:
            cache[(si,pi)] = dfs(si + 1, pi + 1)
            return cache[(si,pi)]
        cache[(si,pi)] = False
        return False
    return dfs(0,0)

def is_match_re(s, p) -> bool:
    return bool(re.search(f'^{p}$', s))
class Test(unittest.TestCase):
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("aa", ".b", False),
        ("nnn", "n*", True),
        ("xyz", ".*z", True),
    ]
    functions = [is_match, is_match_dp, is_match_re]
    def test_is_match(self):
        for function in self.functions:
            for s, p, expected in self.test_cases:
                result = function(s, p)
                assert result == expected

if __name__ == '__main__':
    unittest.main()