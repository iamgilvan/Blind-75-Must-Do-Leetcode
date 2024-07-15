import unittest

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#TC O(26n)
def characterReplacement(s, k):

    count = {}
    res = 0
    maxf = 0
    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

class Test(unittest.TestCase):
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ]
    functions = [characterReplacement]
    def test_characterReplacement(self):
        for function in self.functions:
            for s, k, expected in self.test_cases:
                result = function(s, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()