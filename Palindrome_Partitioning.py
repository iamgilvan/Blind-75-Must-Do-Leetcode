import unittest

# Given a string s, partition s such that every
# substring
# of the partition is a
# palindrome
# . Return all possible palindrome partitioning of s.

#TC  O(2^n)
#SC O(1)
def palindrome_partitioning(s):
    res = []
    part = []

    def isPalindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                 return False
            l += 1
            r -= 1
        return True

    def dfs (start):
        if start >= len(s):
            res.append(part.copy())
            return
        for i in range(start, len(s)):
            if isPalindrome(start, i):
                part.append(s[start:i+1])
                dfs(i+1)
                part.pop()
    dfs(0)
    return res


class Test(unittest.TestCase):
    test_cases = [
        ("aab", [["a","a","b"],["aa","b"]]),
        ("a", [["a"]]),
    ]
    functions = [palindrome_partitioning]
    def test_palindrome_partitioning(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == "__main__":
    unittest.main()