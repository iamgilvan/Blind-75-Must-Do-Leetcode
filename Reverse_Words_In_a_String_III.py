import unittest
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# time complexity :  O(n)
def reverse_words_in_a_string(s):
    words = s.split()
    res = ''
    for word in words:
        res += word[::-1] + " "
    return res.strip()

class Test(unittest.TestCase):
    test_cases = [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("Mr Ding", "rM gniD"),
    ]
    functions = [reverse_words_in_a_string]
    def test_reverse_words_in_a_string(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()