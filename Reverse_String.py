
import unittest
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.
# time complexity :  O(n)
def reverse_string(s):
    """
    Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

class Test(unittest.TestCase):
    test_cases = [
        (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
        (["h","e","l","l","o"], ["o","l","l","e","h"]),
    ]
    functions = [reverse_string]
    def test_reverse_string(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                function(arr)
                assert arr == expected

if __name__ == '__main__':
    unittest.main()