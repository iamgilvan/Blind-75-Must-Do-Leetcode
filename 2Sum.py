import unittest

#O(n^2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]
    return []

#O(n^2)
def two_sum_2(nums, target):
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            if (nums[i] + nums[j]) == target:
                return [i, j]
            j += 1
    return []

#O(n) linear
def two_sum_linear(nums, target):
    num_indices = {}  # Dicionário para rastrear os índices dos números percorridos
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []

class Test(unittest.TestCase):
    test_cases = [
        ([2,7,11,15], 9, [0, 1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6,[0,1]),
    ]
    functions = [two_sum, two_sum_2, two_sum_linear]
    def test_two_sum(self):
        for function in self.functions:
            for arr, target, expected in self.test_cases:
                result = function(arr, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()