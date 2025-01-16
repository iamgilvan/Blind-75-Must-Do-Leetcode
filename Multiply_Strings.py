from typing import List
import unittest

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

#TC O(m * n) / SC O(m+n)
def multiply(num1: str, num2: str) -> str:
    if "0" in [num1, num2]:
        return "0"
    res = [0] * (len(num1) + len(num2))
    num1, num2 = num1[::-1], num2[::-1]
    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            digit = int(num1[i1]) * int(num2[i2])
            res[i1 + i2] += digit
            res[i1 + i2 + 1] += res[i1 + i2] // 10
            res[i1 + i2] = res[i1 + i2] % 10
    res, beg = res[::-1], 0
    while beg < len(res) and res[beg] == 0:
        beg += 1
    res = map(str, res[beg:])
    return "".join(res)

class Test(unittest.TestCase):
    test_cases = [
        ("2", "3", "6"),
        ("123", "456", "56088"),
        ("3", "4", "12"),
        ("111", "222", "24642"),
    ]
    functions = [multiply]
    def test_multiply(self):
        for function in self.functions:
            for num1, num2, expected in self.test_cases:
                result = function(num1, num2)
                assert result == expected

if __name__ == '__main__':
    unittest.main()