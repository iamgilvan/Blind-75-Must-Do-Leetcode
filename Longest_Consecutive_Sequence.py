
import unittest


#TC: O(n log n)
#TS : O(n)
def longest_consecutive_sequence(arr):
    if not arr: return 0
    arr.sort()
    count_max = 0
    count = 1
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]: continue
        if arr[i-1] + 1 == arr[i]:
            count += 1
        else:
            count_max = max(count, count_max)
            count = 1
    return max(count, count_max)

#TC: O(n)
#TS : O(n)
def longest_consecutive_sequence_improved(arr):
    if not arr: return 0
    num_set = set(arr)
    max_length = 0

    for num in num_set:
        # Verifica se o número atual é o início de uma sequência
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Expande a sequência para a direita
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

class Test(unittest.TestCase):
    test_cases = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,2,0,1], 3)
    ]
    functions = [longest_consecutive_sequence, longest_consecutive_sequence_improved]
    def test_longest_consecutive_sequence(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()