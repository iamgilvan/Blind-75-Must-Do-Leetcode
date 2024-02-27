import unittest

#TC O(num)
#TS O(num)
def countBits(num):
    # Inicialize uma lista para armazenar o número de bits definidos para cada número
    bits_count = [0] * (num + 1)

    # Itere de 1 a num
    for i in range(1, num + 1):
        # Se o número for par, o número de bits definidos é o mesmo que a metade do número
        if i % 2 == 0:
            bits_count[i] = bits_count[i // 2]
        # Se o número for ímpar, o número de bits definidos é o mesmo que a metade do número mais 1
        else:
            bits_count[i] = bits_count[i // 2] + 1

    return bits_count

class Test(unittest.TestCase):
    test_cases = [
        (2, [0, 1,1]),
        (5, [0,1,1,2,1,2]),
    ]
    functions = [countBits]
    def test_countBits(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()