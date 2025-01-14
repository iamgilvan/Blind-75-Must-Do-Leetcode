from typing import List
import unittest

# Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

# Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

# You may not use any built-in library functions.

#TC O(logn) / SC O(logn)
def my_pow(x, n) -> float:
    if n == 0:
        return 1.0
    elif n % 2 == 0:
        half = pow(x, n // 2)
        return half * half
    else:
        half = pow(x, (n - 1) // 2)
        return x * half * half

#TC O(n) / SC O(1)
def myPow(x, n) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    res = 1
    for i in range(abs(n)):
        res *= x
    return res if n >= 0 else 1 / res
class Test(unittest.TestCase):
    test_cases = [
        (2.00000,10, 1024.00000),
        (2.10000, 3 , 9.261000),
        (2.10000, -2 , 0.25000),
    ]
    functions = [myPow]
    def test_my_pow(self):
        for function in self.functions:
            for x, n, expected in self.test_cases:
                result = round(function(x, n), 5)
                assert result == expected

if __name__ == '__main__':
    unittest.main()