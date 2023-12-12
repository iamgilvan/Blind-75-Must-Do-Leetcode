import unittest

#TC: O(n)
#EC: O(1)
def number_of_one_bits(n):
    result = 0
    for i in range(n.bit_length()):
        bits = (n >> i) & 1
        if bits == 0: continue
        result += 1
    return result

class Test(unittest.TestCase):
    test_cases = [
        (0b00000000000000000000000000001011, 3 ),
        (0b00000000000000000000000010000000, 1 ),
        (0b11111111111111111111111111111101, 31)
    ]
    functions = [number_of_one_bits]
    def test_reverse_bit(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()