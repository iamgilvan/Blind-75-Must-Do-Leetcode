import unittest

# Given a string s, return the longest palindromic substring in s.

# SC:O(1)
# Time Complexity O(n^2) 
def Longest_palindromic_substring(s):
    r = 0
    pointer = len(s)
    max_result = 0
    subs_result = {0 : ""}
    while r < len(s):
        subs = s[r:pointer]
        if subs == subs[::-1]:
            max_result = max(max_result, len(subs))
            if len(subs) > list(subs_result.keys())[0]:
                subs_result = {}
                subs_result[max_result] = subs
        pointer -=1

        if pointer <= r + 1:
            r += 1
            pointer = len(s)

    return list(subs_result.values())[0]

 #time complexity O(n^2) space complexity: O(1)
def Longest_palindromic_substring_optmized(s):
    result = ""
    resultLen = 0

    def helper(s, leftPointer, rightPointer, result, resultLen):
        while leftPointer >= 0 and rightPointer  < len(s) and s[leftPointer] == s[rightPointer]:
            if (rightPointer - leftPointer + 1) > resultLen:
                result = s[leftPointer:rightPointer+1]
                resultLen = rightPointer - leftPointer + 1
            leftPointer -= 1
            rightPointer += 1
        return result, resultLen
    for i in range(len(s)):
        # odd length
        result, resultLen = helper(s, i, i, result, resultLen)
        # even length
        result, resultLen = helper(s, i, i + 1, result, resultLen)
    return result

def longest_palindromic_substring_manacher(s):
    if len(s) <= 1:
        return s

    # Transform the string
    modified_s = '#'.join('^{}$'.format(s))
    n = len(modified_s)
    p = [0] * n
    C, R = 0, 0  # Center and Right bound of the current palindrome

    for i in range(1, n - 1):
        i_mirror = 2 * C - i  # Mirror of i around center C

        if R > i:
            p[i] = min(R - i, p[i_mirror])

        # Attempt to expand palindrome centered at i
        while modified_s[i + 1 + p[i]] == modified_s[i - 1 - p[i]]:
            p[i] += 1

        # If palindrome centered at i expands past R,
        # adjust center based on expanded palindrome
        if i + p[i] > R:
            C, R = i, i + p[i]

    # Find the maximum element in p
    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    end = start + max_len
    return s[start:end]


class Test(unittest.TestCase):
    test_cases = [
        ("babad", "bab"),
        ("cbbd", "bb"),
    ]
    functions = [Longest_palindromic_substring, Longest_palindromic_substring_optmized,longest_palindromic_substring_manacher]
    def test_longest_palindromic_substring(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()