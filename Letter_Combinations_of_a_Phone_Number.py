import unittest

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#TC  O(n*4^n)
#SC O(1)
def letterCombinations(digits):
    cominations ={2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    res = []

    def dfs (digit_idx, path):
        if len(path) == len(digits):
            res.append(path)
            return
        for c in cominations[int(digits[digit_idx])]:
            dfs(digit_idx + 1, path + c)
    if digits:
        dfs(0, '')
    return res


class Test(unittest.TestCase):
    test_cases = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
    ]
    functions = [letterCombinations]
    def test_letter_combinations(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == "__main__":
    unittest.main()