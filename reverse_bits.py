import unittest

# Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.



#TC: O(1)
#EC: O(1)
def reverse_bit(n):
    result = 0
    bit_length = 32
    for i in range(bit_length):
        bit = (n >> i) & 1
        result |= bit << (bit_length - 1 - i)
    return result

class Test(unittest.TestCase):
    test_cases = [
        (0b00000010100101000001111010011100, 964176192 ),
        (0b11111111111111111111111111111101, 3221225471 ),
    ]
    functions = [reverse_bit]
    def test_reverse_bit(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()