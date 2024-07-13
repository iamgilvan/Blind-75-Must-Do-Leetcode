import unittest

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

#TC O(logn)
#TS O(1)
def binary_search(arr, target):
    if not arr: return -1
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class Test(unittest.TestCase):
    test_cases = [
        ([-1,0,3,5,9,12], 9, 4),
        ([-1,0,3,5,9,12], 2, -1),
        ([-1,0,3,5,9,12], 13, -1)
    ]
    functions = [binary_search]
    def test_binary_search(self):
        for function in self.functions:
            for n,t, expected in self.test_cases:
                result = function(n, t)
                assert result == expected

if __name__ == '__main__':
    unittest.main()