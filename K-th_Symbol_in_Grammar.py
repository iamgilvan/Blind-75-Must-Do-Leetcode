import unittest

# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

#     For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.


# Time Limit Exceeded
#O(N * 2^(N-1) : O(2^N)
def kth_symbol_in_grammar(n, k):
    output = ['0']

    for i in range(1, n):
        last_word = output[i - 1]
        word = ''
        for char in last_word:
            if char == '0':
                word += '01'
            else:
                word += '10'
        output.append(word)
    return int(output[n - 1 ][k - 1])

# O(2^(N-1)) : O(n) worked*
def kthGrammar(n: int, k: int) -> int:
    if n == 1:
        return 0

    middle = 2 ** (n - 2)  # Calcula o ponto médio da linha anterior
    if k <= middle:
        return kthGrammar(n - 1, k)
    else:
        return 1 - kthGrammar(n - 1, k - middle)

# best solution so far
# O(n log k) : O(n)
def kthGrammar_optimized(n: int, k: int) -> int:
    if n == 1:
        return 0
    parent = kthGrammar(n - 1, k/2 + k % 2)
    isKOdd = k % 2 == 1
    if parent == 1:
        return 1 if isKOdd else 0
    else:
        return 0 if isKOdd else 1

class Test(unittest.TestCase):
    test_cases = [
        (1, 1, 0),
        (2, 1, 0),
        (2, 2, 1),
        (3, 1, 0)
    ]
    functions = [kth_symbol_in_grammar, kthGrammar]
    def test_kth_symbol_in_grammar(self):
        for function in self.functions:
            for n, k, expected in self.test_cases:
                result = function(n, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()