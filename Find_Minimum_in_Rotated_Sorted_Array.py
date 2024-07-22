import unittest

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

#TC O(log n)
#TS O(1)
def find_minimum_in_rotate_sorted_array(arr):
    if len(arr) == 1:
        return arr[0]
    point_rotation = find_rotation_point(arr)
    return arr[point_rotation]

def find_rotation_point(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left

#TC O(n)
def find_minimum_in_rotate_sorted_array_ii(arr):
    left = 0
    right = len(arr) - 1
    while arr[left] > arr[right]:
        left += 1
    return arr[left]

class Test(unittest.TestCase):
    test_cases = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11),
    ]
    functions = [find_minimum_in_rotate_sorted_array, find_minimum_in_rotate_sorted_array_ii]
    def test_find_minimum_in_rotate_sorted_array(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()