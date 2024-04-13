from collections import Counter
import unittest
import math

#TC O(n log n)
#TS O(1)
def isAnagram(s: str, t: str) -> bool:
    return ''.join(sorted(s)) == ''.join(sorted(t))

def isAnagramSorted(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def isAnagramCounter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

#TC O(1)
#TS O(1)
def isAnagramHashMap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counterS, counterT = {}, {}
    for i in range(len(s)):
        counterS[s[i]] = 1 + counterS.get(s[i], 0)
        counterT[t[i]] = 1 + counterT.get(t[i], 0)
    for c in counterS:
        if counterS[c] != counterT.get(c, 0):
            return False
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]
    functions = [isAnagram, isAnagramSorted, isAnagramCounter, isAnagramHashMap]
    def test_isAnagram(self):
        for function in self.functions:
            for t, s , expected in self.test_cases:
                result = function(s, t)
                assert result == expected

if __name__ == '__main__':
    unittest.main()