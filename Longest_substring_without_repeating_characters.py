import unittest

# Time Complexity: O(N), Space Complexity: O(1)
def Longest_substring_without_repeating_characters(s):
    subs = set()
    idxSub = 0
    result = 0
    for i in range(len(s)):
        while s[i] in subs:
            subs.remove(s[idxSub])
            idxSub += 1
        subs.add(s[i])
        result = max(result, len(subs))
    return result


class Test(unittest.TestCase):
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3)
    ]
    functions = [Longest_substring_without_repeating_characters]
    def test_Longest_substring_without_repeating_characters(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()