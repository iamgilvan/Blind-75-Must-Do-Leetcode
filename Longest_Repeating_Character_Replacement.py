import unittest

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