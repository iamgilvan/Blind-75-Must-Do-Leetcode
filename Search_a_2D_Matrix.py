import unittest

# You are given an m x n integer matrix matrix with the following two properties:

#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

#TC O(log (n x m))
#TS O(1)
def binary_search_2d_arr(arr, target):
    ROWS, COLS = len(arr), len(arr[0])
    top, bot = 0, ROWS
    while top <=bot:
        row = (top + bot) // 2
        if target > arr[row][-1]:
            top = row + 1
        elif target < arr[row][0]:
            bot = row - 1
        else:
            break
    if not (top <= bot):
        return False
    row = (top + bot) // 2
    left, right = 0, COLS-1
    while left <= right:
        mid = (left + right) // 2
        if arr[row][mid] == target:
            return True
        if arr[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def binary_search_2d_arr_brute_force(arr, target):
    for row in arr:
        if target in row:
            return True
    return False

class Test(unittest.TestCase):
    test_cases = [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
    ]
    functions = [binary_search_2d_arr, binary_search_2d_arr_brute_force]
    def test_binary_search(self):
        for function in self.functions:
            for arr, t, expected in self.test_cases:
                result = function(arr, t)
                assert result == expected

if __name__ == '__main__':
    unittest.main()