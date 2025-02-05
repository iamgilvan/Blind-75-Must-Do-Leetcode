from collections import Counter
import heapq
import unittest

#TC O(1) | SC O(1)
def getSum(a, b):
    # Máscara para limitar os números a 32 bits
    MASK = 0xFFFFFFFF
    # Enquanto b não for 0
    while b != 0:
        # Soma sem considerar o carry
        sum_without_carry = (a ^ b) & MASK
        # Carry
        carry = ((a & b) << 1) & MASK
        # Atualizando a e b para a próxima iteração
        a = sum_without_carry
        b = carry

    # Lidando com overflow
    if a & (1 << 31):
        # Se for negativo, convertemos para o complemento de dois
        return a | ~MASK
    else:
        return a if a < 0x7FFFFFFF else ~(a ^ MASK)

class Test(unittest.TestCase):
    test_cases = [
        (1, 2, 3),
        (2, 3, 5)
    ]
    functions = [getSum]
    def test_getSum(self):
        for function in self.functions:
            for a, b, expected in self.test_cases:
                result = function(a, b)
                assert result == expected

if __name__ == '__main__':
    unittest.main()