import unittest

def minimum_window_substring(s, t):
    # simple check
    if t == "": return ""
    # count occurrences
    t_counts, window_counts = {}, {}
    for char in t:
        t_counts[char] = 1 + t_counts.get(char, 0)

    have, need = 0, len(t_counts)
    result, resultLen = [-1, -1], float("infinity")
    left = 0
    for i in range(len(s)):
        char = s[i]
        window_counts[char] = 1 + window_counts.get(char, 0)

        if char in t_counts and window_counts[char] == t_counts[char]:
            have +=1

        while have == need:
            # update our result
            if (i - left + 1) < resultLen:
                result = [left, i]
                resultLen = i - left + 1
            # pop from the left of our window
            window_counts[s[left]] -= 1
            if s[left] in t_counts and window_counts[s[left]] < t_counts[s[left]]:
                have -= 1
            left += 1
    left, i = result
    return s[left : i + 1] if resultLen != float("infinity") else ""

class Test(unittest.TestCase):
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ]
    functions = [minimum_window_substring]
    def test_climbing_stairs(self):
        for function in self.functions:
            for s, t, expected in self.test_cases:
                result = function(s, t)
                assert result == expected

if __name__ == '__main__':
    unittest.main()