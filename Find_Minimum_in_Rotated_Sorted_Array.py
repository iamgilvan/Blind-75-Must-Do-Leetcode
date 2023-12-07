import unittest

def find_minimum_in_rotate_sorted_array(arr):
    if len(arr) == 1:
        return arr[0]
    point_rotation = find_rotation_point(arr)
    return arr[point_rotation]

def find_rotation_point(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left

class Test(unittest.TestCase):
    test_cases = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11),
    ]
    functions = [find_minimum_in_rotate_sorted_array]
    def test_find_minimum_in_rotate_sorted_array(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()